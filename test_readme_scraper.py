import unittest
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from scrapers import ReadmeScraper, ScraperFactory
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@unittest.skip("Network-dependent tests skipped in this environment")
class TestDeepgramReadmeScraper(unittest.TestCase):
    def setUp(self):
        self.test_url = "https://developers.deepgram.com/docs/introduction"
        self.html_content = None
        asyncio.run(self.fetch_test_content())

    async def fetch_test_content(self):
        """Fetch actual content from Deepgram docs for testing"""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.test_url) as response:
                self.html_content = await response.text()
                self.soup = BeautifulSoup(self.html_content, 'html.parser')

    def test_can_handle_deepgram(self):
        """Test that ReadmeScraper correctly identifies Deepgram docs"""
        self.assertTrue(ReadmeScraper.can_handle(self.soup, "developers.deepgram.com"))

    def test_navigation_extraction(self):
        """Test navigation extraction from Deepgram docs"""
        scraper = ReadmeScraper(self.soup, self.test_url)
        nav_elements = scraper.extract_navigation_elements()
        self.assertGreater(len(nav_elements), 0, "Should find navigation elements")
        
        # Debug navigation elements
        logger.debug(f"Found {len(nav_elements)} navigation elements")
        for nav in nav_elements:
            logger.debug(f"Navigation element: {nav.name}, class: {nav.get('class', [])}")
            for a in nav.find_all('a', href=True):
                logger.debug(f"Link found: {a['href']}, text: {a.get_text(strip=True)}")
        
        # Extract and verify links
        links = scraper.extract_links(nav_elements, set())
        logger.debug(f"Extracted {len(links)} links")
        for link_data in links:
            logger.debug(f"Link data: {link_data}")
        
        self.assertGreater(len(links), 0, "Should find navigation links")
        
        # Verify link structure
        for link_data in links:
            self.assertIsInstance(link_data, tuple, "Link data should be a tuple")
            self.assertEqual(len(link_data), 2, "Link data should have 2 elements")
            link, metadata = link_data
            self.assertTrue(isinstance(link, str), "Link should be a string")
            self.assertTrue(isinstance(metadata, dict), "Metadata should be a dictionary")
            self.assertIn('title', metadata, "Metadata should contain title")
            self.assertTrue(link.startswith('https://'), "Links should be absolute URLs")

    def test_main_content_extraction(self):
        """Test main content extraction from Deepgram docs"""
        scraper = ReadmeScraper(self.soup, self.test_url)
        main_content = scraper.extract_main_content()
        self.assertIsNotNone(main_content, "Should find main content")
        
        # Debug main content
        logger.debug(f"Main content element: {main_content.name}, class: {main_content.get('class', [])}")
        
        # Verify content structure
        self.assertTrue(
            main_content.find('h1') or main_content.find('h2'),
            "Main content should contain headers"
        )

    def test_metadata_extraction(self):
        """Test metadata extraction from Deepgram docs"""
        scraper = ReadmeScraper(self.soup, self.test_url)
        main_content = scraper.extract_main_content()
        metadata = scraper.extract_page_metadata(main_content, self.test_url)
        
        # Debug metadata
        logger.debug(f"Extracted metadata: {metadata}")
        
        self.assertIsNotNone(metadata.title, "Should extract page title")
        self.assertIsInstance(metadata.order, int, "Order should be an integer")

if __name__ == '__main__':
    unittest.main(verbosity=2) 