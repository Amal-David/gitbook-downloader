import re
import logging
from bs4 import BeautifulSoup
from typing import List, Optional, Tuple, Dict, Any
from urllib.parse import urljoin, urlparse
import markdownify

from .base_scraper import BaseScraper, PageContent

logger = logging.getLogger(__name__)

class MkDocsScraper(BaseScraper):
    """Scraper for MkDocs documentation sites"""

    def __init__(self, soup: BeautifulSoup, base_url: str):
        super().__init__(soup, base_url)

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is an MkDocs site."""
        meta_generator = soup.find('meta', attrs={'name': 'generator', 'content': re.compile(r'mkdocs', re.I)})
        if meta_generator:
            return True

        # Material for MkDocs theme indicators
        if soup.find('body', class_=lambda x: x and 'md-container' in x) or \
           soup.find('div', class_='md-sidebar') or \
           soup.find('header', class_='md-header'):
            return True
        
        # Read the Docs theme (often used with MkDocs)
        if soup.find('div', class_='wy-nav-content') or \
           soup.find('nav', class_='wy-nav-side'):
            return True
            
        # Generic MkDocs footer text (less reliable)
        footer = soup.find('footer')
        if footer and "mkdocs" in footer.get_text(strip=True).lower():
            return True
            
        return False

    def extract_navigation_links(self) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract navigation links from MkDocs site using self.soup (base page soup)."""
        nav_links_with_metadata: List[Tuple[str, Dict[str, Any]]] = []
        processed_urls: set[str] = set()
        order = 0

        # Material for MkDocs theme navigation
        material_nav_primary = self.soup.find('nav', class_=re.compile(r'md-nav--primary'))
        nav_container = material_nav_primary
        if not nav_container: # Fallback for other MkDocs themes or structures
            # Read the Docs theme navigation
            nav_container = self.soup.find('nav', class_='wy-nav-side')
            if not nav_container:
                nav_container = self.soup.find('div', class_=re.compile(r'(md-sidebar|toctree-wrapper|nav-sidebar)'))


        if not nav_container:
            logger.warning("Could not find a primary navigation container for MkDocs scraper.")
            return []

        for link_tag in nav_container.find_all('a', href=True):
            href = link_tag['href']
            full_url = urljoin(self.base_url, href)
            
            parsed_full_url = urlparse(full_url)
            if parsed_full_url.scheme not in ['http', 'https']:
                continue

            url_to_check = parsed_full_url._replace(fragment="").geturl()
            if url_to_check in processed_urls or not url_to_check.startswith(self.base_url.split('//')[0]):
                if not url_to_check.startswith(self.base_url) and not href.startswith('/'):
                    continue
            
            link_text = link_tag.get_text(strip=True) or "Untitled Page"
            
            # Try to determine section from parent list items or headers
            section_name = ""
            # For Material theme, active trail might give section
            active_li = link_tag.find_parent('li', class_='md-nav__item--active')
            if active_li:
                # Find previous sibling that might be a section header or a parent nav item
                parent_nav_level = active_li.find_parent('ul', class_='md-nav__list')
                if parent_nav_level and parent_nav_level.parent.name == 'li':
                    section_title_tag = parent_nav_level.parent.find('a', class_='md-nav__link') # Or other title element
                    if section_title_tag:
                        section_name = section_title_tag.get_text(strip=True)

            metadata = {
                'title': link_text,
                'order': order,
                'section': section_name,
            }
            nav_links_with_metadata.append((full_url, metadata))
            processed_urls.add(url_to_check)
            order += 1
            
        logger.info(f"Extracted {len(nav_links_with_metadata)} navigation links from MkDocs site.")
        return nav_links_with_metadata

    def extract_main_content_element(self, page_soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """Extracts the main content block from an MkDocs page's soup."""
        # Material for MkDocs theme
        main_content = page_soup.find('main', class_='md-main')
        if main_content:
            article = main_content.find('article', class_='md-content__inner') # Prefer more specific
            if article: return article
            content_div = main_content.find('div', class_='md-content')
            if content_div: return content_div # Fallback within main
            return main_content # Return main itself if nothing more specific found

        # Read the Docs theme (often used with MkDocs)
        main_content = page_soup.find('section', attrs={'role': 'main'})
        if main_content: return main_content
        main_content = page_soup.find('div', class_='document', attrs={'role': 'main'}) # Older RTD theme
        if main_content: return main_content
        
        # Generic fallback
        main_content = page_soup.find('main')
        if main_content: return main_content

        logger.warning("Could not find a distinct main content element for MkDocs. Falling back to body.")
        return page_soup.find('body')

    def process_special_elements(self, main_content_element: BeautifulSoup) -> None:
        """Processes MkDocs-specific elements within the main_content_element."""
        if not main_content_element:
            return

        # Remove "Edit this page" or "View source" links (common in Material and RTD themes)
        for edit_link in main_content_element.find_all('a', class_=['md-content__button', 'viewcode-link']):
            edit_link.decompose()
        for edit_link_container in main_content_element.find_all('div', class_='md-source-file'): # Material theme
            edit_link_container.decompose()


        # Admonitions: Markdownify usually handles them well if they are simple <div class="admonition ..."><p class="admonition-title">...</p>...</div>
        # For Material theme, they are usually fine. We can add more specific handling if needed.
        # Example: Ensure title is bold for markdownify
        for admonition in main_content_element.find_all('div', class_='admonition'):
            title_tag = admonition.find(['p', 'div'], class_='admonition-title')
            if title_tag and title_tag.string: # Check if string exists to avoid errors
                # Check if already bold or contains other tags
                if not title_tag.find('strong'):
                    title_tag.string = f"**{title_tag.get_text(strip=True)}**" # Make title bold

        # Code blocks: MkDocs (especially with Pygments) uses <pre><code class="language-xxx">.
        # Markdownify's default code_language_callback usually handles this.
        # If there are complex structures like custom copy buttons inside <pre>, they might need removal.
        for pre_tag in main_content_element.find_all('pre'):
            for button in pre_tag.find_all('button', class_=re.compile(r'copy|clip', re.I)):
                button.decompose()
            # Some themes might wrap code blocks in extra divs for styling, these are usually fine.

        # Remove permalinks if they are part of the header text and cause issues
        for permalink in main_content_element.find_all('a', class_='headerlink'):
            permalink.decompose()


    def extract_page_data(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Extracts title, cleans content, converts to Markdown, and returns a PageContent object."""
        
        title_text = ""
        main_content_for_title = self.extract_main_content_element(page_soup)
        if main_content_for_title:
            h1 = main_content_for_title.find('h1')
            if h1:
                title_text = h1.get_text(strip=True)
        
        if not title_text:
            title_tag = page_soup.find('title')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                # Clean title: "Page Title - Site Name" or "Page Title | Site Name"
                title_text = re.split(r'\s*[-\|]\s*', title_text)[0].strip()
        
        if not title_text:
            path_part = urlparse(url).path.split('/')[-1]
            title_text = path_part.replace('-', ' ').replace('_', ' ').title() or "Untitled Page"

        main_content_element = self.extract_main_content_element(page_soup)

        if not main_content_element:
            logger.warning(f"No main content element found for MkDocs page {url}. Content will be empty.")
            return PageContent(url=url, title=title_text, content="", order=0)

        # Generic cleaning + MkDocs-specific cleaning
        # self.clean_content(main_content_element) # Apply generic clean_content from BaseScraper
        self.process_special_elements(main_content_element) # Apply MkDocs specific cleaning

        html_string = str(main_content_element)
        try:
            md = markdownify.markdownify(
                html_string, 
                heading_style="atx",
                bullets='-',
                code_language_callback=lambda el: el.get('class')[0].replace('language-', '') if el.get('class') and el.get('class')[0].startswith('language-') else None
            ).strip()
        except Exception as e:
            logger.error(f"Error during markdownify conversion for MkDocs page {url}: {e}")
            md = f"Error converting content to Markdown: {e}"

        order = 0 # Placeholder
        
        return PageContent(
            url=url,
            title=title_text,
            content=md,
            order=order,
            section="", 
            subsection="",
            is_index= 'index' in url.lower() or url.endswith('/') or (title_text.lower() in ['introduction', 'overview', 'home', 'getting started'])
        )

    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extracts potential MkDocs navigation elements from self.soup."""
        nav_elements = []
        material_nav = self.soup.find('nav', class_=re.compile(r'md-nav--primary'))
        if material_nav: nav_elements.append(material_nav)
        
        rtd_nav = self.soup.find('nav', class_='wy-nav-side')
        if rtd_nav and rtd_nav not in nav_elements: nav_elements.append(rtd_nav)

        if not nav_elements:
            nav_elements.extend(self.soup.find_all(['nav', 'div'], class_=re.compile(r'(md-sidebar|toctree-wrapper|nav-sidebar|wy-menu-vertical)')))
        return nav_elements
        
    def extract_page_metadata(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Required by BaseScraper. Delegates to extract_page_data for MkDocs."""
        logger.debug(f"MkDocsScraper.extract_page_metadata called for {url}, delegating to extract_page_data.")
        return self.extract_page_data(page_soup, url)
