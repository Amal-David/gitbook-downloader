from bs4 import BeautifulSoup
from typing import List, Optional
from .base_scraper import BaseScraper, PageContent

class MkDocsScraper(BaseScraper):
    """Scraper for MkDocs documentation sites"""

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a MkDocs site"""
        # Look for common MkDocs elements and meta tags
        meta_generator = soup.find('meta', {'name': 'generator', 'content': lambda x: x and 'mkdocs' in x.lower()})
        if meta_generator:
            return True

        # Check for Material theme elements
        material_theme = soup.find('body', class_=lambda x: x and 'md-' in x)
        if material_theme:
            return True

        # Check for common MkDocs classes
        mkdocs_elements = soup.find_all(class_=lambda x: x and any(c in str(x) for c in ['md-nav', 'md-main', 'md-content']))
        return len(mkdocs_elements) > 0

    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extract navigation elements from MkDocs page"""
        nav_elements = []
        
        # Try Material theme navigation
        material_nav = self.soup.find('nav', class_='md-nav')
        if material_nav:
            nav_elements.append(material_nav)
            return nav_elements

        # Try default MkDocs navigation
        default_nav = self.soup.find('nav', class_=['md-navigation', 'navbar'])
        if default_nav:
            nav_elements.append(default_nav)

        # Try sidebar navigation
        sidebar = self.soup.find(['div', 'nav'], class_=['md-sidebar', 'md-sidebar--primary'])
        if sidebar:
            nav_elements.append(sidebar)

        return nav_elements

    def extract_main_content(self) -> Optional[BeautifulSoup]:
        """Extract main content from MkDocs page"""
        # Try Material theme content
        content = self.soup.find('article', class_='md-content__inner')
        if not content:
            content = self.soup.find('main', class_='md-main__inner')
        if not content:
            content = self.soup.find('div', class_='md-content')
        
        return content

    def process_special_elements(self, content: BeautifulSoup) -> None:
        """Process MkDocs-specific elements"""
        if not content:
            return

        # Handle code blocks
        for pre in content.find_all('pre'):
            code = pre.find('code')
            if code:
                lang = ''
                for class_ in code.get('class', []):
                    if class_.startswith('language-'):
                        lang = class_.replace('language-', '')
                        break
                if lang:
                    pre['data-lang'] = lang

        # Handle admonitions (Material theme)
        for admonition in content.find_all(class_='admonition'):
            title = admonition.find(class_='admonition-title')
            if title:
                # Convert to markdown blockquote with title
                title.string = f"**{title.get_text(strip=True)}**\n\n"

    def extract_page_metadata(self, content: BeautifulSoup, url: str) -> PageContent:
        """Extract page metadata including title, order, section info"""
        # Try to get title
        title = ""
        h1 = content.find('h1')
        if h1:
            title = h1.get_text(strip=True)
        else:
            title_meta = self.soup.find('meta', {'property': 'og:title'}) or \
                        self.soup.find('meta', {'name': 'title'})
            if title_meta:
                title = title_meta['content']

        # Try to get section info
        section = ""
        nav_item = self.soup.find('li', class_='md-nav__item--active')
        if nav_item:
            parent_section = nav_item.find_parent('li', class_='md-nav__item--nested')
            if parent_section:
                section_label = parent_section.find(class_='md-nav__link')
                if section_label:
                    section = section_label.get_text(strip=True)

        # Get order from nav position
        order = 999999
        if nav_item:
            siblings = nav_item.find_previous_siblings('li')
            order = len(siblings)

        # Check if this is an index page
        is_index = any(x in url.lower() for x in ['index', 'readme', 'getting-started', 'introduction'])

        return PageContent(
            url=url,
            title=title,
            content=str(content),
            order=order,
            section=section,
            is_index=is_index
        )
