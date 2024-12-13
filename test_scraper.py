import unittest
from bs4 import BeautifulSoup
from scrapers import ScraperFactory, GitbookScraper
from gitbook_downloader import GitbookDownloader

class TestGitbookScraper(unittest.TestCase):
    def setUp(self):
        self.test_url = "https://gitbook.goodentry.io"
        self.test_html = """
        <html>
            <body>
                <div data-testid="page.contentEditor">
                    <nav class="navigation">
                        <a href="/page1">Link 1</a>
                        <a href="/page2">Link 2</a>
                    </nav>
                    <main class="content">
                        <h1>Test Title</h1>
                        <div>Main content</div>
                    </main>
                </div>
            </body>
        </html>
        """
        self.soup = BeautifulSoup(self.test_html, 'html.parser')

    def test_scraper_creation(self):
        """Test that ScraperFactory creates a GitbookScraper correctly"""
        scraper = ScraperFactory.create_scraper(self.soup, self.test_url)
        self.assertIsInstance(scraper, GitbookScraper)

    def test_gitbook_scraper_can_handle(self):
        """Test that GitbookScraper correctly identifies GitBook sites"""
        self.assertTrue(GitbookScraper.can_handle(self.soup, "gitbook.goodentry.io"))

    def test_gitbook_scraper_navigation(self):
        """Test that GitbookScraper extracts navigation correctly"""
        scraper = GitbookScraper(self.soup, self.test_url)
        nav_elements = scraper.extract_navigation_elements()
        self.assertEqual(len(nav_elements), 1)
        self.assertEqual(len(nav_elements[0].find_all('a')), 2)

    def test_gitbook_scraper_content(self):
        """Test that GitbookScraper extracts content correctly"""
        scraper = GitbookScraper(self.soup, self.test_url)
        content = scraper.extract_main_content()
        self.assertIsNotNone(content)
        self.assertIn("Main content", content.get_text())
        self.assertIn("Test Title", content.get_text())

    def test_gitbook_downloader_initialization(self):
        """Test GitbookDownloader initialization"""
        downloader = GitbookDownloader(self.test_url)
        self.assertEqual(downloader.base_url, self.test_url)
        self.assertEqual(downloader.domain, "gitbook.goodentry.io")

    def test_gitbook_downloader_scraper_creation(self):
        """Test scraper creation in GitbookDownloader"""
        downloader = GitbookDownloader(self.test_url)
        # Create BeautifulSoup object
        soup = BeautifulSoup(self.test_html, 'html.parser')
        # Create appropriate scraper
        scraper = ScraperFactory.create_scraper(soup, downloader.base_url)
        self.assertIsInstance(scraper, GitbookScraper)

if __name__ == '__main__':
    unittest.main(verbosity=2)
