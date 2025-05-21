import re
import logging
from bs4 import BeautifulSoup
from typing import List, Optional, Tuple, Dict, Any
from urllib.parse import urljoin, urlparse
import markdownify

from .base_scraper import BaseScraper, PageContent

logger = logging.getLogger(__name__)

class ReadmeScraper(BaseScraper):
    """Scraper for ReadMe.com documentation sites"""

    def __init__(self, soup: BeautifulSoup, base_url: str):
        super().__init__(soup, base_url)

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a ReadMe site more accurately."""
        if 'readme.io' in domain or 'readme.com' in domain:
            return True
        
        # Meta tags
        if soup.find('meta', attrs={'name': 'readme-deploy-version'}):
            return True
        if soup.find('meta', attrs={'name': 'readme-id'}): # Common internal ID meta tag
            return True
        
        # Look for specific Readme CSS variables or classes on body/html
        body_tag = soup.find('body')
        if body_tag:
            # Example: <body class="body-documentation ..."> or <body data-readme-version="...">
            if 'body-documentation' in body_tag.get('class', []):
                return True
            if body_tag.get('data-readme-version'):
                return True

        # Check for script URLs containing readme.io or readme.com
        for script_tag in soup.find_all('script', src=True):
            if 'readme.io' in script_tag['src'] or 'readme.com' in script_tag['src']:
                return True
        
        # Check for link hrefs (e.g., for stylesheets)
        for link_tag in soup.find_all('link', href=True):
            if 'readme.io' in link_tag['href'] or 'readme.com' in link_tag['href']:
                return True

        # Fallback to some existing checks like common class names
        # (e.g., deepgram.com is a known Readme user)
        if domain in ['deepgram.com'] or soup.find('div', class_=re.compile(r'(hub-page-wrapper|content-body|markdown-body)')):
            return True
            
        return False

    def extract_navigation_links(self) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract navigation links from Readme site using self.soup (base page soup)."""
        nav_links_with_metadata: List[Tuple[str, Dict[str, Any]]] = []
        processed_urls: set[str] = set()
        
        # Readme navigation is typically in:
        # <nav class="hub-sidebar ..."> or <nav class="NavShell_nav..."> or <nav aria-label="Docs Nav">
        # Links are often in <ul> or <div> elements with classes like "menu-sub", "sublist-item", "NavItem_container..."
        
        nav_container = self.soup.find('nav', class_=re.compile(r'(hub-sidebar|NavShell_nav|sidebar)', re.I))
        if not nav_container:
            nav_container = self.soup.find('nav', attrs={'aria-label': re.compile(r'(Docs Nav|Primary navigation)', re.I)})
        
        if not nav_container:
            logger.warning("Primary Readme navigation container not found. Trying generic nav/div.")
            nav_container = self.soup.find(['nav', 'div'], class_=re.compile(r'(navigation|menu|nav-container)', re.I))

        if not nav_container:
            logger.error("Could not find any navigation container for Readme scraper.")
            return []

        order = 0
        for link_tag in nav_container.find_all('a', href=True):
            href = link_tag['href']
            
            full_url = urljoin(self.base_url, href)
            
            parsed_full_url = urlparse(full_url)
            if parsed_full_url.scheme not in ['http', 'https']:
                continue

            url_to_check = parsed_full_url._replace(fragment="").geturl()
            if url_to_check in processed_urls or not url_to_check.startswith(self.base_url.split('//')[0]): # Ensure same domain/protocol start
                 if not url_to_check.startswith(self.base_url) and not href.startswith('/'): # Allow relative links
                    logger.debug(f"Skipping probably external or already processed link: {full_url}")
                    continue


            link_text = link_tag.get_text(strip=True) or "Untitled Page"
            
            metadata = {
                'title': link_text,
                'order': order,
                # 'section': self._get_parent_section(link_tag), # Implement if possible
            }
            nav_links_with_metadata.append((full_url, metadata))
            processed_urls.add(url_to_check)
            order += 1
            
        logger.info(f"Extracted {len(nav_links_with_metadata)} navigation links from Readme site.")
        return nav_links_with_metadata

    def extract_main_content_element(self, page_soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """Extracts the main content block from a Readme page's soup."""
        # Common Readme main content containers:
        # <div class="hub-content-layout ..."> <article class="page-body ...">
        # <main id="main-content" ...>
        # <div class="markdown-body ..."> (often for user-generated markdown content)
        # <div class="content-body ..."> (seen on deepgram, a readme user)

        selectors = [
            lambda s: s.find('div', class_=re.compile(r'hub-content-layout', re.I)), # This often contains the article
            lambda s: s.find('main', attrs={'id': 'main-content'}),
            lambda s: s.find('article', class_=re.compile(r'page-body', re.I)),
            lambda s: s.find('div', class_=re.compile(r'markdown-body', re.I)),
            lambda s: s.find('div', class_=re.compile(r'content-body', re.I)),
            lambda s: s.find('main') # Generic main as fallback
        ]

        main_content = None
        for selector_func in selectors:
            main_content_candidate = selector_func(page_soup)
            if main_content_candidate:
                # If we found hub-content-layout, try to get the article.page-body inside it
                if 'hub-content-layout' in main_content_candidate.get('class', []):
                    article_body = main_content_candidate.find('article', class_=re.compile(r'page-body', re.I))
                    if article_body:
                        main_content = article_body
                        break
                main_content = main_content_candidate # Use the found candidate
                break 
        
        if not main_content:
            logger.warning("Could not find a distinct main content element for Readme. Falling back to body.")
            return page_soup.find('body')
        return main_content

    def process_special_elements(self, main_content_element: BeautifulSoup) -> None:
        """Processes Readme-specific elements within the main_content_element."""
        if not main_content_element:
            return

        # Remove "Suggest Edits" links or similar interactive elements
        for edit_link in main_content_element.find_all('a', class_=re.compile(r'(suggest-edits|edit-page-button)', re.I)):
            edit_link.decompose()
        
        for feedback_widget in main_content_element.find_all('div', class_=re.compile(r'(feedback-widget|article-ratings)', re.I)):
            feedback_widget.decompose()

        # Handle Readme's code blocks (rdmd-codeblock)
        # Markdownify might handle <pre><code> well, but Readme often has complex structures.
        # For now, let's assume markdownify will do a decent job if we simplify.
        # Decompose code tab selectors if they are separate from the actual code.
        for code_tab_selector in main_content_element.find_all('div', class_=re.compile(r'CodeTabs_buttons', re.I)):
            code_tab_selector.decompose()
        
        # Handle callouts (magic blocks) - convert to simple blockquotes
        for callout in main_content_element.find_all('div', class_=re.compile(r'magic-block-callout', re.I)):
            callout_type_div = callout.find('div', class_=re.compile(r'CalloutInfo_container', re.I)) # Contains icon and type
            callout_content_div = callout.find('div', class_=lambda x: x and x.startswith('CalloutMessage_message'))
            
            title = ""
            if callout_type_div:
                title_span = callout_type_div.find('span')
                if title_span: title = title_span.get_text(strip=True)
                callout_type_div.decompose() # Remove the icon/type div

            if callout_content_div:
                blockquote = page_soup.new_tag('blockquote')
                if title:
                    strong_title = page_soup.new_tag('strong')
                    strong_title.string = title
                    blockquote.append(strong_title)
                    blockquote.append(page_soup.new_tag('br'))
                # Move children of callout_content_div to blockquote
                blockquote.extend(callout_content_div.contents)
                callout.replace_with(blockquote)
            else: # If structure is different, just try to preserve content
                callout.name = 'blockquote' # Convert the div itself to a blockquote

        # Remove API explorers or interactive API sections if they are not convertible
        for api_section in main_content_element.find_all('section', class_=re.compile(r'(hub-api|TryItContainer_root)')):
            api_section.decompose()
        
        # Remove elements specific to Deepgram's Readme theme if needed
        for element in main_content_element.find_all(class_=lambda x: x and any(cls in str(x).lower() for cls in [
            'feedback-', 'edit-', 'toolbar-', 'toc-', 'docs-header', 'page-header' # if page-header is just title, keep
        ])):
            if 'page-header' in element.get('class', []) and element.find('h1'): # Keep H1 if it's in page-header
                 for child in element.find_all(recursive=False): # Decompose other children of page-header
                     if child.name != 'h1': child.decompose()
            else:
                element.decompose()


    def extract_page_data(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Extracts title, cleans content, converts to Markdown, and returns a PageContent object."""
        
        title_text = ""
        main_content_element_for_title = self.extract_main_content_element(page_soup)
        if main_content_element_for_title:
            h1 = main_content_element_for_title.find('h1')
            if h1:
                title_text = h1.get_text(strip=True)
        
        if not title_text:
            title_tag = page_soup.find('title')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                # Readme titles often include site name: "Page Title - Site Name" or "Page Title | Site Name"
                title_text = re.split(r'\s*[-\|]\s*', title_text)[0].strip() 
        
        if not title_text:
            path_part = urlparse(url).path.split('/')[-1]
            title_text = path_part.replace('-', ' ').replace('_', ' ').title() or "Untitled Page"

        main_content_element = self.extract_main_content_element(page_soup)

        if not main_content_element:
            logger.warning(f"No main content element found for Readme page {url}. Content will be empty.")
            return PageContent(url=url, title=title_text, content="", order=0)

        # Generic cleaning + Readme-specific cleaning
        main_content_element = self.clean_content(main_content_element) # From BaseScraper
        self.process_special_elements(main_content_element)

        html_string = str(main_content_element)
        try:
            # Markdownify options for Readme:
            # Readme often uses <pre><code class="lang-xxx">...</code></pre>
            # The default code_language_callback in markdownify should handle this.
            md = markdownify.markdownify(
                html_string, 
                heading_style="atx",
                bullets='-',
                # Default code language callback is usually good.
                # convert=['figure'] # If figures are used and contain meaningful content
            ).strip()
        except Exception as e:
            logger.error(f"Error during markdownify conversion for Readme page {url}: {e}")
            md = f"Error converting content to Markdown: {e}"

        order = 0 # Placeholder, ideally from nav_links_metadata
        
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
        """Extracts potential Readme navigation elements from self.soup."""
        nav_elements = []
        # Try specific Readme nav selectors
        main_nav = self.soup.find('nav', class_=re.compile(r'(hub-sidebar|NavShell_nav|sidebar)', re.I))
        if main_nav:
            nav_elements.append(main_nav)
        
        alt_nav = self.soup.find('nav', attrs={'aria-label': re.compile(r'(Docs Nav|Primary navigation)', re.I)})
        if alt_nav and alt_nav not in nav_elements:
             nav_elements.append(alt_nav)

        if not nav_elements: # Fallback
            nav_elements.extend(self.soup.find_all(['nav', 'div'], class_=re.compile(r'(navigation|menu|nav-container|sidebar)', re.I)))
        return nav_elements
        
    def extract_page_metadata(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Required by BaseScraper. Delegates to extract_page_data for Readme."""
        logger.debug(f"ReadmeScraper.extract_page_metadata called for {url}, delegating to extract_page_data.")
        return self.extract_page_data(page_soup, url)
