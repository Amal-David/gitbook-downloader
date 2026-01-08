from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional, List, Set
from urllib.parse import urljoin, urlparse
import asyncio
import hashlib
import logging
import re
import time

import aiohttp
import markdownify
from bs4 import BeautifulSoup
from slugify import slugify

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Regex to match version path segments (e.g., /v1/, /nightly/, /beta/)
VERSION_PATH_PATTERN = re.compile(
    r'/(?:v\d+(?:\.\d+)*|nightly|canary|next|latest|testnet|stable|beta|alpha|rc\d*|dev|staging|main|master|trunk|edge|unstable)(?:/|$)',
    re.IGNORECASE
)


def normalize_url(href: str, base_url: str) -> Optional[str]:
    """Convert href to full URL, strip fragments, normalize slashes.
    Returns None if URL should be skipped (fragment-only or external)."""
    if not href or href.startswith("#"):
        return None

    parsed_href = urlparse(href)
    if not parsed_href.netloc:
        full_url = urljoin(base_url, href)
    elif href.startswith(base_url.rstrip("/")):
        full_url = href
    else:
        return None  # External URL

    # Strip fragment and normalize trailing slash
    return full_url.split("#", 1)[0].rstrip("/")


def should_skip_url(url: str) -> bool:
    """Return True for mailto:, images, PDFs, etc."""
    skip_patterns = ["mailto:", "tel:", ".pdf", ".jpg", ".png", ".gif", ".svg", "api-docs"]
    return any(skip in url for skip in skip_patterns)


def is_different_version_path(url: str, base_url: str) -> bool:
    """Return True if URL is from a different version path (e.g., /nightly/, /v2/).

    This prevents crawling multiple versions of the same docs which causes duplicates.
    """
    base_path = urlparse(base_url).path
    url_path = urlparse(url).path

    url_has_version = bool(VERSION_PATH_PATTERN.search(url_path))
    base_has_version = bool(VERSION_PATH_PATTERN.search(base_path))

    return url_has_version != base_has_version


def is_different_doc_section(url: str, base_url: str) -> bool:
    """Return True if URL is from a different documentation section.

    For Docusaurus and similar sites that have multiple doc sections (e.g., /developers/,
    /operators/), this prevents crawling into unrelated sections.
    """
    base_path = urlparse(base_url).path.strip("/")
    url_path = urlparse(url).path.strip("/")

    if not base_path:
        return False

    # Get the first path segment(s) that define the doc section
    base_segments = base_path.split("/")
    url_segments = url_path.split("/")

    if not url_segments:
        return False

    # Common documentation section prefixes - these indicate distinct doc areas
    doc_section_prefixes = {"developers", "operators", "nodes", "guides", "tutorials",
                           "api", "reference", "solidity-guides", "relayer-sdk-guides",
                           "examples", "zama-protocol-litepaper", "network", "setup",
                           "operation", "infrastructure", "validator", "sequencer"}

    # Check if base URL has a section prefix
    base_section = None
    base_section_idx = -1
    for i, seg in enumerate(base_segments):
        if seg.lower() in doc_section_prefixes:
            base_section = seg.lower()
            base_section_idx = i
            break

    # Check if URL has a section prefix
    url_section = None
    for seg in url_segments:
        if seg.lower() in doc_section_prefixes:
            url_section = seg.lower()
            break

    # If base has no section prefix but URL does, only filter if URL goes into
    # a clearly different doc area (not just any section prefix)
    # This allows /developers/ to be crawled from / but blocks /operators/
    if base_section is None and url_section is not None:
        # Don't filter - let the crawl discover the main section
        # The recursive crawl will then be limited to that section
        pass

    # If both have section prefixes, they must match
    if base_section and url_section and base_section != url_section:
        return True

    # If URL goes deeper into a recognized section that base didn't specify
    # (e.g., base=/protocol/protocol/, url=/protocol/solidity-guides/)
    if base_section:
        # Check if URL has a different section at the same or deeper level
        for i, seg in enumerate(url_segments):
            if i > base_section_idx and seg.lower() in doc_section_prefixes:
                if seg.lower() != base_section:
                    return True

    return False


class NavExtractor(ABC):
    """Abstract base class for navigation extraction strategies."""

    @abstractmethod
    def can_handle(self, soup: BeautifulSoup) -> bool:
        """Return True if this extractor can handle the page structure."""
        pass

    @abstractmethod
    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        """Extract navigation links as list of (url, title, depth) tuples.
        URL can be None for section headers."""
        pass

    def _process_nav_list(self, nav_list, base_url: str, processed_urls: Set[str], depth: int = 0) -> List[tuple]:
        """Recursively process navigation list items, tracking depth for hierarchy."""
        nav_links = []
        for li in nav_list.find_all("li", recursive=False):
            link = li.find("a", href=True)
            if link:
                url = normalize_url(link["href"], base_url)
                if url and url not in processed_urls and not should_skip_url(url):
                    nav_links.append((url, link.get_text(strip=True), depth))
                    processed_urls.add(url)

            # Process nested lists (children of this li)
            for nested_list in li.find_all(["ol", "ul"], recursive=False):
                nav_links.extend(self._process_nav_list(nested_list, base_url, processed_urls, depth + 1))

        return nav_links


