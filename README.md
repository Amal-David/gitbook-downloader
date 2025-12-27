# Documentation Downloader for LLMs

A tool that converts documentation sites into markdown format, optimized for use with Large Language Models (LLMs) like ChatGPT, Claude, and LLaMA.

## Purpose

- Download technical documentation for training custom LLMs
- Create knowledge bases for ChatGPT, Claude, and other AI assistants
- Feed documentation into context windows of AI chatbots
- Generate markdown files optimized for LLM processing

## Supported Platforms

The downloader uses a **plugin-based architecture** with specialized extractors for different documentation platforms:

| Extractor | Platforms | Detection |
|-----------|-----------|-----------|
| **MintlifyExtractor** | Mintlify docs (e.g., docs.metadao.fi) | `id="navigation-items"` |
| **VocsExtractor** | Vocs docs (e.g., metalex-docs.vercel.app) | `class="vocs_Sidebar_navigation"` |
| **GitBookExtractor** | Traditional GitBook sites | `nav`/`aside` with `ul`/`ol` lists |
| **FallbackExtractor** | Any site | Extracts all same-domain links |

Extractors are tried in priority order, and the first one that matches handles the site.

## Features

- **Multi-platform support**: Automatically detects and handles different documentation frameworks
- **Hierarchical navigation**: Preserves document structure with proper depth/indentation
- **Smart content extraction**: Removes navigation, sidebars, and boilerplate; keeps main content
- **Table of Contents generation**: Creates navigable TOC from extracted pages
- **Duplicate detection**: Content hashing prevents duplicate pages
- **Rate limiting**: Built-in delays and retry logic with exponential backoff

## Installation

1. Clone this repository
2. Install dependencies:
```bash
poetry install
```

## Usage

### Using CLI Tool

Download documentation to a markdown file:
```bash
poetry run python cli.py download <url> --output <output_file.md>
```

Example:
```bash
poetry run python cli.py download https://docs.example.com/ -o docs.md
```

### Using Web Interface

1. Start the web server:
```bash
poetry run python app.py
```

2. Open your browser and navigate to `http://localhost:8080`

3. Enter the URL of a documentation site

4. Choose to either:
   - View the converted content in your browser
   - Download the content as a markdown file

5. Use the downloaded markdown with:
   - ChatGPT (paste into conversation)
   - Claude (upload as a file)
   - Custom LLaMA models (include in training data)
   - Any other LLM that accepts markdown input

## Testing

Run the test script to verify the downloader works with multiple sites:
```bash
poetry run python test.py
```

This creates a `tests-N` folder with downloaded documentation from several test sites.

## Adding New Extractors

To support a new documentation platform, create a class that extends `NavExtractor`:

```python
class MyExtractor(NavExtractor):
    def can_handle(self, soup: BeautifulSoup) -> bool:
        # Return True if this extractor can handle the page
        return soup.find(class_="my-nav-class") is not None

    def extract(self, soup: BeautifulSoup, base_url: str, processed_urls: Set[str]) -> List[tuple]:
        # Return list of (url, title, depth) tuples
        # url can be None for section headers
        nav_links = []
        # ... extraction logic ...
        return nav_links
```

Then add it to the `extractors` list in `GitbookDownloader.__init__()`.

## Technical Details

The application uses:
- **aiohttp** for async HTTP requests
- **BeautifulSoup4** for HTML parsing
- **markdownify** for HTML to markdown conversion
- **Flask** for the web interface
- **python-slugify** for URL/filename handling

## Architecture

```
GitbookDownloader
├── NavExtractor (ABC)
│   ├── MintlifyExtractor  - Mintlify documentation sites
│   ├── VocsExtractor      - Vocs documentation sites
│   ├── GitBookExtractor   - Traditional GitBook sites
│   └── FallbackExtractor  - Generic fallback for any site
├── _extract_nav_links()   - Runs extractors in priority order
├── _follow_nav_links()    - Recursively processes navigation
├── _process_page_content() - Extracts and cleans page content
└── _generate_markdown()   - Produces final markdown output
```
