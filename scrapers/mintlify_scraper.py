import re
import logging
from bs4 import BeautifulSoup
from typing import List, Optional, Tuple, Dict, Any
from urllib.parse import urljoin, urlparse
import markdownify

from .base_scraper import BaseScraper, PageContent

logger = logging.getLogger(__name__)

class MintlifyScraper(BaseScraper):
    """Scraper for Mintlify documentation sites"""

    def __init__(self, soup: BeautifulSoup, base_url: str):
        super().__init__(soup, base_url)

    @classmethod
    def can_handle(cls, soup: BeautifulSoup, domain: str) -> bool:
        """Check if this is a Mintlify site."""
        # Meta tags
        if soup.find("meta", attrs={"name": re.compile(r"mintlify:version", re.I)}) or \
           soup.find("meta", attrs={"name": "generator", "content": re.compile(r"Mintlify", re.I)}):
            return True

        # Specific body or root element classes/attributes
        body_tag = soup.find('body')
        if body_tag and ("mintlify-page" in body_tag.get('class', []) or "mintlify-docs-page" in body_tag.get('class', [])):
            return True
        if soup.find(id="root") and (soup.find("div", class_=lambda x: x and "mode-docs" in x) or soup.find("div", class_=lambda x: x and "mintlify-layout" in x)): # Common Mintlify layout patterns
             return True
        
        # Check for script URLs containing cdn.mintlify.com or mintlify.js
        for script_tag in soup.find_all('script', src=True):
            if 'cdn.mintlify.com' in script_tag['src'] or 'mintlify.js' in script_tag['src']:
                return True
        
        # Check for link hrefs (e.g., for stylesheets)
        for link_tag in soup.find_all('link', href=True):
            if 'cdn.mintlify.com' in link_tag['href']:
                return True
        
        # Check for specific footer patterns if available (less reliable)
        footer = soup.find('footer')
        if footer and footer.find('a', href=re.compile(r'mintlify.com', re.I), string=re.compile(r'Powered by Mintlify', re.I)):
            return True

        return False

    def extract_navigation_links(self) -> List[Tuple[str, Dict[str, Any]]]:
        """Extract navigation links from Mintlify site using self.soup (base page soup)."""
        nav_links_with_metadata: List[Tuple[str, Dict[str, Any]]] = []
        processed_urls: set[str] = set()
        order = 0
        
        # Mintlify navigation can be in:
        # <nav class="...sidebar..."> or <aside class="...sidebar...">
        # Often contains roles like navigation or aria-label="Sidebar"
        # Links are typically within nested lists or divs with specific classes like "Navigation_link..."
        
        nav_container = self.soup.find(['nav', 'aside'], class_=re.compile(r'(sidebar|Navigation_sidebar|DocsNavigation_sidebar)', re.I))
        if not nav_container:
             nav_container = self.soup.find(['nav', 'aside'], attrs={'aria-label': re.compile(r'(Sidebar|Main navigation)', re.I)})

        if not nav_container:
            logger.warning("Primary Mintlify navigation container not found. Trying generic nav/div.")
            # Fallback to any nav or a div that looks like a sidebar structure
            nav_container = self.soup.find(['nav', 'div'], class_=re.compile(r'(nav|menu|navigation|sidebar)', re.I))


        if not nav_container:
            logger.error("Could not find any navigation container for Mintlify scraper.")
            return []

        for link_tag in nav_container.find_all('a', href=True):
            href = link_tag['href']
            
            # Mintlify links are usually relative or absolute within the same domain
            full_url = urljoin(self.base_url, href)
            
            parsed_full_url = urlparse(full_url)
            if parsed_full_url.scheme not in ['http', 'https']:
                continue

            url_to_check = parsed_full_url._replace(fragment="").geturl()
            # Ensure it's a sub-path of the base_url or same domain
            if not url_to_check.startswith(self.base_url.split('//')[0]): # Protocol check
                 if not url_to_check.startswith(self.base_url) and not href.startswith('/'): # Allow relative
                    logger.debug(f"Skipping probably external link: {full_url}")
                    continue
            if url_to_check in processed_urls:
                continue
            
            link_text = link_tag.get_text(strip=True) or "Untitled Page"
            
            # Attempt to derive section from parent elements (e.g., a preceding header or group title)
            section_name = ""
            # Look for a parent div/li that represents a group, then find its title
            # Example: <div class="Navigation_group__..."> <p class="Navigation_groupTitle__...">Group Title</p> ... links ... </div>
            parent_group = link_tag.find_parent(class_=re.compile(r'(Navigation_group|menu-group|sidebar-group)', re.I))
            if parent_group:
                group_title_tag = parent_group.find(class_=re.compile(r'(Navigation_groupTitle|menu-group-title|sidebar-group-title)', re.I))
                if group_title_tag:
                    section_name = group_title_tag.get_text(strip=True)
            
            metadata = {
                'title': link_text,
                'order': order,
                'section': section_name,
            }
            nav_links_with_metadata.append((full_url, metadata))
            processed_urls.add(url_to_check)
            order += 1
            
        logger.info(f"Extracted {len(nav_links_with_metadata)} navigation links from Mintlify site.")
        return nav_links_with_metadata

    def extract_main_content_element(self, page_soup: BeautifulSoup) -> Optional[BeautifulSoup]:
        """Extracts the main content block from a Mintlify page's soup."""
        # Common Mintlify main content selectors:
        # <main role="main"> (often contains the core content)
        # <div class="DocsPage_content__...">
        # <article class="prose ..."> (TailwindCSS typography, sometimes used)
        # <div class="markdown-body"> (if they use a generic markdown renderer)
        
        selectors = [
            lambda s: s.find('main', attrs={'role': 'main'}),
            lambda s: s.find('div', class_=re.compile(r'DocsPage_content|mintlify-content|Page_markdownWrapper', re.I)),
            lambda s: s.find('article', class_=re.compile(r'prose', re.I)),
            lambda s: s.find('div', class_=re.compile(r'markdown', re.I)), # More generic
        ]
        
        main_content = None
        for selector_func in selectors:
            main_content = selector_func(page_soup)
            if main_content:
                 # Sometimes the selected element is a wrapper, try to find a more specific content child
                if main_content.name == 'main':
                    inner_article = main_content.find('article')
                    if inner_article: return inner_article
                    inner_div_content = main_content.find('div', class_=re.compile(r'(content|markdown|prose)', re.I))
                    if inner_div_content: return inner_div_content
                return main_content

        logger.warning("Could not find a distinct main content element for Mintlify. Falling back to body.")
        return page_soup.find('body')

    def process_special_elements(self, main_content_element: BeautifulSoup) -> None:
        """Processes Mintlify-specific elements within the main_content_element."""
        if not main_content_element:
            return

        # Remove "Edit this page", "Was this helpful?", feedback forms
        for el in main_content_element.find_all(class_=re.compile(r'(EditThisPageButton_container|FeedbackExplodingButton_container|DocsPage_feedback)', re.I)):
            el.decompose()

        # Handle Mintlify callouts/info boxes (e.g., <div class="Callout_callout__...">)
        # Convert to simple blockquotes for markdownify
        for callout in main_content_element.find_all('div', class_=re.compile(r'Callout_callout', re.I)):
            icon_div = callout.find('div', class_=re.compile(r'Callout_iconContainer', re.I))
            content_div = callout.find('div', class_=lambda x: x and not x.startswith('Callout_iconContainer')) # Assume rest is content

            title = ""
            if icon_div: # Mintlify callouts might not have explicit titles, but icon implies type
                svg_or_img = icon_div.find(['svg', 'img'])
                if svg_or_img:
                    title = svg_or_img.get('alt', '') or svg_or_img.name.capitalize() # Use alt or tag name
                icon_div.decompose()
            
            if content_div:
                blockquote = main_content_element.new_tag('blockquote')
                if title:
                    strong_title = main_content_element.new_tag('strong')
                    strong_title.string = title
                    blockquote.append(strong_title)
                    blockquote.append(main_content_element.new_tag('br'))
                blockquote.extend(content_div.contents)
                callout.replace_with(blockquote)
            else: # If structure is different, just convert the div itself
                callout.name = 'blockquote'


        # Code blocks: Mintlify often uses <div class="CodeBlock_container__..."> which contains <pre><code>
        # Markdownify should handle <pre><code>. We need to ensure language is detected.
        # Mintlify might store language in a data attribute or a class on a child.
        for code_block_container in main_content_element.find_all('div', class_=re.compile(r'CodeBlock_container', re.I)):
            pre_tag = code_block_container.find('pre')
            if pre_tag:
                # Check if language is specified in a button or tab within the container
                lang_button = code_block_container.find('button', class_=re.compile(r'CodeTabs_tab', re.I), attrs={'data-active': 'true'})
                if lang_button:
                    lang = lang_button.get_text(strip=True).lower()
                    if lang and not pre_tag.has_attr('data-lang'): pre_tag['data-lang'] = lang
                
                # Sometimes Mintlify has a div with class="language-xxx" around the pre
                parent_lang_div = code_block_container.find('div', class_=re.compile(r"language-\w+"))
                if parent_lang_div and not pre_tag.has_attr('data-lang'):
                    lang_class = next((c for c in parent_lang_div.get('class', []) if c.startswith('language-')), None)
                    if lang_class: pre_tag['data-lang'] = lang_class.split('-',1)[1]
                
                # Decompose any copy buttons or other UI elements within the code block container, leaving pre
                for btn in code_block_container.find_all('button', class_=re.compile(r'CopyButton', re.I)):
                    btn.decompose()
                # If the container itself is not the pre tag, we might want to replace container with pre
                if code_block_container != pre_tag:
                    code_block_container.replace_with(pre_tag)


        # Remove other interactive elements like image zoom wrappers if they interfere
        for img_zoom_wrapper in main_content_element.find_all('div', class_=re.compile(r'ZoomableImage_container', re.I)):
            img_tag = img_zoom_wrapper.find('img')
            if img_tag:
                img_zoom_wrapper.replace_with(img_tag) # Keep the image, remove the wrapper
            else:
                img_zoom_wrapper.decompose()


    def extract_page_data(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Extracts title, cleans content, converts to Markdown, and returns a PageContent object."""
        
        title_text = ""
        main_content_element_for_title = self.extract_main_content_element(page_soup)
        if main_content_element_for_title:
            # Mintlify often has H1 as part of a header component, not always first child of main content
            h1 = page_soup.find('h1') # Search broader for H1 if not in main content's direct children
            if not h1 and main_content_element_for_title: # Fallback to H1 within main content
                 h1 = main_content_element_for_title.find('h1')

            if h1: title_text = h1.get_text(strip=True)
        
        if not title_text:
            title_tag = page_soup.find('title')
            if title_tag:
                title_text = title_tag.get_text(strip=True)
                # Mintlify titles: "Page Title | Site Name" or "Page Title – Site Name"
                title_text = re.split(r'\s*[-\|–]\s*', title_text)[0].strip()
        
        if not title_text:
            path_part = urlparse(url).path.strip('/').split('/')[-1]
            title_text = path_part.replace('-', ' ').replace('_', ' ').title() or "Untitled Page"

        main_content_element = self.extract_main_content_element(page_soup)

        if not main_content_element:
            logger.warning(f"No main content element found for Mintlify page {url}. Content will be empty.")
            return PageContent(url=url, title=title_text, content="", order=0)

        # Generic cleaning + Mintlify-specific cleaning
        main_content_element = self.clean_content(main_content_element) # From BaseScraper, removes nav, footer, script, style if within main_content
        self.process_special_elements(main_content_element)

        html_string = str(main_content_element)
        try:
            md = markdownify.markdownify(
                html_string, 
                heading_style="atx",
                bullets='-',
                code_language_callback=lambda el: el.get('data-lang') or (el.find_parent('div', class_=re.compile(r"language-(\w+)")) and el.find_parent('div', class_=re.compile(r"language-(\w+)")).get('class')[0].split('-')[-1])
            ).strip()
        except Exception as e:
            logger.error(f"Error during markdownify conversion for Mintlify page {url}: {e}")
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
        """Extracts potential Mintlify navigation elements from self.soup."""
        nav_elements = []
        nav_main = self.soup.find(['nav', 'aside'], class_=re.compile(r'(sidebar|Navigation_sidebar|DocsNavigation_sidebar)', re.I))
        if nav_main: nav_elements.append(nav_main)
        
        nav_aria = self.soup.find(['nav', 'aside'], attrs={'aria-label': re.compile(r'(Sidebar|Main navigation)', re.I)})
        if nav_aria and nav_aria not in nav_elements: nav_elements.append(nav_aria)

        if not nav_elements:
            nav_elements.extend(self.soup.find_all(['nav', 'div'], class_=re.compile(r'(nav|menu|navigation|sidebar)', re.I)))
        return nav_elements
        
    def extract_page_metadata(self, page_soup: BeautifulSoup, url: str) -> PageContent:
        """Required by BaseScraper. Delegates to extract_page_data for Mintlify."""
        logger.debug(f"MintlifyScraper.extract_page_metadata called for {url}, delegating to extract_page_data.")
        return self.extract_page_data(page_soup, url)
