import re
from bs4 import BeautifulSoup
from typing import List, Optional, Tuple, Dict, Any
from urllib.parse import urljoin, urlparse
import markdownify
import logging

from .base_scraper import BaseScraper, PageContent

logger = logging.getLogger(__name__)

class GitbookScraper(BaseScraper):
    """Scraper for GitBook documentation sites"""

    def __init__(self, soup: BeautifulSoup, base_url: str):
        super().__init__(soup, base_url)
        # self.soup is the soup of the base_url, provided by BaseScraper constructor

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a GitBook site"""
        # Check for meta generator tag
        meta_generator = soup.find("meta", attrs={"name": "generator", "content": re.compile(r"GitBook", re.I)})
        if meta_generator:
            return True
        
        # Existing checks (can be kept as fallbacks)
        return bool(
            soup.find('div', {'class': lambda x: x and 'scroll-pt-' in str(x)}) or # New GitBook
            soup.find('div', {'class': lambda x: x and 'headerLinks_' in str(x)}) or # New GitBook
            soup.find('div', {'data-testid': 'page.contentEditor'}) or # Legacy
            soup.find('div', class_=lambda x: x and 'reset-3c756112--content-764c9ca' in x) or # Legacy
            'gitbook.io' in domain or
            soup.find('div', class_=lambda x: x and "gitbook-layout" in x) or # Common class
            soup.find('style', id="gitbook-root-theme") # Style element
        )

    def extract_navigation_links(self) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract navigation links from the base page's soup (self.soup)."""
        nav_links_with_metadata: List[Tuple[str, Dict[str, Any]]] = []
        processed_urls: set[str] = set()
        
        # Logic adapted from GitbookDownloader._extract_nav_links
        # self.soup is the BeautifulSoup object of the base URL content
        
        # Find GitBook navigation elements (typically in <nav> or <aside>)
        # This can be specific to GitBook's known structures.
        # Example: New GitBook uses <aside> with specific classes. Legacy might use <nav role="navigation">
        
        # Try new GitBook structure first (often in an <aside>)
        nav_container = self.soup.find('aside', {'class': lambda x: x and 'flex' in str(x)})
        if not nav_container:
            # Try legacy navigation structures
            nav_container = self.soup.find(['nav', 'aside', 'div'],
                                           class_=lambda x: x and ('navigation' in x.lower() or
                                                                  'sidebar' in x.lower() or
                                                                  'menu' in x.lower() or
                                                                  'summary' in x.lower() # GitBook legacy uses 'summary' class for ToC
                                                                  ))
        
        if not nav_container:
            logger.warning("Could not find a primary navigation container in GitBook site.")
            # Fallback: Check for any list of links in common nav areas if specific container not found
            nav_elements = self.soup.find_all(['nav', 'aside'])
            if not nav_elements: nav_elements = [self.soup] # process whole page if no nav/aside
        else:
            nav_elements = [nav_container]


        order = 0
        for nav_element in nav_elements:
            # Look for ordered lists or simple lists of links
            # GitBook often uses nested <ul> or <ol> for structure
            for link_tag in nav_element.find_all('a', href=True):
                href = link_tag['href']
                
                # Resolve relative URLs against self.base_url
                full_url = urljoin(self.base_url, href)
                
                # Basic validation: ensure it's an HTTP/HTTPS URL and within the same domain (optional, but good practice)
                parsed_full_url = urlparse(full_url)
                parsed_base_url = urlparse(self.base_url)
                
                if parsed_full_url.scheme not in ['http', 'https']:
                    continue # Skip non-http links
                
                # Optional: Keep links only within the same domain/subdomain
                # if parsed_full_url.netloc != parsed_base_url.netloc:
                #     continue

                # Avoid fragments and already processed URLs
                if parsed_full_url.fragment: # Skip fragment-only links like #section
                    full_url_no_fragment = full_url.split('#')[0]
                    if full_url_no_fragment in processed_urls: continue
                elif full_url in processed_urls:
                    continue
                
                link_text = link_tag.get_text(strip=True) or "Untitled Page"
                
                # Add to list if it's a new, valid link
                # For metadata, we can include title and order.
                # More complex metadata (section, subsection) could be derived here if structure allows.
                metadata = {
                    'title': link_text,
                    'order': order,
                    # 'section': self._get_parent_section(link_tag), # Example if you have such a helper
                }
                nav_links_with_metadata.append((full_url, metadata))
                processed_urls.add(full_url)
                if parsed_full_url.fragment: processed_urls.add(full_url_no_fragment)
                order += 1
        
        # Also check for next/prev navigation links (less common for full ToC)
        # next_links = self.soup.find_all('a', {'aria-label': ['Next', 'Previous', 'next', 'previous']})
        # ... (similar processing if needed) ...

        logger.info(f"Extracted {len(nav_links_with_metadata)} navigation links.")
        return nav_links_with_metadata


    def extract_main_content_element(self, page_soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """
        Extracts the main content block from a page's soup.
        This is specific to GitBook's structure.
        """
        # Try new GitBook structure first (often <main class="flex-1...">)
        main_content = page_soup.find('main', {'class': lambda x: x and 'flex-1' in str(x)})
        if main_content: return main_content

        # Legacy GitBook structure: <div role="main">, <div class="page-inner">, <section class="normal markdown-section">
        main_content = page_soup.find('div', attrs={'role': 'main'})
        if main_content: return main_content
        
        main_content = page_soup.find('div', class_='page-inner')
        if main_content:
            # Inside page-inner, content is often in section.normal or directly
            actual_content = main_content.find('section', class_='normal')
            if actual_content: return actual_content
            return main_content # Return page-inner if no sub-section

        # More generic content tags if specific ones fail
        main_content = page_soup.find(['main', 'article'])
        if main_content: return main_content
        
        # Fallback for very old or custom GitBook: content div
        main_content = page_soup.find('div', {'class': ['markdown', 'content', 'article', 'documentation']})
        if main_content: return main_content
        
        logger.warning("Could not find a distinct main content element. Falling back to body.")
        return page_soup.find('body') # Fallback, might include too much

    def process_special_elements(self, main_content_element: BeautifulSoup) -> None:
        """
        Processes GitBook-specific elements within the main_content_element
        before it's converted to Markdown.
        This method modifies main_content_element in place.
        """
        if not main_content_element:
            return

        # Remove GitBook specific navigation elements like "Previous", "Next" links at the bottom
        for link in main_content_element.find_all('a', text=re.compile(r'Previous|Next', re.I)):
            # Check if they are part of a clear footer/navigation structure within content
            parent_div = link.find_parent('div')
            if parent_div and ('flex' in parent_div.get('class', []) and 'justify-between' in parent_div.get('class', [])):
                parent_div.decompose()
            else:
                link.decompose()

        # Remove headers and footers if they are mistakenly included in main_content_element
        # BaseScraper.clean_content already handles top-level <header>, <footer>.
        # This is for those embedded deeper or with GitBook specific classes.
        for el in main_content_element.find_all(['header', 'footer'], class_=re.compile(r"header|footer", re.I)):
            el.decompose()

        # Remove UI elements like buttons for "Edit this page", "Share", etc.
        for btn_container in main_content_element.find_all('div', class_=lambda x: x and ("buttons" in x or "actions" in x)):
            btn_container.decompose()
        
        # Decompose elements known to be problematic or non-content
        # Example: table of contents within the page body if it's duplicated
        for toc_in_page in main_content_element.find_all('ul', class_="toc"): # GitBook specific class
            toc_in_page.decompose()


    def extract_page_data(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """
        Extracts title, cleans content, converts to Markdown, and returns a PageContent object.
        """
        # 1. Extract Title
        title = None
        h1 = page_soup.find('h1')
        if h1:
            title = h1.get_text(strip=True)
        
        if not title:
            title_tag = page_soup.find('title')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                # Clean up title - remove site name and extra parts (common in GitBook titles)
                title = re.split(r'[|\-–—]\s*(GitBook|Documentation|Book)$', title_text, flags=re.I)[0].strip()
        
        if not title: # Fallback title
            path_part = urlparse(url).path.split('/')[-1]
            if path_part and '.' in path_part: # like 'mypage.html'
                title = path_part.rsplit('.', 1)[0].replace('-', ' ').replace('_', ' ').title()
            elif path_part:
                 title = path_part.replace('-', ' ').replace('_', ' ').title()
            else: # if path is just '/'
                title = urlparse(self.base_url).netloc # Use domain as title for root page
            if not title: title = "Untitled Page"


        # 2. Get Main Content Element
        main_content_element = self.extract_main_content_element(page_soup)

        if not main_content_element:
            logger.warning(f"No main content element found for {url}. Content might be empty or incorrect.")
            # Return PageContent with empty content or raise error?
            # For now, return with empty content, let downloader decide to skip.
            return PageContent(url=url, title=title, content="", order=0) # Default order

        # 3. Clean the main content element
        # First, generic cleaning (removes nav, header, footer, script, style, etc.)
        cleaned_content_element = self.clean_content(main_content_element) # From BaseScraper
        
        # Then, GitBook-specific cleaning
        self.process_special_elements(cleaned_content_element)


        # 4. Convert cleaned HTML content to Markdown
        html_string = str(cleaned_content_element)
        try:
            # Using markdownify with options
            md = markdownify.markdownify(
                html_string, 
                heading_style="atx", # Use '#' for headers
                bullets='-', # Use '-' for unordered lists
                code_language_callback=lambda el: el.get('class', [None])[0] if el.get('class') and el.get('class')[0].startswith('language-') else None
            )
        except Exception as e:
            logger.error(f"Error during markdownify conversion for {url}: {e}")
            md = f"Error converting content to Markdown: {e}"


        # 5. GitBook-specific Markdown Cleanup
        md = re.sub(r'\n{3,}', '\n\n', md).strip()  # Remove excessive newlines
        # Normalize heading levels if necessary (e.g., if GitBook uses H1 for page title and also for section titles)
        # This might be too aggressive, depends on output. For now, let's keep headings as they are after conversion.
        # md = re.sub(r'^#\s', '## ', md, flags=re.MULTILINE) # Example: demote all H1 to H2 in content

        # Attempt to derive order from URL or a common GitBook pattern if possible
        # This is a placeholder; robust order often comes from navigation link metadata
        order = 0 
        # Example: if URL is like /01-introduction.html, try to get 01 as order
        match = re.search(r'/(\d+)[-_]', url)
        if match:
            order = int(match.group(1))
        
        # TODO: Extract section/subsection if possible from page_soup or URL structure

        return PageContent(
            url=url,
            title=title,
            content=md,
            order=order, # Placeholder, ideally comes from nav metadata
            section="", # Placeholder
            subsection="", # Placeholder
            # is_index can be heuristically determined
            is_index= 'index' in url.lower() or url.endswith('/') or (title.lower() in ['introduction', 'overview', 'home'])
        )

    # These methods are part of BaseScraper's abstract methods.
    # extract_navigation_elements is not directly used by DocumentationDownloader if extract_navigation_links is implemented.
    # However, BaseScraper.extract_links (which can be called by a scraper) uses it.
    # For GitbookScraper, we've implemented extract_navigation_links directly.
    # So, this can be minimal or raise NotImplementedError if we are sure it won't be called.
    def extract_navigation_elements(self) -> List[BeautifulSoup]:
        """
        Extracts navigation <aside> or <nav> elements from self.soup (base page).
        This is used by BaseScraper's own extract_links if a derived scraper doesn't override extract_navigation_links.
        Since we've overridden extract_navigation_links, this might not be strictly needed for GitBookScraper's direct use by DocumentationDownloader.
        """
        nav_elements = []
        # Try to find navigation in new GitBook structure
        nav = self.soup.find('aside', {'class': lambda x: x and 'flex' in str(x)})
        if nav:
            nav_elements.append(nav)
            return nav_elements
            
        # Try legacy navigation structures
        nav_elements.extend(self.soup.find_all(
            ['nav', 'aside', 'div'],
            class_=lambda x: x and (
                'navigation' in x.lower() or
                'sidebar' in x.lower() or
                'menu' in x.lower() or
                'summary' in x.lower() # GitBook legacy
            )
        ))
        return nav_elements


    # extract_page_metadata: As per previous reasoning, extract_page_data is the primary method.
    # If BaseScraper's design necessitates this for some internal helpers that GitbookScraper might
    # inadvertently use, it should be implemented. For now, let's assume DocumentationDownloader's
    # direct call to extract_page_data is sufficient.
    # If this method is truly abstract and MUST be implemented, we can make it call extract_page_data
    # or a common helper.
    def extract_page_metadata(self, content_soup: BeautifulSoup, url: str) -> PageContent:
        """
        This method is required by BaseScraper.
        For GitbookScraper, the primary logic is in extract_page_data.
        This can call extract_page_data or be a simplified version if needed elsewhere.
        """
        logger.debug(f"extract_page_metadata called for {url}. Redirecting to extract_page_data.")
        # Assuming 'content_soup' here is equivalent to 'page_soup' in extract_page_data context
        return self.extract_page_data(content_soup, url)