class MintlifyExtractor(NavExtractor):
    """Extractor for Mintlify documentation sites."""

    def can_handle(self, soup: BeautifulSoup) -> bool:
        return soup.find(id="navigation-items") is not None

    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        nav_links = []
        navigation_items = soup.find(id="navigation-items")

        for child in navigation_items.children:
            if not hasattr(child, 'name'):
                continue

            # Check for section group (div with sidebar-group-header + sidebar-group ul)
            group_header = child.find(class_="sidebar-group-header") if hasattr(child, 'find') else None
            if group_header:
                # Get section title from h5 or other heading
                title_elem = group_header.find(["h5", "h4", "h3", "span"])
                if title_elem:
                    section_title = title_elem.get_text(strip=True)
                    if section_title:
                        nav_links.append((None, section_title, 0))  # Section header

                # Get links in this section
                sidebar_group = child.find(class_="sidebar-group") or child.find("ul")
                if sidebar_group:
                    nav_links.extend(self._process_nav_list(sidebar_group, base_url, processed_urls, depth=1))

            elif child.name == "ul":
                nav_links.extend(self._process_nav_list(child, base_url, processed_urls, depth=0))

        return nav_links


class GitBookExtractor(NavExtractor):
    """Extractor for traditional GitBook sites with nav/aside navigation."""

    def can_handle(self, soup: BeautifulSoup) -> bool:
        nav_elements = soup.find_all(["nav", "aside"])
        for nav in nav_elements:
            if nav.find_all(["ol", "ul"]):
                return True
        return False

    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        nav_links = []
        nav_elements = soup.find_all(["nav", "aside"])

        for nav in nav_elements:
            nav_lists = nav.find_all(["ol", "ul"], recursive=False)
            if not nav_lists:
                nav_lists = nav.find_all(["ol", "ul"])
            for nav_list in nav_lists:
                nav_links.extend(self._process_nav_list(nav_list, base_url, processed_urls, depth=0))

        # Also check for next/prev navigation links
        for link in soup.find_all("a", {"aria-label": ["Next", "Previous", "next", "previous"]}):
            url = normalize_url(link.get("href"), base_url)
            if url and url not in processed_urls:
                nav_links.append((url, link.get_text(strip=True), 0))
                processed_urls.add(url)

        return nav_links


class VocsExtractor(NavExtractor):
    """Extractor for Vocs documentation sites (e.g., metalex-docs.vercel.app)."""

    def can_handle(self, soup: BeautifulSoup) -> bool:
        return soup.find(class_="vocs_Sidebar_navigation") is not None

    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        nav_links = []
        nav = soup.find(class_="vocs_Sidebar_navigation")
        if not nav:
            return nav_links

        # Process all top-level sections
        for section in nav.find_all("section", class_="vocs_Sidebar_section", recursive=False):
            nav_links.extend(self._process_vocs_section(section, base_url, processed_urls, depth=0))

        # Also process any div.vocs_Sidebar_group that contains sections
        for group in nav.find_all("div", class_="vocs_Sidebar_group", recursive=False):
            for section in group.find_all("section", class_="vocs_Sidebar_section", recursive=False):
                nav_links.extend(self._process_vocs_section(section, base_url, processed_urls, depth=0))

        return nav_links

    def _process_vocs_section(self, section, base_url: str, processed_urls: Set[str], depth: int) -> List[tuple]:
        """Recursively process a Vocs sidebar section."""
        nav_links = []
        has_header = False

        # Look for section header
        header = section.find("div", class_="vocs_Sidebar_sectionHeader", recursive=False)
        if header:
            # Check for section title (non-link header like "🤖 BORGs")
            title_elem = header.find("div", class_="vocs_Sidebar_sectionTitle")
            if title_elem:
                section_title = title_elem.get_text(strip=True)
                if section_title:
                    nav_links.append((None, section_title, depth))
                    has_header = True

            # Check for non-link item header (like "📋 BORG Types" which is a div, not a link)
            if not has_header:
                item_div = header.find("div", class_="vocs_Sidebar_item")
                if item_div and not item_div.find("a"):
                    section_title = item_div.get_text(strip=True)
                    if section_title:
                        nav_links.append((None, section_title, depth))
                        has_header = True

            # Check for link in header (like "BORG Modes" which is both a page and section header)
            link = header.find("a", class_="vocs_Sidebar_item", href=True)
            if link:
                url = normalize_url(link["href"], base_url)
                if url and url not in processed_urls and not should_skip_url(url):
                    nav_links.append((url, link.get_text(strip=True), depth))
                    processed_urls.add(url)
                    has_header = True

        # Determine child depth: if there's a header, children are one level deeper
        child_depth = depth + 1 if has_header else depth

        # Process direct item links in this section
        items_div = section.find("div", class_="vocs_Sidebar_items", recursive=False)

        # Collect nested section containers to avoid processing their links twice
        nested_section_containers = set()
        if items_div:
            for nested_section in items_div.find_all("section", class_="vocs_Sidebar_section", recursive=True):
                nested_section_containers.add(id(nested_section))

        if items_div:
            # Find all links in items_div (including wrapped ones), but exclude those inside nested sections
            for link in items_div.find_all("a", class_="vocs_Sidebar_item", href=True):
                # Skip if this link is inside a nested section (will be processed recursively)
                parent_section = link.find_parent("section", class_="vocs_Sidebar_section")
                if parent_section and id(parent_section) in nested_section_containers:
                    continue

                url = normalize_url(link["href"], base_url)
                if url and url not in processed_urls and not should_skip_url(url):
                    nav_links.append((url, link.get_text(strip=True), child_depth))
                    processed_urls.add(url)

        # Process nested sections (subsections) - both directly under section and inside items_div
        all_nested_sections = []
        for nested_section in section.find_all("section", class_="vocs_Sidebar_section", recursive=False):
            all_nested_sections.append(nested_section)
        if items_div:
            for nested_section in items_div.find_all("section", class_="vocs_Sidebar_section", recursive=False):
                if nested_section not in all_nested_sections:
                    all_nested_sections.append(nested_section)

        for nested_section in all_nested_sections:
            nav_links.extend(self._process_vocs_section(nested_section, base_url, processed_urls, child_depth))

        return nav_links


