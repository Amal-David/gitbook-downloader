from bs4 import BeautifulSoup
from typing import List, Optional
from .base_scraper import BaseScraper, PageContent

class GitbookScraper(BaseScraper):
    """Scraper for GitBook documentation sites"""

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a GitBook site"""
        return bool(
            # New GitBook structure detection
            soup.find('div', {'class': lambda x: x and 'scroll-pt-' in str(x)}) or
            soup.find('div', {'class': lambda x: x and 'headerLinks_' in str(x)}) or
            # Legacy GitBook structure detection
            soup.find('div', {'data-testid': 'page.contentEditor'}) or
            soup.find('div', class_=lambda x: x and 'reset-3c756112--content-764c9ca' in x) or
            # Domain-based detection
            'gitbook.io' in domain
        )

    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extract GitBook navigation elements"""
        nav_elements = []
        
        # Try to find navigation in new GitBook structure
        nav = self.soup.find('aside', {'class': lambda x: x and 'flex' in str(x)})
        if nav:
            nav_elements.append(nav)
            return nav_elements
            
        # Try legacy navigation structures
        nav_elements.extend(self.soup.find_all(
            ['nav', 'aside', 'div'],
            class_=lambda x: x and (
                'navigation' in x.lower() or
                'sidebar' in x.lower() or
                'menu' in x.lower()
            )
        ))
        
        return nav_elements

    def extract_main_content(self) -> Optional[BeautifulSoup]:
        """Extract GitBook main content"""
        # Try new GitBook structure first
        main_content = self.soup.find(
            'main',
            {'class': lambda x: x and 'flex-1' in str(x)}
        )
        
        if not main_content:
            # Try legacy content structures
            main_content = self.soup.find(
                ['main', 'article', 'div'],
                class_=lambda x: x and ('content' in x.lower() or 'main' in x.lower())
            )
        
        if not main_content:
            # Fallback to body
            main_content = self.soup.find('body')
            
        return main_content

    def process_special_elements(self, content: BeautifulSoup) -> None:
        """Process GitBook-specific elements"""
        # Remove navigation elements that might be included
        for nav in content.find_all(['nav', 'aside']):
            nav.decompose()
            
        # Remove header elements
        for header in content.find_all('header'):
            header.decompose()
            
        # Remove script tags
        for script in content.find_all('script'):
            script.decompose()

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
        
        if nav:
            # Try to find the current page in navigation
            current_link = nav[0].find('a', href=lambda x: x and url.endswith(x))
            if current_link:
                # Look for parent sections
                parent = current_link.find_parent(['div', 'section', 'nav'])
                if parent:
                    section_header = parent.find_previous(['h2', 'h3'])
                    if section_header:
                        section = section_header.get_text().strip()
                
                # Get order based on position in navigation
                siblings = nav[0].find_all('a')
                order = siblings.index(current_link) if current_link in siblings else 0
        
        # Create PageContent object
        return PageContent(
            url=url,
            title=title,
            content=content.get_text(separator='\n\n').strip(),
            order=order,
            section=section,
            subsection=subsection,
            is_index='index' in url.lower() or url.endswith('/')
        )
