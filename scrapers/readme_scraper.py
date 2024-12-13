from bs4 import BeautifulSoup
from typing import List, Optional, Tuple, Dict, Any
from .base_scraper import BaseScraper, PageContent
from urllib.parse import urljoin
import logging

logger = logging.getLogger(__name__)

class ReadmeScraper(BaseScraper):
    """Scraper for ReadMe.com documentation sites"""

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a ReadMe site"""
        return bool(
            'readme.io' in domain or
            'deepgram.com' in domain or  # Add Deepgram domain
            soup.find('meta', {'name': 'readme-deploy'}) or
            soup.find('div', {'class': 'markdown-body'}) or
            soup.find('div', {'class': 'content-body'})  # Add Deepgram content class
        )

    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extract ReadMe navigation elements"""
        nav_elements = []
        
        # Try to find navigation in different possible locations
        nav = self.soup.find('nav', {'class': 'sidebar'})
        if nav:
            nav_elements.append(nav)
            return nav_elements
            
        # Try Deepgram-specific navigation
        nav = self.soup.find('nav', {'aria-label': 'Docs navigation'})
        if nav:
            nav_elements.append(nav)
            return nav_elements
            
        # Try alternate navigation structures
        nav_elements.extend(self.soup.find_all(
            ['nav', 'div'],
            class_=lambda x: x and (
                'sidebar' in x.lower() or
                'navigation' in x.lower() or
                'menu' in x.lower() or
                'nav-' in x.lower()  # Add common nav prefix
            )
        ))
        
        # If still no navigation found, try finding lists in sidebars
        if not nav_elements:
            sidebar = self.soup.find('div', class_=lambda x: x and 'sidebar' in x.lower())
            if sidebar:
                nav_elements.append(sidebar)
        
        return nav_elements

    def extract_main_content(self) -> Optional[BeautifulSoup]:
        """Extract ReadMe main content"""
        # Try Deepgram-specific content first
        main_content = self.soup.find('div', {'class': 'content-body'})
        if main_content:
            return main_content
            
        # Try to find content in markdown-body
        main_content = self.soup.find('div', {'class': 'markdown-body'})
        if main_content:
            return main_content
            
        # Try alternate content containers
        main_content = self.soup.find(
            ['main', 'article', 'div'],
            class_=lambda x: x and (
                'content' in x.lower() or
                'documentation' in x.lower() or
                'doc-content' in x.lower() or
                'article-' in x.lower()  # Add common article prefix
            )
        )
        
        # If still no content found, try the main tag
        if not main_content:
            main_content = self.soup.find('main')
        
        return main_content

    def process_special_elements(self, content: BeautifulSoup) -> None:
        """Process ReadMe-specific elements"""
        # Remove navigation elements
        for nav in content.find_all(['nav', 'aside']):
            nav.decompose()
            
        # Remove header elements
        for header in content.find_all('header'):
            header.decompose()
            
        # Remove API explorer elements
        for explorer in content.find_all(class_=lambda x: x and 'api-explorer' in x.lower()):
            explorer.decompose()
            
        # Remove code tabs (but keep code content)
        for tabs in content.find_all(class_=lambda x: x and 'code-tabs' in x.lower()):
            code = tabs.find('code')
            if code:
                tabs.replace_with(code)
            else:
                tabs.decompose()
                
        # Process Deepgram-specific elements
        for element in content.find_all(class_=lambda x: x and any(cls in str(x).lower() for cls in [
            'feedback-', 'edit-', 'toolbar-', 'toc-'
        ])):
            element.decompose()

    def extract_page_metadata(self, content: BeautifulSoup, url: str) -> PageContent:
        """Extract page metadata including title, order, section, etc."""
        # Try to find the title in h1 or title tags
        title_tag = content.find('h1') or self.soup.find('title')
        title = title_tag.get_text().strip() if title_tag else url
        
        # Get navigation context if available
        nav = self.extract_navigation_elements()
        section = ""
        subsection = ""
        order = 0
        weight = 0
        is_index = False
        
        if nav and nav[0]:
            # Try to find the current page in navigation
            current_link = nav[0].find('a', href=lambda x: x and url.endswith(x))
            if current_link:
                # Look for parent sections
                parent = current_link.find_parent(['div', 'section', 'nav'])
                if parent:
                    section_header = parent.find_previous(['h2', 'h3'])
                    if section_header:
                        section = section_header.get_text().strip()
                    
                    # Try to find subsection
                    subsection_header = parent.find_previous(['h3', 'h4'])
                    if subsection_header and subsection_header != section_header:
                        subsection = subsection_header.get_text().strip()
                    
                    # Calculate order based on position
                    siblings = parent.find_all('a', href=True)
                    order = siblings.index(current_link) if current_link in siblings else 0
                    
                    # Check if this is an index/overview page
                    is_index = any(word in title.lower() for word in ['introduction', 'overview', 'getting started'])
        
        return PageContent(
            url=url,
            title=title,
            content="",  # Content will be set later
            order=order,
            section=section,
            subsection=subsection,
            weight=weight,
            is_index=is_index
        )

    def extract_links(self, nav_elements: List[BeautifulSoup], visited_urls: set) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract links and their metadata from navigation elements"""
        links = []
        for nav in nav_elements:
            logger.debug(f"Processing navigation element: {nav.name}, class: {nav.get('class', [])}")
            
            # Find all links in the navigation
            for a in nav.find_all('a', href=True):
                href = a['href']
                full_url = urljoin(self.base_url, href)
                
                # Handle both relative and absolute URLs
                if href.startswith('/') or href.startswith(self.base_url):
                    if full_url.startswith(self.base_url) and full_url not in visited_urls:
                        # Extract metadata
                        metadata = {
                            'title': a.get_text(strip=True),
                            'order': self._get_element_order(a),
                            'section': self._get_parent_section(a),
                            'subsection': self._get_parent_subsection(a),
                            'weight': self._get_element_weight(a),
                            'is_index': self._is_index_page(a)
                        }
                        logger.debug(f"Found link: {full_url} with metadata: {metadata}")
                        links.append((full_url, metadata))
        
        # Sort links by section, subsection, order, and weight
        sorted_links = sorted(links, key=lambda x: (
            x[1]['section'],
            x[1]['subsection'],
            x[1]['order'],
            x[1]['weight']
        ))
        
        logger.debug(f"Returning {len(sorted_links)} sorted links")
        return sorted_links

    def _get_element_order(self, element: BeautifulSoup) -> int:
        """Get the order of an element from its attributes or position"""
        # Check common ordering attributes
        order = element.get('data-order', -1)
        if order == -1:
            order = element.get('data-position', -1)
        if order == -1:
            # Try to get order from parent list item
            li = element.find_parent('li')
            if li:
                siblings = li.find_previous_siblings()
                order = len(siblings)
        return int(order) if str(order).isdigit() else 999999

    def _get_parent_section(self, element: BeautifulSoup) -> str:
        """Get the parent section name"""
        section = ""
        parent = element.find_parent(['div', 'section', 'nav'])
        if parent:
            section_header = parent.find_previous(['h2', 'h3'])
            if section_header:
                section = section_header.get_text(strip=True)
        return section

    def _get_parent_subsection(self, element: BeautifulSoup) -> str:
        """Get the parent subsection name"""
        subsection = ""
        parent = element.find_parent(['div', 'section', 'nav'])
        if parent:
            subsection_header = parent.find_previous(['h3', 'h4'])
            if subsection_header:
                subsection = subsection_header.get_text(strip=True)
        return subsection

    def _get_element_weight(self, element: BeautifulSoup) -> int:
        """Get the weight of an element (for ordering)"""
        weight = element.get('data-weight', -1)
        return int(weight) if str(weight).isdigit() else 0

    def _is_index_page(self, element: BeautifulSoup) -> bool:
        """Check if the element links to an index/overview page"""
        text = element.get_text(strip=True).lower()
        href = element.get('href', '').lower()
        return any(word in text or word in href for word in [
            'introduction', 'overview', 'getting started', 'index'
        ]) or href.endswith('/')
