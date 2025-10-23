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
from contextlib import contextmanager

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@contextmanager
def timeout(seconds=0, minutes=0, hours=0):
    """
    Add a signal-based timeout to any function.
    Usage:
    with timeout(seconds=5):
        my_slow_function(...)
    Args:
    - seconds: The time limit, in seconds.
    - minutes: The time limit, in minutes.
    - hours: The time limit, in hours.
    """
    limit = seconds + 60 * minutes + 3600 * hours
    try:

        async def check_timeout():
            await asyncio.sleep(limit)
            raise TimeoutError("timed out after {} seconds".format(limit))

        asyncio.create_task(check_timeout())
        yield
    except TimeoutError as e:
        raise e
    finally:
        asyncio.create_task(check_timeout()).cancel()


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
    def __init__(self, url, recursive: bool):
        self.base_url = url.rstrip("/")
        self.recursive = recursive
        self.status = DownloadStatus()
        self.session = None
        self.visited_urls = set()
        self.delay = 1  # Delay between requests in seconds
        self.max_retries = 3
        self.retry_delay = 2  # Initial retry delay in seconds
        self.pages = {}  # Store page titles and content
        self.content_hash = {}  # Track content hashes

    async def download(self):
        """Main download method"""
        try:
            self.status.start_time = time.time()
            self.status.status = "downloading"
            self.visited_urls = set()  # Track visited URLs

            # Create aiohttp session
            async with aiohttp.ClientSession() as self.session:
                # First get the main page
                initial_content = await self._fetch_page(self.base_url)
                if not initial_content:
                    raise Exception("Failed to fetch main page")

                # Extract navigation links
                nav_links = await self._extract_nav_links(initial_content)
                self.status.top_level_pages = len(nav_links) + 1  # +1 for main page

                # Process main page
                main_page = await self._process_page_content(
                    self.base_url, initial_content
                )
                if main_page:
                    self.pages[0] = {"index": 0, **main_page}
                    self.status.pages_scraped.append(main_page["title"])
                    self.visited_urls.add(self.base_url)

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
        for link in nav_links:
            try:
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
                    page_data = await self._process_page_content(link, content)
                    if page_data:
                        # Check for duplicate content
                        content_hash = hash(page_data["content"])
                        if content_hash not in self.content_hash:
                            self.pages[page_index] = {
                                "index": page_index,
                                **page_data,
                            }
                            self.status.pages_scraped.append(page_data["title"])
                            self.content_hash[content_hash] = page_index
                            page_index += 1

                            # Search for sub-nav links (only if new content)
                            if self.recursive:
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

            # Get main content
            main_content = soup.find(["main", "article"])
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
        for page in sorted(self.pages.values(), key=lambda x: x["index"]):
            if page.get("title"):
                title = page["title"].strip()
                if title and title not in seen_titles:
                    markdown_parts.append(f"- [{title}](#{slugify(title)})")
                    seen_titles.add(title)

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

    async def _extract_nav_links(self, content):
        """Extract navigation links from GitBook page content"""
        try:
            soup = BeautifulSoup(content, "html.parser")
            nav_links = []
            processed_urls = set()

            # Find GitBook navigation elements
            nav_elements = soup.find_all(["nav", "aside"])
            for nav in nav_elements:
                # Look for ordered lists that typically contain the navigation
                nav_lists = nav.find_all(["ol", "ul"])
                for nav_list in nav_lists:
                    # Process list items in order
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

                            # Skip duplicate URLs and fragments
                            if full_url not in processed_urls:
                                nav_links.append(full_url)
                                processed_urls.add(full_url)

            # Also check for next/prev navigation links
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

                    if full_url not in processed_urls and not href.startswith("#"):
                        nav_links.append(full_url)
                        processed_urls.add(full_url)

            # Remove duplicates while preserving order
            return list(dict.fromkeys(nav_links))

        except Exception as e:
            logger.error(f"Error extracting nav links: {str(e)}")
            return []
