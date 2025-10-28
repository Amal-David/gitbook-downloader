from typing import Type, Optional
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from .base_scraper import BaseScraper
from .gitbook_scraper import GitbookScraper
from .docusaurus_scraper import DocusaurusScraper
from .readme_scraper import ReadmeScraper
from .mkdocs_scraper import MkDocsScraper
from .sphinx_scraper import SphinxScraper
from .mintlify_scraper import MintlifyScraper
from .scraper_factory import ScraperFactory

__all__ = [
    'BaseScraper',
    'GitbookScraper',
    'DocusaurusScraper',
    'ReadmeScraper',
    'MkDocsScraper',
    'SphinxScraper',
    'MintlifyScraper',
    'ScraperFactory'
]