class DocusaurusExtractor(NavExtractor):
    """Extractor for Docusaurus v2/v3 documentation sites."""

    def can_handle(self, soup: BeautifulSoup) -> bool:
        # Docusaurus uses Infima CSS with menu__list and menu__link classes
        menu_list = soup.find(class_=re.compile(r'\bmenu__list\b'))
        menu_link = soup.find(class_=re.compile(r'\bmenu__link\b'))
        return menu_list is not None and menu_link is not None

    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        nav_links = []

        # Find the main sidebar navigation
        sidebar = soup.find('nav', class_=re.compile(r'\bmenu\b'))
        if not sidebar:
            sidebar = soup.find('aside', class_=re.compile(r'docSidebar|theme-doc-sidebar'))
        if not sidebar:
            # Try finding any element containing menu__list
            menu_list = soup.find('ul', class_=re.compile(r'\bmenu__list\b'))
            if menu_list:
                sidebar = menu_list.parent
        if not sidebar:
            return nav_links

        # Find top-level menu lists - only take the first one to avoid duplicate
        # version sidebars (e.g., Aztec has multiple version docs)
        menu_lists = sidebar.find_all('ul', class_=re.compile(r'\bmenu__list\b'), recursive=False)
        if not menu_lists:
            menu_lists = sidebar.find_all('ul', class_=re.compile(r'\bmenu__list\b'))

        # Only process the first menu list to avoid duplicates from multiple versions
        if menu_lists:
            nav_links.extend(self._process_menu_list(menu_lists[0], base_url, processed_urls, depth=0))

        return nav_links

    def _process_menu_list(self, menu_list, base_url: str, processed_urls: Set[str], depth: int) -> List[tuple]:
        nav_links = []
        in_section = False  # Track if we're inside a named section

        # Find all list items (both menu__list-item and sidebar-title items)
        # Handle both direct <li> children and <li> inside <div> wrappers (Uniswap docs pattern)
        direct_lis = menu_list.find_all('li', recursive=False)
        if not direct_lis:
            # Check for <li> inside direct <div> children (e.g., <ul><div><li>...</li></div></ul>)
            direct_lis = []
            for child in menu_list.children:
                if hasattr(child, 'name') and child.name == 'div':
                    direct_lis.extend(child.find_all('li', recursive=False))
        for li in direct_lis:
            classes = li.get('class', [])
            class_str = ' '.join(classes) if isinstance(classes, list) else classes

            # Check for sidebar-title (section header without link) - Docusaurus custom theme element
            if 'sidebar-title' in class_str:
                title_span = li.find('span', class_='sidebar-title')
                if title_span:
                    title = title_span.get_text(strip=True)
                    if title:
                        nav_links.append((None, title, depth))
                        in_section = True  # Items after this should be indented
                continue

            # Skip if not a menu list item
            if 'menu__list-item' not in class_str:
                continue

            # Determine current item depth (indent if we're in a named section)
            current_depth = depth + 1 if in_section else depth

            # Check if this is a category (collapsible section)
            is_category = 'theme-doc-sidebar-item-category' in class_str or \
                          li.find(class_=re.compile(r'menu__link--sublist'))

            if is_category:
                # Extract category header
                category_link = li.find('a', class_=re.compile(r'menu__link--sublist|menu__link'))
                nested_list = li.find('ul', class_=re.compile(r'\bmenu__list\b'))
                has_nested = nested_list is not None

                if category_link:
                    title = category_link.get_text(strip=True)
                    href = category_link.get('href')

                    # Category might be a link itself or just a header
                    if href and href != '#' and not href.startswith('#'):
                        url = normalize_url(href, base_url)
                        if url and url not in processed_urls and not should_skip_url(url):
                            nav_links.append((url, title, current_depth))
                            processed_urls.add(url)
                        elif title and has_nested:
                            # URL already processed but has nested items - add as section header
                            # so nested items have their parent category in the TOC
                            nav_links.append((None, title, current_depth))
                    elif title:
                        # Non-link category header
                        nav_links.append((None, title, current_depth))

                # Process nested items
                if nested_list:
                    nav_links.extend(self._process_menu_list(nested_list, base_url, processed_urls, current_depth + 1))
            else:
                # Regular link item
                link = li.find('a', class_=re.compile(r'\bmenu__link\b'), href=True)
                if link:
                    url = normalize_url(link['href'], base_url)
                    if url and url not in processed_urls and not should_skip_url(url):
                        nav_links.append((url, link.get_text(strip=True), current_depth))
                        processed_urls.add(url)

        return nav_links


