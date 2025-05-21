import re
import logging
from bs4 import BeautifulSoup
from typing import List, Optional, Tuple, Dict, Any
from urllib.parse import urljoin, urlparse
import markdownify

from .base_scraper import BaseScraper, PageContent

logger = logging.getLogger(__name__)

class SphinxScraper(BaseScraper):
    """Scraper for Sphinx documentation sites"""

    def __init__(self, soup: BeautifulSoup, base_url: str):
        super().__init__(soup, base_url)

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a Sphinx site."""
        meta_generator = soup.find('meta', attrs={'name': 'generator', 'content': re.compile(r'sphinx', re.I)})
        if meta_generator:
            return True
        
        if soup.find('div', class_='sphinxsidebar') or \
           soup.find('div', class_='bodywrapper') or \
           soup.find('div', class_='document'): # Common structural elements
            return True

        # Check for Sphinx static files
        for script_tag in soup.find_all('script', src=True):
            if '_static/documentation_options.js' in script_tag['src'] or \
               '_static/sphinx_highlight.js' in script_tag['src']:
                return True
        
        footer = soup.find('footer')
        if footer and "sphinx" in footer.get_text(strip=True).lower():
            return True
            
        return False

    def extract_navigation_links(self) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract navigation links from Sphinx site using self.soup (base page soup)."""
        nav_links_with_metadata: List[Tuple[str, Dict[str, Any]]] = []
        processed_urls: set[str] = set()
        order = 0
        
        # Common navigation areas in Sphinx:
        # 1. Sidebar with toctree: div.sphinxsidebar, nav[aria-label="main navigation"], div.toctree-wrapper
        # 2. Some themes might have top navigation bars as well.
        
        nav_containers = []
        # Primary sidebar (classic, alabaster, etc.)
        sidebar_nav = self.soup.find('div', class_='sphinxsidebar')
        if sidebar_nav: nav_containers.append(sidebar_nav)
        
        # HTML5 theme nav (nav[aria-label="main navigation"])
        main_nav = self.soup.find('nav', attrs={'aria-label': re.compile(r'main navigation|global navigation', re.I)})
        if main_nav and main_nav not in nav_containers: nav_containers.append(main_nav)

        # PyData Sphinx Theme, Furo, etc. often use a more modern nav structure
        modern_nav = self.soup.find('nav', class_=re.compile(r'(bd-links__nav|sidebar-drawer__content|sd-sidebar-ناطق)', re.I)) # sd-sidebar-ناطق for Furo's off-canvas
        if modern_nav and modern_nav not in nav_containers: nav_containers.append(modern_nav)


        if not nav_containers:
            logger.warning("Could not find a primary navigation container for Sphinx scraper. Checking generic toctree-wrapper.")
            toctree_fallback = self.soup.find_all('div', class_='toctree-wrapper')
            if toctree_fallback: nav_containers.extend(toctree_fallback)

        if not nav_containers:
            logger.error("No navigation containers found for Sphinx scraper.")
            return []

        for nav_container in nav_containers:
            # Process links, trying to determine sections from toctree structure
            current_section_title = ""
            for element in nav_container.find_all(['p', 'caption', 'a', 'li']): # p.caption is often a section title
                if element.name in ['p', 'caption'] and 'caption' in element.get('class', []):
                    current_section_title = element.get_text(strip=True)
                    continue

                if element.name == 'a' and element.get('href'):
                    link_tag = element
                elif element.name == 'li': # if it's a list item, find the first direct 'a' child
                    link_tag = element.find('a', href=True, recursive=False)
                    if not link_tag and element.find_parent('li', class_=re.compile(r"toctree-l\d", re.I)): # Check parent if nested
                        link_tag = element.find('a', href=True) # Deeper search if in toctree
                else:
                    continue
                
                if not link_tag: continue

                href = link_tag['href']
                full_url = urljoin(self.base_url, href)
                
                parsed_full_url = urlparse(full_url)
                if parsed_full_url.scheme not in ['http', 'https']:
                    continue

                url_to_check = parsed_full_url._replace(fragment="").geturl()
                if url_to_check in processed_urls or not url_to_check.startswith(self.base_url.split('//')[0]):
                     if not url_to_check.startswith(self.base_url) and not href.startswith('/'): # Allow relative
                        continue
                
                link_text = link_tag.get_text(strip=True) or "Untitled Page"
                
                # Try to determine hierarchy/section based on toctree classes (toctree-l1, toctree-l2, etc.)
                section_from_toctree = current_section_title
                parent_li = link_tag.find_parent('li', class_=re.compile(r"toctree-l\d", re.I))
                if parent_li:
                    # Try to find a preceding caption or header for this section if current_section_title is not specific enough
                    # This is complex as structure varies. For now, use current_section_title or derive from parent toctree items.
                    pass


                metadata = {
                    'title': link_text,
                    'order': order,
                    'section': section_from_toctree,
                }
                nav_links_with_metadata.append((full_url, metadata))
                processed_urls.add(url_to_check)
                order += 1
            
        logger.info(f"Extracted {len(nav_links_with_metadata)} navigation links from Sphinx site.")
        return nav_links_with_metadata

    def extract_main_content_element(self, page_soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """Extracts the main content block from a Sphinx page's soup."""
        # Common main content selectors for Sphinx:
        # <div role="main"> (classic, alabaster)
        # <section role="main"> (html5writer)
        # <div class="body" role="main"> (some themes)
        # <article class="bd-article" ...> (pydata-sphinx-theme)
        # <main id="main-content" ... > (furo)

        selectors = [
            lambda s: s.find('article', class_=re.compile(r'bd-article', re.I)), # PyData Sphinx Theme
            lambda s: s.find('main', attrs={'id': 'main-content'}), # Furo, others
            lambda s: s.find(['div', 'section'], attrs={'role': 'main'}),
            lambda s: s.find('div', class_='body'), # Often wraps the main content
            lambda s: s.find('div', class_='documentwrapper'), # Contains document div
            lambda s: s.find('div', class_='document'), # Core document
        ]
        
        main_content = None
        for selector_func in selectors:
            main_content = selector_func(page_soup)
            if main_content:
                # If we got documentwrapper, try to get its .body child
                if 'documentwrapper' in main_content.get('class', []) and main_content.find('div', class_='body'):
                    return main_content.find('div', class_='body')
                return main_content

        logger.warning("Could not find a distinct main content element for Sphinx. Falling back to body.")
        return page_soup.find('body')

    def process_special_elements(self, main_content_element: BeautifulSoup) -> None:
        """Processes Sphinx-specific elements within the main_content_element."""
        if not main_content_element:
            return

        # Remove permalink anchors (often ¶ or # symbols in headers)
        for headerlink in main_content_element.find_all('a', class_='headerlink'):
            headerlink.decompose()

        # Remove "View page source" links
        for source_link in main_content_element.find_all('a', class_='reference', string='[source]'):
            source_link.decompose()
        for source_link_container in main_content_element.find_all('p', class_='topless'): # Often contains "[source]"
            if source_link_container.find('a', class_='reference', string='[source]'):
                source_link_container.decompose()
        
        # Sphinx copybutton.js adds buttons inside <pre> blocks
        for copy_button in main_content_element.find_all(class_='copybutton'):
            copy_button.decompose()

        # MathJax content: <span class="math">. Markdownify can't convert this.
        # We can either remove it or try to preserve the LaTeX. For now, let's remove the span tag but keep content.
        for math_span in main_content_element.find_all('span', class_='math'):
            math_span.unwrap() # Removes the span but keeps its content (the LaTeX code)

        # Admonitions (note, warning, seealso, etc.)
        # Markdownify handles basic <div class="admonition"><p class="admonition-title">...</p>...</div>
        # Ensure title is bold for better conversion.
        for admonition in main_content_element.find_all('div', class_=re.compile(r'admonition\b')): # \b for word boundary
            title_tag = admonition.find(['p', 'div'], class_='admonition-title')
            if title_tag and title_tag.string:
                 if not title_tag.find('strong'): # Avoid double-bolding
                    title_tag.string = f"**{title_tag.get_text(strip=True)}**"
        
        # Definition lists (dl.field-list, dl.option-list, dl.glossary, dl.simple)
        # Markdownify converts <dl><dt>...</dt><dd>...</dd></dl> reasonably well.
        # No special processing needed unless specific issues arise.

        # Code blocks: div.highlight-LANG > pre or just pre.highlight
        # Markdownify's default code_language_callback should work if lang is in class like 'highlight-python'.
        # If not, we might need to help it find the language.
        for highlight_div in main_content_element.find_all('div', class_=re.compile(r"highlight-\w+")):
            lang_class = next((c for c in highlight_div.get('class', []) if c.startswith('highlight-')), None)
            if lang_class:
                lang = lang_class.split('-', 1)[1]
                pre_tag = highlight_div.find('pre')
                if pre_tag and not pre_tag.has_attr('data-lang'): # Add if not already set
                    pre_tag['data-lang'] = lang


    def extract_page_data(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Extracts title, cleans content, converts to Markdown, and returns a PageContent object."""
        
        title_text = ""
        # Try to get title from H1 in main content first
        main_content_element_for_title = self.extract_main_content_element(page_soup)
        if main_content_element_for_title:
            h1 = main_content_element_for_title.find('h1')
            if h1: title_text = h1.get_text(strip=True)
        
        if not title_text: # Fallback to page <title>
            title_tag = page_soup.find('title')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                # Sphinx titles: "Page Title — Documentation Site Name version" or "Page Title | Site Name"
                title_text = re.split(r'\s*(?:—|\|)\s*', title_text)[0].strip()
        
        if not title_text: # Ultimate fallback
            path_part = urlparse(url).path.split('/')[-1]
            title_text = path_part.replace('-', ' ').replace('_', ' ').title() or "Untitled Page"

        main_content_element = self.extract_main_content_element(page_soup)

        if not main_content_element:
            logger.warning(f"No main content element found for Sphinx page {url}. Content will be empty.")
            return PageContent(url=url, title=title_text, content="", order=0)

        # Generic cleaning + Sphinx-specific cleaning
        # self.clean_content(main_content_element) # Apply generic clean_content from BaseScraper
        self.process_special_elements(main_content_element)

        html_string = str(main_content_element)
        try:
            md = markdownify.markdownify(
                html_string, 
                heading_style="atx",
                bullets='-',
                code_language_callback=lambda el: el.get('data-lang') or (el.get('class')[0].replace('language-', '') if el.get('class') and el.get('class')[0].startswith('language-') else None)
            ).strip()
        except Exception as e:
            logger.error(f"Error during markdownify conversion for Sphinx page {url}: {e}")
            md = f"Error converting content to Markdown: {e}"

        order = 0 # Placeholder
        
        return PageContent(
            url=url,
            title=title_text,
            content=md,
            order=order,
            section="", # Placeholder, can be derived from nav_links_metadata
            subsection="",
            is_index= 'index' in url.lower() or url.endswith(('.html', '/')) and (title_text.lower() in ['introduction', 'overview', 'home', 'contents', 'welcome'])
        )

    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """Extracts potential Sphinx navigation elements from self.soup."""
        nav_elements = []
        # Primary sidebar (classic, alabaster, etc.)
        sidebar_nav = self.soup.find('div', class_='sphinxsidebar')
        if sidebar_nav: nav_elements.append(sidebar_nav)
        
        # HTML5 theme nav (nav[aria-label="main navigation"])
        main_nav = self.soup.find('nav', attrs={'aria-label': re.compile(r'main navigation|global navigation', re.I)})
        if main_nav and main_nav not in nav_elements: nav_elements.append(main_nav)

        # PyData Sphinx Theme, Furo, etc.
        modern_nav = self.soup.find('nav', class_=re.compile(r'(bd-links__nav|sidebar-drawer__content|sd-sidebar-ناطق)', re.I))
        if modern_nav and modern_nav not in nav_elements: nav_elements.append(modern_nav)
        
        toctree_wrappers = self.soup.find_all('div', class_='toctree-wrapper')
        for wrapper in tocTree_wrappers:
            if wrapper not in nav_elements: nav_elements.append(wrapper)
            
        return nav_elements
        
    def extract_page_metadata(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Required by BaseScraper. Delegates to extract_page_data for Sphinx."""
        logger.debug(f"SphinxScraper.extract_page_metadata called for {url}, delegating to extract_page_data.")
        return self.extract_page_data(page_soup, url)
