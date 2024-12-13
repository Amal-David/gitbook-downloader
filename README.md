# Documentation Downloader

A powerful web application that downloads and converts online documentation into markdown format, supporting multiple documentation platforms.

## Supported Platforms

- GitBook
- Docusaurus
- ReadMe.com
- MkDocs
- Sphinx

The application automatically detects the documentation platform and uses the appropriate scraper.

## Features

- Multi-platform documentation support with automatic detection
- Asynchronous downloading for improved performance
- Real-time progress tracking
- Clean markdown conversion with preserved formatting
- Interactive web interface with:
  - Submit and Download buttons
  - Real-time progress updates
  - Detailed download metrics
  - Copy to clipboard functionality
- Handles rate limiting and retries
- Preserves document structure and navigation
- Support for internal links and cross-references

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the web server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:8082`

3. Enter the URL of any supported documentation site

4. Click "Submit" to start the download process

5. Monitor real-time progress and metrics

6. When complete, you can:
   - View the converted content in your browser
   - Copy content to clipboard
   - Download as a markdown file

## Technical Details

### Architecture
- Flask for the web interface
- BeautifulSoup4 for HTML parsing
- Async support with aiohttp for concurrent downloads
- Object-oriented design with platform-specific scrapers
- Factory pattern for scraper selection

### Key Components
- Platform-specific scraper classes
- Async download manager
- Progress tracking system
- Markdown conversion pipeline
- Real-time metrics collection

### Metrics Tracked
- Total pages processed
- Successful downloads
- Failed attempts
- Retry counts
- Download duration
- Average time per page
- Total content size

## Contributing

Feel free to contribute by:
1. Adding support for new documentation platforms
2. Improving existing scrapers
3. Enhancing the UI/UX
4. Adding new features

## Note

While the tool works best with the supported platforms (GitBook, Docusaurus, ReadMe.com, MkDocs, Sphinx), it includes fallback mechanisms for handling other documentation sites. The application automatically selects the most appropriate scraper based on the site's structure and characteristics.
