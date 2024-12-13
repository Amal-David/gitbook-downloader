from bs4 import BeautifulSoup
from typing import List, Optional
from .base_scraper import BaseScraper, PageContent

class SphinxScraper(BaseScraper):
    """Scraper for Sphinx documentation sites"""

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a Sphinx site"""
        # Look for Sphinx-specific elements
        sphinx_elements = soup.find_all(class_=lambda x: x and any(c in str(x) for c in [
            'sphinxsidebar',
            'sphinx-',
            'docutils',
            'document'
        ]))
        
        # Check for Sphinx meta tags
        meta_generator = soup.find('meta', {'name': 'generator', 'content': lambda x: x and 'sphinx' in x.lower()})
        
        return len(sphinx_elements) > 0 or meta_generator is not None

    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extract navigation elements from Sphinx page"""
        nav_elements = []
        
        # Try sidebar navigation
        sidebar = self.soup.find('div', class_='sphinxsidebar')
        if sidebar:
            nav_elements.append(sidebar)
        
        # Try local table of contents
        local_toc = self.soup.find('div', class_=['contents', 'local-toc'])
        if local_toc:
            nav_elements.append(local_toc)
        
        # Try navigation sidebars
        nav_sidebars = self.soup.find_all('div', class_=['nav-sidebar', 'toctree-wrapper'])
        nav_elements.extend(nav_sidebars)
        
        return nav_elements

    def extract_main_content(self) -> Optional[BeautifulSoup]:
        """Extract main content from Sphinx page"""
        # Try different Sphinx content containers
        content = self.soup.find('div', class_='body')  # Classic theme
        if not content:
            content = self.soup.find('div', class_='document')  # Basic theme
        if not content:
            content = self.soup.find('article', class_='bd-article')  # PyData theme
        if not content:
            content = self.soup.find('div', role='main')  # Generic
            
        return content

    def process_special_elements(self, content: BeautifulSoup) -> None:
        """Process Sphinx-specific elements"""
        if not content:
            return

        # Handle admonitions
        for admonition in content.find_all(class_='admonition'):
            title = admonition.find(class_='admonition-title')
            if title:
                # Convert to markdown blockquote with title
                title.string = f"**{title.get_text(strip=True)}**\n\n"

        # Handle viewcode links
        for viewcode in content.find_all(class_='viewcode-link'):
            viewcode.decompose()

        # Handle sphinx-copybutton
        for copy_button in content.find_all(class_='copybutton'):
            copy_button.decompose()

        # Handle code blocks
        for pre in content.find_all('pre'):
            code = pre.find('code')
            if code:
                # Get language from highlight class
                classes = pre.get('class', [])
                lang = ''
                for class_ in classes:
                    if class_.startswith('highlight-'):
                        lang = class_.replace('highlight-', '')
                        break
                if lang:
                    pre['data-lang'] = lang

    def extract_page_metadata(self, content: BeautifulSoup, url: str) -> PageContent:
        """Extract page metadata including title, order, section info"""
        # Try to get title
        title = ""
        h1 = content.find('h1')
        if h1:
            title = h1.get_text(strip=True)
        else:
            title_meta = self.soup.find('meta', {'property': 'og:title'}) or \
                        self.soup.find('title')
            if title_meta:
                title = title_meta.get_text(strip=True)

        # Try to get section info from breadcrumbs
        section = ""
        breadcrumbs = self.soup.find(['ul', 'div'], class_=['breadcrumbs', 'related'])
        if breadcrumbs:
            crumbs = breadcrumbs.find_all(['li', 'a'])
            if len(crumbs) > 1:
                section = crumbs[1].get_text(strip=True)

        # Get order from toctree
        order = 999999
        current_item = self.soup.find(class_=['current', 'active'])
        if current_item:
            siblings = current_item.find_previous_siblings(['li', 'div'])
            order = len(siblings)

        # Try to get weight from toctree
        weight = 0
        if current_item:
            weight_attr = current_item.get('data-weight', 0)
            try:
                weight = int(weight_attr)
            except (ValueError, TypeError):
                pass

        # Check if this is an index page
        is_index = any(x in url.lower() for x in ['index', 'readme', 'contents', 'getting-started'])

        return PageContent(
            url=url,
            title=title,
            content=str(content),
            order=order,
            section=section,
            weight=weight,
            is_index=is_index
        )
