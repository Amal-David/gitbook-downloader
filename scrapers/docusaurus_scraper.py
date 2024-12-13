from bs4 import BeautifulSoup
from typing import List, Optional
from .base_scraper import BaseScraper

class DocusaurusScraper(BaseScraper):
    """Scraper for Docusaurus documentation sites"""

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a Docusaurus site"""
        return bool(
            soup.find('div', class_='docusaurus-highlight-code-line') or
            soup.find('nav', class_='navbar navbar--fixed-top') or
            soup.find('div', class_='main-wrapper')
        )

    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extract Docusaurus navigation elements"""
        return self.soup.find_all(
            ['nav', 'div'],
            class_=lambda x: x and (
                'menu' in x.lower() or
                'navbar' in x.lower() or
                'table-of-contents' in x.lower() or
                'doc-sidebar' in x.lower()
            )
        )

    def extract_main_content(self) -> Optional[BeautifulSoup]:
        """Extract Docusaurus main content"""
        main_content = self.soup.find('article', class_=lambda x: x and 'docusaurus-doc-content' in x)
        if not main_content:
            main_content = self.soup.find('main', class_=lambda x: x and 'container' in x)
            
        if not main_content:
            main_content = self.soup.find('body')
            
        return main_content

    def process_special_elements(self, content: BeautifulSoup) -> None:
        """Process Docusaurus-specific elements"""
        # Currently no special processing needed for Docusaurus
        pass
