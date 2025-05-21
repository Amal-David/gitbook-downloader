# Documentation Downloader

A powerful web application that downloads and converts online documentation into markdown format.

## Supported Platforms

The application now supports several common documentation platforms including:

-   GitBook
-   Docusaurus
-   ReadMe.com
-   MkDocs
-   Sphinx
-   Mintlify

While the scrapers have been designed to handle typical structures for these platforms, the accuracy of the downloaded content can vary based on specific site customizations and complex JavaScript-driven content. The application attempts to automatically detect the platform and use the appropriate scraper. If no specific scraper can handle the site, the download will not proceed for that URL.

## Features

-   Support for multiple documentation platforms (GitBook, Docusaurus, ReadMe.com, MkDocs, Sphinx, Mintlify).
-   Modular scraper design for easier extension to other platforms.
-   Asynchronous downloading for improved performance.
-   Real-time progress tracking via API endpoints.
-   Clean markdown conversion with preserved formatting.
-   Interactive web interface with:
    -   URL submission for downloads.
    -   Real-time progress updates (status, pages processed, errors).
    -   Download link for the final Markdown file.
-   Handles rate limiting and retries during page fetching.
-   **Enhanced Download Diagnostics**: Provides detailed operational logs and a count of failed pages during the download process, accessible via the status API, aiding in troubleshooting.

## Installation

1.  Clone this repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure `requirements.txt` includes `Flask`, `aiohttp`, `BeautifulSoup4`, `markdownify`, `python-slugify`, `requests`)

## Usage

1.  Start the web server:
    ```bash
    python app.py
    ```

2.  Open your browser and navigate to `http://localhost:8080` (or the configured port).

3.  Enter the URL of a documentation site from the supported platforms.

4.  Click "Submit" to start the download process.

5.  Monitor real-time progress and metrics via the status API endpoint (e.g., `/status/<task_id>`).

6.  When complete, you can:
    -   View the converted content by accessing the result API endpoint (e.g., `/result/<task_id>`).
    -   Download the markdown file via the download API endpoint (e.g., `/download/<task_id>/markdown`).

## Technical Details

### Architecture

The application follows a modular architecture:

-   **Frontend & Task Management (`app.py`)**: A Flask-based web application that handles user requests, initiates download tasks in background threads, and provides API endpoints for status, results, and file downloads.
-   **Core Download Engine (`DocumentationDownloader`)**: This central class orchestrates the entire download process for a given URL. It manages:
    -   Asynchronous page fetching using `aiohttp`.
    -   Retry mechanisms for failed requests.
    -   Rate limit awareness.
    -   Overall download status tracking (e.g., pages processed, errors, logs) via the `DownloadStatus` dataclass.
    -   Delegation to a scraper instance for platform-specific logic.
-   **Scraper Abstraction (`scrapers/base_scraper.py::BaseScraper`)**: An abstract base class defining the contract for all platform-specific scrapers. It requires methods for identifying compatible sites (`can_handle`), extracting navigation links (`extract_navigation_links`), and processing individual page content into Markdown (`extract_page_data`).
-   **Platform-Specific Scrapers (e.g., `scrapers/gitbook_scraper.py::GitbookScraper`)**: Concrete classes that inherit from `BaseScraper`. Each is tailored to a specific documentation platform, implementing the logic to:
    -   Parse navigation structures from the site's main page.
    -   Extract, clean, and convert the main content of each documentation page into Markdown.
-   **Scraper Selection (`scrapers/scraper_factory.py::ScraperFactory`)**: This factory class takes the initial HTML soup of a target URL and its domain to determine which available scraper class (if any) can handle it. If no suitable scraper is found, it returns `None`, and the download process for that URL is typically halted.

### Key Components

-   Flask web application (`app.py`) with API endpoints.
-   Generic `DocumentationDownloader` class for download orchestration.
-   Abstract `BaseScraper` class defining the scraper interface.
-   Concrete scraper implementations (e.g., `GitbookScraper`, `DocusaurusScraper`, `MintlifyScraper`, etc.).
-   `ScraperFactory` for dynamic, content-aware scraper selection.
-   `DownloadStatus` dataclass for detailed, per-task progress and error/log reporting.
-   Asynchronous HTTP requests via `aiohttp`.
-   HTML parsing with `BeautifulSoup4`.
-   HTML to Markdown conversion using `markdownify`.
-   Filename sanitization using `slugify`.

### Metrics Tracked (via `DownloadStatus` and logs)

-   Total pages identified for download.
-   Number of successfully scraped pages.
-   Number of failed pages.
-   Current page being processed.
-   Overall status (initializing, downloading, completed, error).
-   Specific error messages.
-   Operational log messages.
-   Output filename.
-   Rate limit reset timings (if encountered).

## Contributing

Contributions are welcome, especially in the following areas:
1.  **Adding Support for New Documentation Platforms**: Creating new scraper classes that implement the `BaseScraper` interface.
2.  Improving existing scrapers and Markdown conversion quality.
3.  Enhancing the UI/UX of the Flask web frontend.
4.  Adding new features or more robust error handling and recovery.

## Note

While the framework is in place for multiple platforms, the reliability can vary based on individual site structures and customizations. Always check the application logs and the status API for detailed information on the download process.
