import asyncio
import aiohttp
import logging
import time
from contextlib import contextmanager
from typing import Dict, Optional, List, Set, Tuple, Any
from dataclasses import dataclass, field
from datetime import datetime
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import markdownify
from slugify import slugify
import re

# Assuming PageContent is in scrapers.base_scraper
# We will need to adjust this if it's moved or structured differently later
from scrapers.base_scraper import BaseScraper, PageContent

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
        
        timeout_task = asyncio.create_task(check_timeout())
        yield
    except TimeoutError as e:
        raise e
    finally:
        if 'timeout_task' in locals() and not timeout_task.done():
            timeout_task.cancel()

@dataclass
class DownloadStatus:
    total_pages: int = 0
    current_page: int = 0
    current_url: str = ""
    status: str = "idle"  # idle, downloading, completed, error
    error: Optional[str] = None
    start_time: Optional[float] = None
    pages_scraped_titles: List[str] = field(default_factory=list) # Store titles of scraped pages
    output_file: Optional[str] = None
    rate_limit_reset: Optional[int] = None
    failed_pages_count: int = 0
    log_messages: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        elapsed_time = 0
        if self.start_time:
            elapsed_time = round(time.time() - self.start_time, 2)
        
        return {
            "total_pages": self.total_pages,
            "current_page": self.current_page,
            "current_url": self.current_url,
            "status": self.status,
            "error": self.error,
            "elapsed_time": elapsed_time,
            "pages_scraped_titles": self.pages_scraped_titles,
            "output_file": self.output_file,
            "rate_limit_reset": self.rate_limit_reset,
            "failed_pages_count": self.failed_pages_count,
            "log_messages": self.log_messages
        }

