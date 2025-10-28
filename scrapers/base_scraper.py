from bs4 import BeautifulSoup
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Tuple, Any
from urllib.parse import urljoin
from dataclasses import dataclass

@dataclass
class PageContent:
    """Represents a page's content with metadata for ordering"""
    url: str
    title: str
    content: str
    order: int  # Lower numbers appear first
    section: str = ""  # Group pages by section
    subsection: str = ""  # Further grouping
    weight: int = 0  # Some docs use weight for ordering
    is_index: bool = False  # True for index/overview pages

class BaseScraper(ABC):
    """Base class for documentation scrapers"""
    
    def __init__(self, soup: BeautifulSoup, base_url: str):
        self.soup = soup
        self.base_url = base_url
        self.pages: Dict[str, PageContent] = {}
        self.nav_structure: Dict[str, Any] = {}  # Stores the navigation hierarchy

    @classmethod
    @abstractmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this scraper can handle the given site"""
        pass

    @abstractmethod
    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extract navigation elements from the page"""
        pass

    @abstractmethod
    def extract_main_content_element(self, page_soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """Extract the main content element from the provided page soup"""
        pass

    def extract_main_content(self) -> Optional[BeautifulSoup]:
        """Extract the main content from the stored page soup"""
        return self.extract_main_content_element(self.soup)

    @abstractmethod
    def process_special_elements(self, content: BeautifulSoup) -> None:
        """Process any site-specific special elements"""
        pass

    @abstractmethod
    def extract_page_metadata(self, content: BeautifulSoup, url: str) -> PageContent:
        """Extract page metadata including title, order, section, etc."""
        pass

    def extract_links(self, nav_elements: List[BeautifulSoup], visited_urls: set) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract links and their metadata from navigation elements"""
        links = []
        for nav in nav_elements:
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
                        links.append((full_url, metadata))
        
        # Sort links by section, subsection, order, and weight
        return sorted(links, key=lambda x: (
            x[1]['section'],
            x[1]['subsection'],
            x[1]['order'],
            x[1]['weight']
        ))

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
        section_elem = element.find_parent(['nav', 'section', 'div'], class_=lambda x: x and (
            'section' in x.lower() or
            'category' in x.lower() or
            'group' in x.lower()
        ))
        if section_elem:
            heading = section_elem.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            if heading:
                return heading.get_text(strip=True)
            return section_elem.get('data-section', '')
        return ""

    def _get_parent_subsection(self, element: BeautifulSoup) -> str:
        """Get the parent subsection name"""
        subsection_elem = element.find_parent(['div', 'ul'], class_=lambda x: x and (
            'subsection' in x.lower() or
            'submenu' in x.lower() or
            'children' in x.lower()
        ))
        if subsection_elem:
            heading = subsection_elem.find(['h3', 'h4', 'h5', 'h6'])
            if heading:
                return heading.get_text(strip=True)
        return ""

    def _get_element_weight(self, element: BeautifulSoup) -> int:
        """Get the weight of an element (used by some doc systems for ordering)"""
        weight = element.get('data-weight', -1)
        if weight == -1:
            weight = element.get('weight', -1)
        return int(weight) if str(weight).isdigit() else 0

    def _is_index_page(self, element: BeautifulSoup) -> bool:
        """Check if this is an index/overview page"""
        href = element.get('href', '')
        text = element.get_text(strip=True).lower()
        return any([
            'index' in href.lower(),
            'overview' in href.lower(),
            'introduction' in href.lower(),
            'getting-started' in href.lower(),
            'index' in text,
            'overview' in text,
            'introduction' in text,
            'getting started' in text
        ])

    def clean_content(self, content: BeautifulSoup) -> BeautifulSoup:
        """Remove unnecessary elements from content"""
        if not content:
            return content
            
        # Remove navigation, header, footer elements
        for element in content.find_all(['nav', 'header', 'footer', 'aside']):
            element.decompose()
            
        # Remove scripts and styles
        for element in content.find_all(['script', 'style', 'iframe', 'noscript']):
            element.decompose()
            
        return content

    def build_navigation_structure(self) -> Dict[str, Any]:
        """Build a hierarchical navigation structure"""
        structure = {}
        for url, page in sorted(self.pages.items(), key=lambda x: (
            x[1].section,
            x[1].subsection,
            x[1].order,
            x[1].weight
        )):
            section = page.section or "Main"
            subsection = page.subsection
            
            if section not in structure:
                structure[section] = {"pages": [], "subsections": {}}
            
            if subsection:
                if subsection not in structure[section]["subsections"]:
                    structure[section]["subsections"][subsection] = []
                structure[section]["subsections"][subsection].append(page)
            else:
                structure[section]["pages"].append(page)
                
        return structure