class ModernGitBookExtractor(NavExtractor):
    """Extractor for modern GitBook sites (Next.js-based with Tailwind CSS)."""

    def can_handle(self, soup: BeautifulSoup) -> bool:
        # Check for table-of-contents ID
        toc = soup.find(id="table-of-contents")
        if toc:
            return True

        # Check for data-testid attribute
        toc = soup.find(attrs={"data-testid": "table-of-contents"})
        if toc:
            return True

        # Check for toclink class (GitBook's link styling)
        toclink = soup.find(class_=re.compile(r'\btoclink\b'))
        if toclink:
            return True

        # Check for group/toclink pattern (Tailwind group variant)
        for elem in soup.find_all(class_=True):
            classes = elem.get('class', [])
            if isinstance(classes, list):
                if any('group/toclink' in c for c in classes):
                    return True

        return False

    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        nav_links = []

        # Find the table of contents container
        toc = soup.find(id="table-of-contents")
        if not toc:
            toc = soup.find(attrs={"data-testid": "table-of-contents"})
        if not toc:
            # Fall back to finding aside with toclink children
            for aside in soup.find_all('aside'):
                if aside.find(class_=re.compile(r'\btoclink\b')):
                    toc = aside
                    break

        if not toc:
            return nav_links

        # Process the TOC structure
        nav_links.extend(self._process_toc(toc, base_url, processed_urls, depth=0))

        return nav_links

    def _is_section_header(self, elem) -> bool:
        """Check if element is a section header based on styling classes."""
        classes = elem.get('class', [])
        if isinstance(classes, list):
            class_str = ' '.join(classes)
        else:
            class_str = str(classes)

        # Section headers typically have uppercase + tracking-wide + font-semibold
        header_indicators = ['uppercase', 'tracking-wide', 'font-semibold']
        matches = sum(1 for ind in header_indicators if ind in class_str)

        # Also check for sticky positioning (section headers are often sticky)
        if 'sticky' in class_str and matches >= 1:
            return True

        return matches >= 2

    def _process_toc(self, container, base_url: str, processed_urls: Set[str], depth: int) -> List[tuple]:
        nav_links = []

        # First, look for section headers (divs with section header styling)
        for child in container.children:
            if not hasattr(child, 'name') or child.name is None:
                continue

            # Check if this is a section header
            if child.name in ['div', 'span'] and self._is_section_header(child):
                title = child.get_text(strip=True)
                if title and len(title) > 1:
                    nav_links.append((None, title, depth))
                continue

            # Check if this is a list item containing a section header
            if child.name == 'li':
                header_elem = child.find(lambda tag: tag.name in ['div', 'span'] and self._is_section_header(tag))
                if header_elem:
                    title = header_elem.get_text(strip=True)
                    if title and len(title) > 1:
                        nav_links.append((None, title, depth))

                    # Process children of this section (links in nested ul/div)
                    for nested in child.find_all(['ul', 'div'], recursive=False):
                        if nested != header_elem:
                            nav_links.extend(self._process_toc(nested, base_url, processed_urls, depth + 1))
                    continue

                # Regular link item
                link = child.find('a', href=True, recursive=False)
                if not link:
                    link = child.find('a', href=True)

                if link:
                    classes = link.get('class', [])
                    class_str = ' '.join(classes) if isinstance(classes, list) else str(classes)

                    # Check for toclink class or that it's a navigation link
                    if 'toclink' in class_str or 'group/toclink' in class_str or link.find_parent(id="table-of-contents"):
                        url = normalize_url(link['href'], base_url)
                        if url and url not in processed_urls and not should_skip_url(url):
                            nav_links.append((url, link.get_text(strip=True), depth))
                            processed_urls.add(url)

            # Process nested ul elements
            elif child.name == 'ul':
                nav_links.extend(self._process_toc(child, base_url, processed_urls, depth))

            # Process nested divs that might contain more nav items
            elif child.name == 'div':
                # Check if this div contains toclinks
                if child.find(class_=re.compile(r'toclink')):
                    nav_links.extend(self._process_toc(child, base_url, processed_urls, depth))

        return nav_links


class FallbackExtractor(NavExtractor):
    """Fallback extractor that finds all same-domain links."""

    def can_handle(self, soup: BeautifulSoup) -> bool:
        return True  # Always can handle as fallback

    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        nav_links = []
        base_url_normalized = base_url.rstrip("/")
        base_path = urlparse(base_url_normalized).path.rstrip("/")

        for link in soup.find_all("a", href=True):
            url = normalize_url(link.get("href"), base_url)
            if not url or url in processed_urls or should_skip_url(url):
                continue

            # Only include links under base_url, exclude base_url itself
            if url == base_url_normalized or not url.startswith(base_url_normalized):
                continue

            link_text = link.get_text(strip=True)
            if link_text and len(link_text) > 1:  # Skip icons/separators
                # Skip navigation buttons (Previous/Next pagination links)
                if link_text.startswith("Previous") or link_text.startswith("Next"):
                    continue

                # Infer depth from URL path structure relative to base URL
                url_path = urlparse(url).path.rstrip("/")
                if base_path and url_path.startswith(base_path):
                    relative_path = url_path[len(base_path):].strip("/")
                else:
                    relative_path = url_path.strip("/")

                # Depth is number of path segments (e.g., /foo/bar = depth 1, /foo/bar/baz = depth 2)
                depth = len(relative_path.split("/")) - 1 if relative_path else 0
                depth = max(0, min(depth, 4))  # Clamp to reasonable range

                nav_links.append((url, link_text, depth))
                processed_urls.add(url)

        return nav_links


