from bs4 import BeautifulSoup
from typing import Optional
from .base_scraper import BaseScraper
from .gitbook_scraper import GitbookScraper
from .docusaurus_scraper import DocusaurusScraper
from .readme_scraper import ReadmeScraper
from .mkdocs_scraper import MkDocsScraper
from .sphinx_scraper import SphinxScraper
from urllib.parse import urlparse

class ScraperFactory:
    """Factory for creating the appropriate scraper based on the site type"""
    
    _scrapers = [
        GitbookScraper,
        DocusaurusScraper,
        ReadmeScraper,
        MkDocsScraper,
        SphinxScraper
    ]
    
    @classmethod
    def create_scraper(cls, soup: BeautifulSoup, url: str) -> Optional[BaseScraper]:
        """Create appropriate scraper for the given site"""
        domain = urlparse(url).netloc
        
        for scraper_class in cls._scrapers:
            if scraper_class.can_handle(soup, domain):
                return scraper_class(soup, url)
        
        # Default to GitBook if no other scraper matches
        return GitbookScraper(soup, url)

    @classmethod
    def get_supported_platforms(cls) -> list[str]:
        """Get list of supported documentation platforms"""
        return [
            scraper.__name__.replace('Scraper', '')
            for scraper in cls._scrapers
        ]