class DocumentationDownloader:
    def __init__(self, base_url: str, scraper_instance: BaseScraper):
        self.base_url = base_url.rstrip('/')
        self.scraper_instance = scraper_instance
        
        self.status = DownloadStatus()
        self.session: Optional[aiohttp.ClientSession] = None # Will be created in download
        self.output_file: Optional[str] = None
        self.visited_urls: Set[str] = set()
        self.delay: int = 1  # Delay between requests in seconds
        self.max_retries: int = 3
        self.retry_delay: int = 2  # Initial retry delay in seconds
        
        # pages will store PageContent objects, keyed by URL or a unique ID
        self.pages: Dict[str, PageContent] = {} 
        self.content_hash: Dict[int, str] = {}  # Track content hashes to avoid duplicates

    async def _fetch_page(self, url: str) -> Optional[str]:
        """Fetch a page with retry logic, rate limit handling, etc."""
        retry_count = 0
        current_delay = self.retry_delay
        
        # Ensure session is initialized
        if not self.session or self.session.closed:
            log_msg = "aiohttp.ClientSession not initialized or closed."
            logger.error(log_msg)
            # Cannot add to self.status.log_messages if self.status is not guaranteed to be initialized
            # This case should ideally not happen if _fetch_page is only called from download()
            return None

        while retry_count < self.max_retries:
            try:
                logger.debug(f"Fetching URL: {url}")
                async with self.session.get(url) as response:
                    if response.status == 429:  # Rate limit
                        retry_after_header = response.headers.get('Retry-After', str(self.retry_delay * (2**retry_count)))
                        try:
                            wait_time = int(retry_after_header)
                        except ValueError:
                            wait_time = self.retry_delay * (2**retry_count) # Default backoff
                        
                        self.status.rate_limit_reset = int(time.time() + wait_time)
                        logger.warning(f"Rate limited. Waiting {wait_time} seconds. Retry-After: {retry_after_header}")
                        await asyncio.sleep(wait_time)
                        # Don't increment retry_count for 429 if Retry-After is present,
                        # as the server explicitly tells us when to try again.
                        # However, to prevent infinite loops if server keeps sending 429,
                        # we might still want to limit retries or use a different counter.
                        # For now, let's increment to ensure eventual exit.
                        retry_count +=1 
                        continue # Retry the same request
                        
                    response.raise_for_status() # Raise HTTPError for bad responses (4XX or 5XX)
                    
                    # Check content type to avoid downloading non-HTML content by mistake
                    content_type = response.headers.get('Content-Type', '').lower()
                    if 'text/html' not in content_type:
                        log_msg = f"Skipping non-HTML content at {url} (Content-Type: {content_type})"
                        logger.warning(log_msg)
                        self.status.log_messages.append(log_msg)
                        return None
                        
                    return await response.text()
                        
            except aiohttp.ClientResponseError as e:
                log_msg = f"HTTP {e.status} for {url}: {e.message}"
                logger.warning(log_msg)
                self.status.log_messages.append(log_msg)
                if e.status in [403, 404]: # Don't retry for these errors
                    return None
                # For other client errors, retry
            except aiohttp.ClientError as e: # More generic client error
                log_msg = f"ClientError fetching {url}: {str(e)}"
                logger.error(log_msg)
                self.status.log_messages.append(log_msg)
            except asyncio.TimeoutError: # Specific timeout from session.get if configured
                log_msg = f"Timeout fetching {url}"
                logger.error(log_msg)
                self.status.log_messages.append(log_msg)
            except Exception as e: # Catch other unexpected errors
                log_msg = f"Unexpected error fetching {url}: {str(e)}"
                logger.error(log_msg, exc_info=True)
                self.status.log_messages.append(log_msg)

            # If we reach here, it's an error that warrants a retry
            retry_count += 1
            if retry_count < self.max_retries:
                log_msg = f"Retrying {url} in {current_delay}s (attempt {retry_count}/{self.max_retries})"
                logger.info(log_msg)
                # self.status.log_messages.append(log_msg) # Optional: too verbose?
                await asyncio.sleep(current_delay)
                current_delay *= 2  # Exponential backoff
            else:
                log_msg = f"Max retries reached for {url}. Giving up."
                logger.error(log_msg)
                self.status.log_messages.append(log_msg)
                return None
        
        return None # Should be unreachable if max_retries leads to None

    async def download(self):
        """Main download method using the provided scraper instance."""
        self.status.start_time = time.time()
        self.status.status = "downloading"
        self.status.failed_pages_count = 0 # Initialize
        self.status.log_messages = [] # Initialize
        self.visited_urls.clear()
        self.pages.clear()
        self.content_hash.clear()
        
        page_index = 0 # Tracks successfully processed pages for self.pages dict keying if needed

        try:
            async with aiohttp.ClientSession() as session:
                self.session = session # Assign session for _fetch_page

                # Step 1: Fetch the initial page content for the scraper to get navigation links
                # The scraper_instance was already initialized with the soup of the base_url by ScraperFactory
                # So, self.scraper_instance.soup is the soup of self.base_url
                
                # Step 2: Extract navigation links using the scraper
                logger.info(f"Extracting navigation links using {type(self.scraper_instance).__name__}")
                try:
                    nav_links_metadata: List[Tuple[str, Dict[str, Any]]] = self.scraper_instance.extract_navigation_links()
                except Exception as e:
                    log_msg = f"Error extracting navigation links: {str(e)}"
                    logger.error(log_msg, exc_info=True)
                    self.status.log_messages.append(log_msg)
                    self.status.status = "error"
                    self.status.error = log_msg
                    raise Exception(log_msg) # Abort download

                if not nav_links_metadata:
                    log_msg = f"No navigation links found by the scraper for {self.base_url}."
                    logger.warning(log_msg)
                    self.status.log_messages.append(log_msg)
                    
                    # Attempt to process base_url as a single page
                    logger.info(f"Attempting to process base_url {self.base_url} as a single page.")
                    try:
                        base_page_data = self.scraper_instance.extract_page_data(self.scraper_instance.soup, self.base_url)
                        if base_page_data and base_page_data.content:
                            self.pages[self.base_url] = base_page_data
                            self.status.pages_scraped_titles.append(base_page_data.title)
                            self.status.total_pages = 1
                            page_index += 1
                            logger.info(f"Successfully processed base_url as a single page: {base_page_data.title}")
                        else:
                            log_msg_base = "Failed to extract content from base_url as a single page, and no navigation links found."
                            logger.error(log_msg_base)
                            self.status.log_messages.append(log_msg_base)
                            self.status.status = "error"
                            self.status.error = log_msg_base
                            raise Exception(log_msg_base) # Abort download
                    except Exception as e:
                        log_msg_base_exc = f"Error processing base_url as single page: {str(e)}"
                        logger.error(log_msg_base_exc, exc_info=True)
                        self.status.log_messages.append(log_msg_base_exc)
                        self.status.status = "error"
                        self.status.error = log_msg_base_exc
                        raise Exception(log_msg_base_exc) # Abort download
                else:
                    self.status.total_pages = len(nav_links_metadata)
                    logger.info(f"Found {self.status.total_pages} potential pages to scrape.")

                    # Also process the base_url itself as a page if it's not explicitly in nav_links
                    # Some scrapers might include it, others might not.
                    # We use extract_page_data which should give us a PageContent object.
                    if self.base_url not in [link_url for link_url, _ in nav_links_metadata]:
                        logger.info(f"Processing base URL {self.base_url} separately as it's not in nav_links.")
                        try:
                            base_page_content_obj = self.scraper_instance.extract_page_data(self.scraper_instance.soup, self.base_url)
                            if base_page_content_obj and base_page_content_obj.content:
                                content_md_hash = hash(base_page_content_obj.content)
                                if content_md_hash not in self.content_hash:
                                    self.pages[self.base_url] = base_page_content_obj
                                    self.status.pages_scraped_titles.append(base_page_content_obj.title)
                                    self.content_hash[content_md_hash] = self.base_url
                                    self.visited_urls.add(self.base_url)
                                    page_index +=1
                                else:
                                    logger.info(f"Content of base URL {self.base_url} is a duplicate. Skipping.")
                            else:
                                logger.warning(f"No content extracted from base URL {self.base_url} by the scraper, or content was empty.")
                                # Not necessarily a failed page if base_url is just a redirector or container
                        except Exception as e:
                            log_msg = f"Error processing base URL {self.base_url} separately: {str(e)}"
                            logger.error(log_msg, exc_info=True)
                            self.status.log_messages.append(log_msg)
                            self.status.failed_pages_count += 1


                # Step 3: Loop through navigation links and process each page
                for i, (link_url, metadata) in enumerate(nav_links_metadata):
                    self.status.current_page = i + 1 
                    self.status.current_url = link_url
                    
                    if link_url in self.visited_urls:
                        logger.info(f"Skipping already visited/processed URL: {link_url}")
                        continue

                    logger.info(f"Processing page {self.status.current_page}/{self.status.total_pages}: {link_url}")
                    
                    await asyncio.sleep(self.delay)
                    
                    page_html_content = await self._fetch_page(link_url)
                    self.visited_urls.add(link_url) # Mark as visited even if fetch fails to avoid retrying in this run

                    if not page_html_content:
                        log_msg = f"Failed to fetch content for {link_url}. See previous logs for details."
                        # _fetch_page already logs specifics and adds to self.status.log_messages
                        # logger.warning(log_msg) # Redundant if _fetch_page logged it
                        # self.status.log_messages.append(log_msg)
                        self.status.failed_pages_count += 1
                        continue

                    try:
                        page_soup = BeautifulSoup(page_html_content, 'html.parser')
                        page_content_obj = self.scraper_instance.extract_page_data(page_soup, link_url)

                        if page_content_obj and page_content_obj.content:
                            content_md_hash = hash(page_content_obj.content)
                            if content_md_hash not in self.content_hash:
                                self.pages[link_url] = page_content_obj
                                self.status.pages_scraped_titles.append(page_content_obj.title)
                                self.content_hash[content_md_hash] = link_url
                                page_index += 1
                            else:
                                logger.info(f"Duplicate content detected for {link_url} (hash: {content_md_hash}), originally from {self.content_hash[content_md_hash]}. Skipping.")
                        else:
                            log_msg = f"No content extracted by scraper for {link_url}, or content was empty."
                            logger.warning(log_msg)
                            self.status.log_messages.append(log_msg)
                            self.status.failed_pages_count += 1
                    except Exception as e:
                        log_msg = f"Error processing page data for {link_url}: {str(e)}"
                        logger.error(log_msg, exc_info=True)
                        self.status.log_messages.append(log_msg)
                        self.status.failed_pages_count += 1
                        continue # Continue to the next page

                # Step 4: Generate final markdown output
                if not self.pages:
                    final_error_msg = "No pages were successfully scraped."
                    logger.error(final_error_msg)
                    self.status.log_messages.append(final_error_msg)
                    self.status.status = "error"
                    self.status.error = final_error_msg
                    raise Exception(final_error_msg)
                
                markdown_output = self._generate_markdown()
                self.status.status = "completed"
                
                final_log_msg = f"Download completed. Successfully scraped: {len(self.pages)} pages. Failed pages: {self.status.failed_pages_count}."
                logger.info(final_log_msg)
                self.status.log_messages.append(final_log_msg)
                if self.status.failed_pages_count > 0:
                    self.status.error = f"Completed with {self.status.failed_pages_count} failed page(s). Check logs." # Set error if some pages failed
                return markdown_output

        except aiohttp.ClientError as e:
            self.status.status = "error"
            self.status.error = f"HTTP Client Error: {str(e)}"
            logger.error(self.status.error, exc_info=True)
            raise
        except TimeoutError as e: # From our custom timeout
            self.status.status = "error"
            self.status.error = str(e)
            logger.error(self.status.error, exc_info=True)
            raise
        except Exception as e:
            self.status.status = "error"
            self.status.error = f"An unexpected error occurred: {str(e)}"
            logger.error(self.status.error, exc_info=True)
            raise
        finally:
            if self.session and not self.session.closed:
                await self.session.close()
            self.status.start_time = None # Clear start time or calculate total duration

    def _generate_markdown(self) -> str:
        """Generates markdown from self.pages, respecting order, sections, and ToC."""
        if not self.pages:
            return ""

        markdown_parts = []
        
        # Sort pages: This is crucial. PageContent should have order, section fields.
        # We assume PageContent objects are stored in self.pages.values()
        # The sorting key might need adjustment based on PageContent structure
        sorted_pages = sorted(
            self.pages.values(),
            key=lambda p: (p.section or "", p.subsection or "", p.order or 0, p.title or "")
        )

        # Add Table of Contents
        markdown_parts.append("# Table of Contents\n")
        toc_entries = {} # Using dict to avoid duplicate titles in ToC from different sections leading to same slug

        for page in sorted_pages:
            if page.title:
                # Create a unique slug for ToC linking, considering sections for uniqueness if titles repeat
                slug_prefix = slugify(page.section) if page.section else ""
                slug_title = slugify(page.title)
                full_slug = f"{slug_prefix}-{slug_title}" if slug_prefix else slug_title
                
                entry = f"- [{page.section} - {page.title}](#{full_slug})" if page.section else f"- [{page.title}](#{full_slug})"
                
                # Indent subsections in ToC
                if page.subsection:
                    entry = f"  {entry}" # Simple indentation
                
                if full_slug not in toc_entries:
                    toc_entries[full_slug] = entry
        
        markdown_parts.extend(list(toc_entries.values()))
        markdown_parts.append("\n---\n")

        # Add Content
        processed_titles_for_content = set() # To avoid writing content for the same title multiple times if slugs clash

        for page in sorted_pages:
            if page.title and page.content:
                # Use the same slugging logic for headers as for ToC
                slug_prefix = slugify(page.section) if page.section else ""
                slug_title = slugify(page.title)
                full_slug = f"{slug_prefix}-{slug_title}" if slug_prefix else slug_title

                # Ensure we only add content for a unique title/slug once
                if full_slug not in processed_titles_for_content:
                    if page.section:
                        markdown_parts.append(f"\n## {page.section} - {page.title}") # Use H2 for combined section/title
                    else:
                        markdown_parts.append(f"\n## {page.title}") # Use H2 for title
                    
                    # Add subsection if it exists and is different from title
                    if page.subsection and page.subsection != page.title:
                         markdown_parts.append(f"\n### {page.subsection}")


                    markdown_parts.append(f"\n_Source: {page.url}_")
                    markdown_parts.append(f"\n{page.content.strip()}")
                    markdown_parts.append("\n---\n")
                    processed_titles_for_content.add(full_slug)
        
        return "\n".join(markdown_parts)

    # Helper to convert HTML to Markdown, could be part of scraper or downloader
    def _html_to_markdown(self, html_content: str, base_url_for_links: Optional[str] = None) -> str:
        """Converts HTML to Markdown using markdownify."""
        if not html_content:
            return ""
        
        # Configure markdownify options if needed, e.g., to handle images, code blocks
        # In markdownify, relative links are preserved. If absolute links are needed:
        # md = markdownify.markdownify(html_content, heading_style="atx", base_url=base_url_for_links)
        md = markdownify.markdownify(html_content, heading_style="atx")
        
        # Basic post-processing (optional, can be enhanced)
        md = md.replace('```\n\n```', '```\n```') # Fix potential extra newlines in empty code blocks
        md = re.sub(r'\n{3,}', '\n\n', md).strip() # Remove excessive newlines
        return md

"""
**Note on `_html_to_markdown`**:
The `PageContent.content` returned by `scraper_instance.extract_page_data` is *already expected to be markdown* as per the prompt for the `BaseScraper` changes later ("`PageContent` would include title, `markdown_content`, order, section etc.").
So, the `DocumentationDownloader` should not call `_html_to_markdown` itself on `page_content_obj.content`.
If `extract_page_data` in a specific scraper implementation returns HTML that needs conversion, that scraper's `extract_page_data` method should handle the conversion to Markdown before populating the `PageContent.content` field.
"""