@dataclass
class DownloadStatus:
    top_level_pages: int = 0
    current_page: int = 0
    current_url: str = ""
    status: str = "idle"
    error: Optional[str] = None
    start_time: Optional[float] = None
    pages_scraped: List[str] = None
    output_file: Optional[str] = None
    rate_limit_reset: Optional[int] = None

    def __post_init__(self):
        if self.pages_scraped is None:
            self.pages_scraped = []

    def to_dict(self) -> Dict:
        return {
            "top_level_pages": self.top_level_pages,
            "current_page": self.current_page,
            "current_url": self.current_url,
            "status": self.status,
            "error": self.error,
            "elapsed_time": (
                round(datetime.now().timestamp() - self.start_time, 2)
                if self.start_time
                else 0
            ),
            "pages_scraped": self.pages_scraped,
            "output_file": self.output_file,
            "rate_limit_reset": self.rate_limit_reset,
        }


class GitbookDownloader:
    def __init__(self, url, native_md: bool, section_only: bool = False):
        # Preserve trailing slash so urljoin treats base_url as a directory
        # This prevents dropping path prefixes like /scf-handbook when joining relative URLs
        self.base_url = url.rstrip("/") + "/"
        self.native_md = native_md
        self.section_only = section_only
        # Extract section prefix for filtering when section_only is enabled
        if section_only:
            path = urlparse(url).path.rstrip("/")
            # Remove last segment (e.g., /Overview) to get section prefix
            self.section_prefix = "/".join(path.split("/")[:-1])
        else:
            self.section_prefix = None
        self.status = DownloadStatus()
        self.session = None
        self.visited_urls = set()
        self.delay = 1  # Delay between requests in seconds
        self.max_retries = 3
        self.retry_delay = 2  # Initial retry delay in seconds
        self.pages = {}  # Store page titles and content
        self.content_hash = {}  # Track content hashes
        self.has_global_nav = False  # True for sites like Mintlify where nav is identical on all pages
        self.nav_preserves_order = False  # True for extractors that produce reliable nav ordering
        self.sparse_nav = False  # True for sites with collapsed nav where sub-page section headers should be filtered
        # Navigation extractors in priority order
        self.extractors = [
            MintlifyExtractor(),
            VocsExtractor(),
            DocusaurusExtractor(),
            ModernGitBookExtractor(),
            GitBookExtractor(),
            FallbackExtractor()
        ]

    async def download(self):
        """Main download method"""
        try:
            self.status.start_time = time.time()
            self.status.status = "downloading"
            self.visited_urls = set()  # Track visited URLs

            # Create aiohttp session with timeout
            timeout = aiohttp.ClientTimeout(total=60, connect=10, sock_read=30)
            async with aiohttp.ClientSession(timeout=timeout) as self.session:
                # First get the main page
                initial_content = await self._fetch_page(self.base_url)
                if not initial_content:
                    raise Exception("Failed to fetch main page")

                # Extract navigation links
                nav_links = await self._extract_nav_links(initial_content)

                # For sites with global nav (Mintlify), nav_links includes main page with correct depth
                # For other sites, process main page separately
                if self.has_global_nav:
                    self.status.top_level_pages = len(nav_links)
                    await self._follow_nav_links(nav_links, page_index=0)
                else:
                    self.status.top_level_pages = len(nav_links) + 1  # +1 for main page
                    # Process main page
                    main_page = await self._process_page_content(
                        self.base_url, initial_content
                    )
                    if main_page:
                        self.pages[0] = {"index": 0, "depth": 0, **main_page}
                        self.status.pages_scraped.append(main_page["title"])
                        # Normalize URL (no trailing slash) for consistent visited_urls tracking
                        self.visited_urls.add(self.base_url.rstrip("/"))
                    # Process other pages
                    await self._follow_nav_links(nav_links, page_index=1)

                # Generate markdown
                markdown_content = self._generate_markdown()
                if not markdown_content:
                    raise Exception("Failed to generate markdown content")

                self.status.status = "completed"
                return markdown_content

        except Exception as e:
            self.status.status = "error"
            self.status.error = str(e)
            logger.error(f"Download failed: {str(e)}")
            raise

    async def _follow_nav_links(self, nav_links, page_index):
        for link, title, depth in nav_links:
            try:
                # Handle section headers (title-only, no URL)
                if link is None:
                    # Skip section headers when section_only is enabled
                    # (they may be from parent categories outside our target section)
                    if self.section_only:
                        continue
                    self.pages[page_index] = {
                        "index": page_index,
                        "depth": depth,
                        "title": title,
                        "content": None,  # No content for section headers
                        "url": None,
                    }
                    page_index += 1
                    continue

                # Skip if URL already processed, but update depth if found at different depth
                # (e.g., page first discovered via content link at depth 0, then found in nav at depth 1)
                if link in self.visited_urls:
                    # Find and update depth if current depth is more accurate (from nav extraction)
                    for page_idx, page_data in self.pages.items():
                        if page_data.get('url') == link and page_data.get('depth', 0) != depth:
                            # Prefer deeper depth from proper nav extraction over shallow depth from fallback
                            if depth > page_data.get('depth', 0):
                                self.pages[page_idx]['depth'] = depth
                            break
                    continue

                # Skip URLs from different version paths (e.g., /nightly/ when base is stable)
                # This prevents duplicating content from multiple doc versions
                if is_different_version_path(link, self.base_url):
                    continue

                # Skip URLs from different documentation sections (e.g., /operators/ when base is /developers/)
                # This prevents mixing content from unrelated doc sections
                if is_different_doc_section(link, self.base_url):
                    continue

                # Skip URLs outside section when section_only is enabled
                if self.section_only and self.section_prefix:
                    link_path = urlparse(link).path
                    if not link_path.startswith(self.section_prefix):
                        continue

                self.status.current_page = page_index
                self.status.current_url = link

                # Add delay between requests
                await asyncio.sleep(self.delay)

                content = await self._fetch_page(link)
                self.visited_urls.add(link)
                if content:
                    if self.native_md:
                        md_text = await self._fetch_page(f"{link}.md")
                        page_data = {"title": title, "content": md_text, "url": link}
                    else:
                        page_data = await self._process_page_content(link, content)
                    if page_data:
                        # Check for duplicate content using SHA256 for stable hashing
                        content_hash = hashlib.sha256(
                            page_data["content"].encode("utf-8")
                        ).hexdigest()
                        if content_hash not in self.content_hash:
                            # Use nav title if available (more reliable for TOC than page h1)
                            # e.g., Docusaurus category "Getting Started" vs page h1 "Quick Start"
                            effective_title = title if title else page_data["title"]
                            self.pages[page_index] = {
                                "index": page_index,
                                "depth": depth,
                                **page_data,
                                "title": effective_title,  # Override with nav title
                            }
                            self.status.pages_scraped.append(effective_title)
                            self.content_hash[content_hash] = page_index
                            page_index += 1

                            # Search for sub-nav links to handle sites with
                            # JS-rendered collapsible navigation (e.g., Vocs, Docusaurus)
                            # Skip for sites with global nav (e.g., Mintlify) since all pages have same sidebar
                            if not self.has_global_nav:
                                subnav_links = await self._extract_nav_links(content)
                                # For sites with sparse nav (collapsed sections), filter out section headers
                                # from sub-pages to avoid depth issues (sub-pages have local depths)
                                if self.sparse_nav:
                                    subnav_links = [(url, title, depth) for url, title, depth in subnav_links if url is not None]
                                page_index = await self._follow_nav_links(
                                    subnav_links, page_index
                                )

            except Exception as e:
                logger.error(f"Error processing page {link}: {str(e)}")
                continue

        return page_index

    async def _process_page_content(self, url, content):
        """Process the content of a page"""
        try:
            soup = BeautifulSoup(content, "html.parser")

            # Extract title
            title = None
            h1 = soup.find("h1")
            if h1:
                title = h1.get_text(strip=True)
            if not title:
                title_tag = soup.find("title")
                if title_tag:
                    # Clean up title - remove site name and extra parts
                    title = title_tag.get_text(strip=True)
                    title = re.split(r"[|\-–]", title)[0].strip()
            if not title:
                title = urlparse(url).path.split("/")[-1] or "Introduction"

            # Get main content - prefer more specific containers first
            # Look for article first (more specific), then main (less specific)
            main_content = soup.find("article")
            if not main_content:
                # Try content-area div (common in Mintlify sites)
                main_content = soup.find("div", {"id": "content-area"})
            if not main_content:
                main_content = soup.find("main")
            if not main_content:
                main_content = soup.find(
                    "div",
                    {"class": ["markdown", "content", "article", "documentation"]},
                )
            if not main_content:
                main_content = soup

            # Remove navigation elements
            for nav in main_content.find_all(["nav", "aside", "header", "footer"]):
                nav.decompose()

            # Remove sidebar elements by id (common patterns)
            for sidebar in main_content.find_all(id=re.compile(r"sidebar|nav|menu", re.I)):
                sidebar.decompose()

            # Remove scripts and styles
            for tag in main_content.find_all(["script", "style"]):
                tag.decompose()

            # Remove navigation links at bottom
            for link in main_content.find_all("a", text=re.compile(r"Previous|Next")):
                link.decompose()

            # Convert to markdown
            content_html = str(main_content)
            md = markdownify.markdownify(content_html, heading_style="atx")

            # Clean up markdown
            md = re.sub(r"\n{3,}", "\n\n", md)  # Remove extra newlines
            md = re.sub(r"#{3,}", "##", md)  # Normalize heading levels
            # Remove permalink anchor links like [​](#anchor) or [ ](#anchor)
            md = re.sub(r'\[[\s\u200b]*\]\(#[^)]+\)\s*', '', md)
            # Remove adjacent navigation links (prev/next) at end of content
            # Pattern: [text](url)[text](url) with no space between
            md = re.sub(r'\[([^\]]+)\]\(/[^)]*\)\[([^\]]+)\]\(/[^)]*\)\s*$', '', md, flags=re.MULTILINE)
            # Remove keyboard shortcut hints (⌘I, ⌃C, etc.)
            md = re.sub(r'[⌘⌃⌥⇧]+[A-Za-z]\s*', '', md)

            return {"title": title, "content": md, "url": url}

        except Exception as e:
            logger.error(f"Error processing page content: {str(e)}")
            return None

    def _get_page_sort_key(self, page):
        """Generate a sort key for a page based on URL structure.

        This groups pages by URL prefix and ensures:
        - Root page comes first
        - Top-level pages (single path segment) come second
        - Section-grouped pages come third, grouped by first segment
        - Section headers are placed at the start of their section
        """
        url = page.get("url")
        base_path = urlparse(self.base_url).path.strip("/")

        if url:
            parsed = urlparse(url)
            full_path = parsed.path.strip("/")

            # Get path relative to base URL
            if base_path and full_path.startswith(base_path):
                relative_path = full_path[len(base_path):].strip("/")
            else:
                relative_path = full_path

            segments = relative_path.split("/") if relative_path else []

            if not segments or not relative_path:
                # Root page: sort first
                return (0, 0, "", "", "")

            if len(segments) == 1:
                # Top-level page (e.g., /intro, /faq): sort after root, before sections
                return (1, 0, relative_path, "", "")

            # Nested page (e.g., /borg/foo): group by first segment
            first_segment = segments[0]
            # Sort key: (1=non-root, 1=nested, section_name, full_path, "")
            return (1, 1, first_segment, relative_path, "")
        else:
            # Section header (no URL) - try to place it before its section's pages
            title = page.get("title", "").lower()

            # Try to infer section from title (remove emojis and special chars)
            # e.g., "🤖 BORGs" -> "borgs", "Developer" -> "developer"
            clean_title = re.sub(r'[^\w\s]', '', title).strip().lower()
            words = clean_title.split()
            section_key = words[0] if words else ""

            # Section headers sort before their pages within the section group
            return (1, 1, section_key, "", title)

    def _generate_markdown(self):
        """Generate markdown content from downloaded pages"""
        if not self.pages:
            return ""

        markdown_parts = []
        seen_urls = set()  # Track URLs to avoid duplicate pages in TOC
        seen_section_headers = set()  # Track section header titles to avoid duplicates
        seen_titles = set()  # Track titles for content deduplication

        # Add table of contents
        markdown_parts.append("# Table of Contents\n")
        # For single-page docs, include h2 headings for richer ToC
        include_h2 = len(self.pages) == 1
        # For sites with reliable nav ordering, preserve extraction order for TOC
        # For other sites, sort by URL structure to group related pages
        if self.has_global_nav or self.nav_preserves_order:
            sorted_pages = sorted(self.pages.values(), key=lambda x: x["index"])
        else:
            sorted_pages = sorted(self.pages.values(), key=self._get_page_sort_key)

        # Pre-filter: identify section headers that have no items following them
        # A section header is "empty" if:
        # - When nav_preserves_order: next URL item is at same/shallower depth
        # - Always: there's another section header immediately following with no URL items between
        empty_header_indices = set()
        for i, page in enumerate(sorted_pages):
            if page.get("url") is None:  # Section header
                header_depth = page.get("depth", 0)
                has_children = False
                next_is_header = True  # Assume empty unless we find a URL item

                # Look ahead for items that belong to this section
                for j in range(i + 1, len(sorted_pages)):
                    next_page = sorted_pages[j]
                    next_depth = next_page.get("depth", 0)

                    if next_page.get("url") is None:
                        # Another section header
                        if next_depth <= header_depth:
                            # Sibling or parent level header - stop here
                            break
                        # Nested section header - continue looking
                        continue

                    # Found a URL item
                    next_is_header = False

                    if self.has_global_nav or self.nav_preserves_order:
                        # Strict depth checking when nav order is reliable
                        if next_depth > header_depth:
                            has_children = True
                            break
                        # Same or shallower depth - not our child
                        break
                    else:
                        # When using fallback, just finding any URL item means section has content
                        has_children = True
                        break

                # Empty if no children found (either next is header or strict depth check failed)
                if not has_children and next_is_header:
                    empty_header_indices.add(i)
                elif not has_children and (self.has_global_nav or self.nav_preserves_order):
                    empty_header_indices.add(i)

        for i, page in enumerate(sorted_pages):
            if page.get("title"):
                title = page["title"].strip()
                url = page.get("url")

                # Skip empty section headers
                if i in empty_header_indices:
                    continue

                # Section headers deduplicated by title; pages deduplicated by URL
                # This allows a page to have the same title as a section header
                if url is None:
                    if title in seen_section_headers:
                        continue
                    seen_section_headers.add(title)
                else:
                    if url in seen_urls:
                        continue
                    seen_urls.add(url)
                # Use depth for indentation (2 spaces per level)
                depth = page.get("depth", 0)
                indent = "  " * depth
                # Section headers (no URL) shown as bold text, pages as links
                if url is None:
                    markdown_parts.append(f"{indent}**{title}**")
                else:
                    markdown_parts.append(f"{indent}- [{title}](#{slugify(title)})")
                    # Extract h2 headings from content for sub-items
                    if include_h2 and page.get("content"):
                        h2_headings = re.findall(r'^## (.+)$', page["content"], re.MULTILINE)
                        current_section_depth = 0  # Track depth based on numbered sections
                        for h2 in h2_headings:
                            h2_clean = h2.strip()
                            if h2_clean:
                                # Determine depth from numbered prefix (e.g., "1" = depth 1, "1.1" = depth 2)
                                number_match = re.match(r'^(\d+(?:\.\d+)*)\s', h2_clean)
                                if number_match:
                                    number_parts = number_match.group(1).split('.')
                                    h2_depth = len(number_parts)  # "1" = 1, "1.1" = 2, "1.1.1" = 3
                                    current_section_depth = h2_depth
                                else:
                                    # Non-numbered heading: nest under current section
                                    h2_depth = current_section_depth + 1
                                h2_indent = "  " * h2_depth
                                markdown_parts.append(f"{h2_indent}- [{h2_clean}](#{slugify(h2_clean)})")

        markdown_parts.append("\n---\n")

        # Add content (use same sort order as TOC)
        seen_titles.clear()
        for page in sorted_pages:
            if page.get("title") and page.get("content"):
                title = page["title"].strip()
                content = page["content"].strip()

                if title and title not in seen_titles:
                    markdown_parts.append(f"\n# {title}")
                    markdown_parts.append(f"\nSource: {page['url']}\n")
                    markdown_parts.append(content)
                    markdown_parts.append("\n---\n")
                    seen_titles.add(title)

        return "\n".join(markdown_parts)

    async def _fetch_page(self, url):
        """Fetch a page with retry logic"""
        retry_count = 0
        current_delay = self.retry_delay
        logging.info(f"fetching {url}")

        while retry_count < self.max_retries:
            try:
                async with self.session.get(url) as response:
                    if response.status == 429:  # Rate limit
                        retry_after = response.headers.get("Retry-After", "60")
                        wait_time = int(retry_after)
                        self.status.rate_limit_reset = wait_time
                        logging.warning(f"Rate limited. Waiting {wait_time} seconds")
                        await asyncio.sleep(wait_time)
                        retry_count += 1
                        continue

                    if response.status == 200:
                        return await response.text()
                    else:
                        logging.warning(f"HTTP {response.status} for {url}")
                        return None

            except Exception as e:
                logging.error(f"Error fetching {url}: {str(e)}")
                if retry_count < self.max_retries - 1:
                    await asyncio.sleep(current_delay)
                    current_delay *= 2  # Exponential backoff
                    retry_count += 1
                else:
                    return None

        return None

    async def _extract_nav_links(self, content):
        """Extract navigation links using the first matching extractor."""
        try:
            soup = BeautifulSoup(content, "html.parser")
            processed_urls = set()

            for extractor in self.extractors:
                if extractor.can_handle(soup):
                    # Set flags based on extractor type:
                    # - has_global_nav: sidebar is identical on all pages (skip re-extraction)
                    # - nav_preserves_order: navigation order should be used for TOC sorting
                    if isinstance(extractor, MintlifyExtractor):
                        self.has_global_nav = True
                        self.nav_preserves_order = True
                    elif isinstance(extractor, (DocusaurusExtractor, ModernGitBookExtractor)):
                        # These extractors produce reliable nav ordering
                        self.nav_preserves_order = True
                    elif isinstance(extractor, VocsExtractor):
                        # VocsExtractor: check if sections are collapsed first before setting flag
                        pass  # Will be set below if nav is complete
                    nav_links = extractor.extract(soup, self.base_url, processed_urls)
                    if nav_links:
                        # For Vocs sites with collapsed sections, also extract content links
                        # to bootstrap into sections that aren't visible in the collapsed nav
                        if isinstance(extractor, VocsExtractor):
                            # Check if we have actual page URLs (not just section headers)
                            actual_pages = [link for link in nav_links if link[0] is not None]
                            section_headers = [link for link in nav_links if link[0] is None]
                            # If there are section headers but few pages, sections are likely collapsed
                            if section_headers and len(actual_pages) <= len(section_headers) + 3:
                                # Don't trust nav order when using fallback - use URL-based sorting
                                self.nav_preserves_order = False
                                # Mark nav as sparse so subnav extraction filters section headers
                                # (sub-pages have expanded sections with local depths that don't match global structure)
                                self.sparse_nav = True
                                fallback = FallbackExtractor()
                                content_links = fallback.extract(soup, self.base_url, processed_urls)
                                # Bump fallback depths by 1 since section headers are at depth 0
                                # and fallback items should nest under them
                                adjusted_links = [(url, title, depth + 1) for url, title, depth in content_links]
                                nav_links.extend(adjusted_links)
                            else:
                                # Nav is complete, preserve order
                                self.nav_preserves_order = True

                        # For Modern GitBook sites with client-rendered nav, also extract content links
                        # to find pages not visible in the static sidebar
                        if isinstance(extractor, ModernGitBookExtractor):
                            actual_pages = [link for link in nav_links if link[0] is not None]
                            # If we found fewer than 10 actual pages, supplement with content links
                            if len(actual_pages) < 10:
                                # Don't trust nav order when using fallback - use URL-based sorting
                                self.nav_preserves_order = False
                                fallback = FallbackExtractor()
                                content_links = fallback.extract(soup, self.base_url, processed_urls)
                                nav_links.extend(content_links)

                        # Deduplicate while preserving order
                        seen = set()
                        return [
                            item for item in nav_links
                            if item[0] is None or (item[0] not in seen and not seen.add(item[0]))
                        ]

            return []

        except Exception as e:
            logger.error(f"Error extracting nav links: {str(e)}")
            return []
