from typing import Type, Optional
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from .base_scraper import BaseScraper
from .gitbook_scraper import GitbookScraper
from .docusaurus_scraper import DocusaurusScraper
from .readme_scraper import ReadmeScraper
from .mkdocs_scraper import MkDocsScraper
from .sphinx_scraper import SphinxScraper
from .scraper_factory import ScraperFactory

__all__ = [
    'BaseScraper',
    'GitbookScraper',
    'DocusaurusScraper',
    'ReadmeScraper',
    'MkDocsScraper',
    'SphinxScraper',
    'ScraperFactory'
]

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
        
        return None

    @classmethod
    def register_scraper(cls, scraper_class: Type[BaseScraper]) -> None:
        """Register a new scraper class"""
        if scraper_class not in cls._scrapers:
            cls._scrapers.append(scraper_class)

    @classmethod
    def get_supported_platforms(cls) -> list[str]:
        """Get list of supported documentation platforms"""
        return [
            scraper.__name__.replace('Scraper', '')
            for scraper in cls._scrapers
        ]
