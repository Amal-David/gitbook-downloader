import re
import logging
from bs4 import BeautifulSoup
from typing import List, Optional, Tuple, Dict, Any
from urllib.parse import urljoin, urlparse
import markdownify

from .base_scraper import BaseScraper, PageContent

logger = logging.getLogger(__name__)

class DocusaurusScraper(BaseScraper):
    """Scraper for Docusaurus documentation sites"""

    def __init__(self, soup: BeautifulSoup, base_url: str):
        super().__init__(soup, base_url)

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a Docusaurus site more accurately."""
        # Check for Docusaurus specific IDs, attributes, or class name patterns
        if soup.find(id='__docusaurus'):
            return True
        if soup.find('html', attrs={'data-theme': 'docusaurus'}): # Docusaurus v3 might use this
            return True
        if soup.find('html', class_=lambda x: x and 'plugin-pages' in x): # Docusaurus v2
            return True
        if soup.find('nav', class_=lambda x: x and 'navbar--fixed-top' in x and 'navbar' in x): # Common navbar
             # Further check for Docusaurus specific sidebar/main content structure
            if soup.find('div', class_=lambda x: x and ('main-wrapper' in x or 'docPage_' in x)): # main-wrapper for v2, docPage for v3
                return True
        # Meta generator tag (less reliable as it can be removed)
        meta_generator = soup.find('meta', attrs={'name': 'generator', 'content': re.compile(r'Docusaurus', re.I)})
        if meta_generator:
            return True
        
        # Fallback to some of the older checks if necessary, but prioritize newer indicators
        return bool(
            soup.find('div', class_='docusaurus-highlight-code-line') or # Common in Docusaurus code blocks
            soup.find('div', class_=re.compile(r"theme-doc-sidebar-container", re.I)) or
            soup.find('main', role="main") # Docusaurus often uses <main role="main">
        )

    def extract_navigation_links(self) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract navigation links from Docusaurus site using self.soup (base page soup)."""
        nav_links_with_metadata: List[Tuple[str, Dict[str, Any]]] = []
        processed_urls: set[str] = set()
        
        # Common Docusaurus navigation containers:
        # - <aside class="theme-doc-sidebar-container ...">
        # - <nav aria-label="Docs sidebar" ...>
        # - <div class="navbar__items navbar__items--left"> (for top nav, less common for full ToC)
        # - Older versions might use different structures.
        
        # Try primary sidebar first
        nav_container = self.soup.find('aside', class_=re.compile(r'theme-doc-sidebar-container', re.I))
        if not nav_container:
            nav_container = self.soup.find('nav', attrs={'aria-label': re.compile(r'Docs sidebar', re.I)})
        
        if not nav_container:
            # Fallback to a more generic menu if specific sidebar not found
            nav_container = self.soup.find('div', class_=re.compile(r'(menu|sidebar|toc|nav)', re.I))
            logger.warning("Primary Docusaurus navigation container not found, trying generic one.")

        if not nav_container:
            logger.error("Could not find any navigation container for Docusaurus scraper.")
            return []

        order = 0
        # Links are typically within <a> tags, often nested in lists <li> or divs with menu item classes
        for link_tag in nav_container.find_all('a', href=True):
            href = link_tag['href']
            
            # Some Docusaurus links might be fully qualified if they link to sub-sites, handle carefully
            full_url = urljoin(self.base_url, href)
            
            parsed_full_url = urlparse(full_url)
            if parsed_full_url.scheme not in ['http', 'https']:
                continue

            # Avoid fragments and already processed URLs
            url_to_check = parsed_full_url._replace(fragment="").geturl()
            if url_to_check in processed_urls:
                continue
            
            link_text = link_tag.get_text(strip=True) or "Untitled Page"
            
            # Docusaurus specific: check for active link class to identify current section
            # section = ""
            # if link_tag.find_parent('li', class_=re.compile(r"menu__list-item--active", re.I)):
            #    section_element = link_tag.find_parent() # ... more logic to find section title ...
            
            metadata = {
                'title': link_text,
                'order': order,
                # 'section': section, # Placeholder for now
            }
            nav_links_with_metadata.append((full_url, metadata))
            processed_urls.add(url_to_check)
            order += 1
            
        logger.info(f"Extracted {len(nav_links_with_metadata)} navigation links from Docusaurus site.")
        return nav_links_with_metadata

    def extract_main_content_element(self, page_soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """Extracts the main content block from a Docusaurus page's soup."""
        # Docusaurus v2/v3 common main content containers:
        # <article> (often with class "theme-doc-markdown markdown")
        # <main role="main"> then find inner content div
        # <div class="docItemContainer_...">
        # <div class="markdown"> (might be too generic, but a fallback)
        
        main_content = page_soup.find('article', class_=re.compile(r'theme-doc-markdown|markdown', re.I))
        if main_content: return main_content

        main_content = page_soup.find('main', attrs={'role': 'main'})
        if main_content:
            # Often there's an inner div that's the true content root
            inner_div = main_content.find('div', class_=re.compile(r'(docItemContainer_|theme-doc-markdown|markdown)'))
            if inner_div: return inner_div
            return main_content # Return main itself if no more specific inner div

        main_content = page_soup.find('div', class_=re.compile(r'docItemContainer_'))
        if main_content: return main_content
        
        # Fallback for older or very custom Docusaurus sites
        main_content = page_soup.find('div', class_='main-wrapper') # Docusaurus v1/v2 wrapper
        if main_content and main_content.find('article'): # Check if it contains an article
            return main_content.find('article')
        if main_content: return main_content # If main-wrapper has no article, return it as is

        logger.warning("Could not find a distinct main content element for Docusaurus. Falling back to body.")
        return page_soup.find('body')

    def process_special_elements(self, main_content_element: BeautifulSoup) -> None:
        """Processes Docusaurus-specific elements within the main_content_element."""
        if not main_content_element:
            return

        # Remove "Edit this page" links
        for edit_link in main_content_element.find_all('a', class_=re.compile(r'theme-edit-this-page', re.I)):
            edit_link.decompose()

        # Remove Docusaurus specific footer navigation (prev/next buttons) if they are part of main_content_element
        for footer_nav in main_content_element.find_all('nav', class_=re.compile(r'pagination-nav', re.I)):
            footer_nav.decompose()
        
        # Remove table of contents if it's embedded within the main content and duplicated
        for toc_embedded in main_content_element.find_all('div', class_=re.compile(r'table-of-contents', re.I)):
            # Be careful not to remove the main navigation sidebar's ToC if it was misidentified as main_content_element
            if toc_embedded.find_parent('main') or toc_embedded.find_parent('article'): # Ensure it's in main body
                 # More specific check: if it's a short ToC for the page, not the global one
                if len(toc_embedded.find_all('a')) < 10: # Heuristic: page ToCs are usually shorter
                    logger.debug("Decomposing embedded page table of contents.")
                    toc_embedded.decompose()


        # Remove version badges/info boxes if not desired
        for version_info in main_content_element.find_all('div', class_=re.compile(r'theme-doc-version-badge|alert--info')):
            # Check if it's a prominent banner vs small notice. Decompose small notices.
            if 'alert--info' in version_info.get('class', []) and len(version_info.get_text(strip=True)) < 100 :
                 version_info.decompose()


    def extract_page_data(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Extracts title, cleans content, converts to Markdown, and returns a PageContent object."""
        
        # 1. Extract Title
        title_text = ""
        main_content_for_title = self.extract_main_content_element(page_soup) # Use content element for H1
        if main_content_for_title:
            h1 = main_content_for_title.find('h1')
            if h1:
                title_text = h1.get_text(strip=True)
        
        if not title_text:
            title_tag = page_soup.find('title')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                # Docusaurus titles often include site name, try to remove it
                parts = re.split(r'\s*\|\s*', title_text)
                if len(parts) > 1 and parts[-1].lower() != urlparse(self.base_url).netloc.lower(): # If last part is not domain
                    title_text = parts[0] # Assume first part is page title
        
        if not title_text: # Fallback title
            path_part = urlparse(url).path.split('/')[-1]
            title_text = path_part.replace('-', ' ').replace('_', ' ').title() or "Untitled Page"

        # 2. Get Main Content Element
        main_content_element = self.extract_main_content_element(page_soup)

        if not main_content_element:
            logger.warning(f"No main content element found for Docusaurus page {url}. Content will be empty.")
            return PageContent(url=url, title=title_text, content="", order=0)

        # 3. Clean the main content element
        # First, generic cleaning (removes nav, header, footer, script, style, etc. if they are *inside* main_content_element)
        # Note: BaseScraper.clean_content is designed to clean the *whole* soup usually.
        # Here, we apply it to the identified main_content_element.
        # This might be too aggressive if main_content_element is high up.
        # A more targeted cleaning in process_special_elements is often better.
        
        # Let's rely more on process_special_elements and careful selection of main_content_element
        # self.clean_content(main_content_element) # Use with caution or refine BaseScraper.clean_content
        
        # Docusaurus-specific cleaning
        self.process_special_elements(main_content_element)


        # 4. Convert cleaned HTML content to Markdown
        html_string = str(main_content_element)
        try:
            md = markdownify.markdownify(
                html_string, 
                heading_style="atx",
                bullets='-',
                code_language_callback=lambda el: el.get('class', [None])[-1].replace('language-', '') if el.get('class') and el.get('class')[-1].startswith('language-') else None,
                strip=['a'], # Example: strip 'a' tags if they are problematic and not handled by other means
                convert=['div', 'figure'] # Convert divs and figures if they often contain meaningful text
            ).strip()
        except Exception as e:
            logger.error(f"Error during markdownify conversion for Docusaurus page {url}: {e}")
            md = f"Error converting content to Markdown: {e}"

        # 5. Populate PageContent
        # Order might come from nav_links_metadata if passed through or stored
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

    # This method is required by BaseScraper but DocumentationDownloader calls extract_navigation_links directly.
    # Provide a basic implementation or adapt from extract_navigation_links if it's simple.
    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extracts potential Docusaurus navigation <aside> or <nav> elements from self.soup."""
        nav_elements = []
        # Try primary sidebar first
        sidebar = self.soup.find('aside', class_=re.compile(r'theme-doc-sidebar-container', re.I))
        if sidebar:
            nav_elements.append(sidebar)
        
        navbar = self.soup.find('nav', class_=re.compile(r'navbar', re.I))
        if navbar:
            nav_elements.append(navbar)
            
        if not nav_elements:
            # Fallback: find common Docusaurus navigation structures
            nav_elements.extend(self.soup.find_all(['nav', 'div'], class_=lambda x: x and any(
                keyword in x.lower() for keyword in ['menu', 'sidebar', 'toc', 'navbar'])
            ))
        return nav_elements
        
    # This method is required by BaseScraper.
    # DocumentationDownloader calls extract_page_data directly for each page.
    # This implementation can delegate to extract_page_data.
    def extract_page_metadata(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """
        Required by BaseScraper. Delegates to extract_page_data for Docusaurus.
        """
        logger.debug(f"DocusaurusScraper.extract_page_metadata called for {url}, delegating to extract_page_data.")
        return self.extract_page_data(page_soup, url)
