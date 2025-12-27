import requests
from bs4 import BeautifulSoup, Comment
import json
from urllib.parse import urljoin, urlparse
import re
from slugify import slugify
import os
import logging
from typing import Dict, Optional, List, Set
from dataclasses import dataclass
from datetime import datetime
import markdownify
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import time
import hashlib

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)





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
    def __init__(self, url, native_md: bool):
        # Preserve trailing slash so urljoin treats base_url as a directory
        # This prevents dropping path prefixes like /scf-handbook when joining relative URLs
        self.base_url = url.rstrip("/") + "/"
        self.native_md = native_md
        self.status = DownloadStatus()
        self.session = None
        self.visited_urls = set()
        self.delay = 1  # Delay between requests in seconds
        self.max_retries = 3
        self.retry_delay = 2  # Initial retry delay in seconds
        self.pages = {}  # Store page titles and content
        self.content_hash = {}  # Track content hashes
        self.has_global_nav = False  # True for sites like Mintlify where nav is identical on all pages

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
                    self.pages[page_index] = {
                        "index": page_index,
                        "depth": depth,
                        "title": title,
                        "content": None,  # No content for section headers
                        "url": None,
                    }
                    page_index += 1
                    continue

                # Skip if URL already processed
                if link in self.visited_urls:
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
                            self.pages[page_index] = {
                                "index": page_index,
                                "depth": depth,
                                **page_data,
                            }
                            self.status.pages_scraped.append(page_data["title"])
                            self.content_hash[content_hash] = page_index
                            page_index += 1

                            # Search for sub-nav links to handle sites with
                            # JS-rendered collapsible navigation (e.g., Vocs, Docusaurus)
                            # Skip for sites with global nav (e.g., Mintlify) since all pages have same sidebar
                            if not self.has_global_nav:
                                subnav_links = await self._extract_nav_links(content)
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

    def _generate_markdown(self):
        """Generate markdown content from downloaded pages"""
        if not self.pages:
            return ""

        markdown_parts = []
        seen_titles = set()

        # Add table of contents
        markdown_parts.append("# Table of Contents\n")
        # For single-page docs, include h2 headings for richer ToC
        include_h2 = len(self.pages) == 1
        for page in sorted(self.pages.values(), key=lambda x: x["index"]):
            if page.get("title"):
                title = page["title"].strip()
                if title and title not in seen_titles:
                    # Use depth for indentation (2 spaces per level)
                    depth = page.get("depth", 0)
                    indent = "  " * depth
                    # Section headers (no URL) shown as bold text, pages as links
                    if page.get("url") is None:
                        markdown_parts.append(f"{indent}**{title}**")
                    else:
                        markdown_parts.append(f"{indent}- [{title}](#{slugify(title)})")
                    seen_titles.add(title)
                    # Extract h2 headings from content for sub-items
                    if include_h2 and page.get("content"):
                        h2_headings = re.findall(r'^## (.+)$', page["content"], re.MULTILINE)
                        for h2 in h2_headings:
                            h2_clean = h2.strip()
                            if h2_clean:
                                markdown_parts.append(f"  - [{h2_clean}](#{slugify(h2_clean)})")

        markdown_parts.append("\n---\n")

        # Add content
        seen_titles.clear()
        for page in sorted(self.pages.values(), key=lambda x: x["index"]):
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
        logging.info(f"fetching {url}")  # TODO: remove

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

    def _process_nav_list(self, nav_list, processed_urls, depth=0):
        """Recursively process navigation list items, tracking depth for hierarchy."""
        nav_links = []
        for li in nav_list.find_all("li", recursive=False):
            link = li.find("a", href=True)
            if link:
                href = link["href"]
                # Skip fragment-only links
                if href.startswith("#"):
                    continue
                # Use urlparse/urljoin so relative paths that already include
                # the base path are handled correctly (no double prefix).
                parsed_href = urlparse(href)
                if not parsed_href.netloc:
                    full_url = urljoin(self.base_url, href)
                elif href.startswith(self.base_url):
                    full_url = href
                else:
                    continue

                # Skip duplicate URLs, strip fragments, and normalize trailing slashes
                url_without_fragment = full_url.split("#", 1)[0].rstrip("/")
                if url_without_fragment not in processed_urls:
                    nav_links.append((url_without_fragment, link.get_text(), depth))
                    processed_urls.add(url_without_fragment)

            # Process nested lists (children of this li)
            nested_lists = li.find_all(["ol", "ul"], recursive=False)
            for nested_list in nested_lists:
                nav_links.extend(self._process_nav_list(nested_list, processed_urls, depth + 1))

        return nav_links

    async def _extract_nav_links(self, content):
        """Extract navigation links from GitBook page content with hierarchy depth."""
        try:
            soup = BeautifulSoup(content, "html.parser")
            nav_links = []
            processed_urls = set()

            # Check for Mintlify-style navigation (sidebar-group pattern)
            navigation_items = soup.find(id="navigation-items")
            if navigation_items:
                # Mintlify sites have identical nav on all pages - skip recursive extraction
                self.has_global_nav = True
                # Process Mintlify sidebar structure
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
                                # Add section header as title-only entry (URL=None)
                                nav_links.append((None, section_title, 0))
                        # Get links in this section
                        sidebar_group = child.find(class_="sidebar-group") or child.find("ul")
                        if sidebar_group:
                            nav_links.extend(self._process_nav_list(sidebar_group, processed_urls, depth=1))
                    elif child.name == "ul":
                        # Top-level list (external links like MetaDAO, API Docs)
                        nav_links.extend(self._process_nav_list(child, processed_urls, depth=0))

            # Find GitBook navigation elements (traditional structure)
            if not nav_links:
                nav_elements = soup.find_all(["nav", "aside"])
                for nav in nav_elements:
                    # Look for top-level lists that typically contain the navigation
                    nav_lists = nav.find_all(["ol", "ul"], recursive=False)
                    if not nav_lists:
                        # If no direct child lists, find any lists
                        nav_lists = nav.find_all(["ol", "ul"])
                    for nav_list in nav_lists:
                        nav_links.extend(self._process_nav_list(nav_list, processed_urls, depth=0))

            # Also check for next/prev navigation links (these are always depth 0)
            next_links = soup.find_all(
                "a", {"aria-label": ["Next", "Previous", "next", "previous"]}
            )
            for link in next_links:
                href = link.get("href")
                if href:
                    parsed_href = urlparse(href)
                    if not parsed_href.netloc:
                        full_url = urljoin(self.base_url, href)
                    elif href.startswith(self.base_url):
                        full_url = href
                    else:
                        continue

                    # Skip fragment-only links, strip fragments, and normalize trailing slashes
                    url_without_fragment = full_url.split("#", 1)[0].rstrip("/")
                    if url_without_fragment not in processed_urls and not href.startswith("#"):
                        nav_links.append((url_without_fragment, link.get_text(), 0))
                        processed_urls.add(url_without_fragment)

            # Fallback: If no nav links found in nav/aside, look for documentation links
            # This handles sites like Mintlify that don't use traditional nav structures
            if not nav_links:
                # For initial navigation extraction, search the whole page (not just main content)
                # because navigation is often in header/sidebar elements
                # Find all links that point to other pages on the same domain
                all_links = soup.find_all("a", href=True)
                for link in all_links:
                    href = link.get("href")
                    if href and not href.startswith("#"):
                        parsed_href = urlparse(href)
                        if not parsed_href.netloc:
                            full_url = urljoin(self.base_url, href)
                        elif href.startswith(self.base_url):
                            full_url = href
                        else:
                            continue

                        # Only include links that are different from the base URL and look like doc pages
                        # Strip fragment and normalize trailing slashes
                        url_without_fragment = full_url.split("#", 1)[0].rstrip("/")
                        base_url_normalized = self.base_url.rstrip("/")
                        # Skip fragment-only links or links that only differ by fragment from base URL
                        if full_url.startswith("#") or url_without_fragment == base_url_normalized:
                            continue
                        if (url_without_fragment not in processed_urls and
                            url_without_fragment.startswith(base_url_normalized) and
                            not any(skip in url_without_fragment for skip in ["mailto:", "tel:", ".pdf", ".jpg", ".png", ".gif", ".svg", "api-docs"])):
                            link_text = link.get_text(strip=True)
                            # Only include links with meaningful text (not empty, not just icons)
                            # Filter out very short text that's likely just icons or separators
                            if link_text and len(link_text.strip()) > 1:
                                # Fallback links have no hierarchy info, use depth 0
                                nav_links.append((url_without_fragment, link_text.strip(), 0))
                                processed_urls.add(url_without_fragment)

            # Remove duplicates while preserving order (use url as key since tuples now have 3 elements)
            # Section headers (url=None) are never duplicates - they have unique titles
            seen_urls = set()
            unique_links = []
            for item in nav_links:
                url = item[0]
                if url is None:
                    # Section headers - always keep (they have unique titles)
                    unique_links.append(item)
                elif url not in seen_urls:
                    seen_urls.add(url)
                    unique_links.append(item)
            return unique_links

        except Exception as e:
            logger.error(f"Error extracting nav links: {str(e)}")
            return []
