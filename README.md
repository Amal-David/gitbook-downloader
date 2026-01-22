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
| **VocsExtractor** | Vocs docs (e.g., metalex-docs.vercel.app, docs.zamm.eth.limo) | `class="vocs_Sidebar_navigation"` |
| **DocusaurusExtractor** | Docusaurus v2/v3 (e.g., docs.aztec.network, noir-lang.org) | `class="menu__list"` + `class="menu__link"` |
| **ModernGitBookExtractor** | Next.js GitBook (e.g., gmtribe.gitbook.io, docs.zama.org) | `id="table-of-contents"` or `class="toclink"` |
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
- **Doc section filtering**: Prevents crawling into unrelated documentation areas (e.g., stays in `/developers/` without crawling `/operators/`)
- **Version path filtering**: Avoids duplicating content from multiple doc versions (e.g., `/nightly/`, `/next/`)

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

#### Downloading a specific section

Use the `--section-only` / `-s` flag to download only pages within a specific documentation section:
```bash
poetry run python cli.py download "https://docs.uniswap.org/contracts/liquidity-launchpad/Overview" --section-only -o liquidity-launchpad.md
```

This restricts crawling to URLs sharing the same path prefix as the starting URL (e.g., `/contracts/liquidity-launchpad/`), useful for downloading just one section of a large documentation site.

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

### Test Sites

| Site | Extractor | URL |
|------|-----------|-----|
| ZAMM | VocsExtractor | docs.zamm.eth.limo |
| GMTribe | ModernGitBookExtractor | gmtribe.gitbook.io |
| MetaDAO | MintlifyExtractor | docs.metadao.fi |
| MetaLeX | VocsExtractor | metalex-docs.vercel.app |
| Aztec | DocusaurusExtractor | docs.aztec.network |
| Noir | DocusaurusExtractor | noir-lang.org/docs |
| Zama Protocol | ModernGitBookExtractor | docs.zama.org/protocol |
| Zama Solidity | ModernGitBookExtractor | docs.zama.org/protocol/solidity-guides |

## Development & Debugging

For coding agents and contributors working on extractor improvements:

| Resource | Purpose |
|----------|---------|
| `test.py` | Automated test runner that downloads 8 reference documentation sites |
| `test-prompt.md` | Structured prompt for coding agents with verification checklist and debugging workflow |
| `test-screenshots/` | Reference screenshots of expected sidebar/TOC structure for each test site |

### Workflow for Fixing Extractors

1. Run `poetry run python test.py` to generate test output
2. Compare generated `tests-N/*.md` files against screenshots in `test-screenshots/`
3. Use `test-prompt.md` as a guide for systematic verification
4. Fix issues in `gitbook_downloader.py` and re-run tests

## Known Limitations

### Collapsed Navigation (Docusaurus, Vocs)
Sites with JavaScript-rendered collapsed navigation may not capture all nav items in the static HTML. The extractor recursively crawls pages to discover content, but:
- Nav link titles may differ from page H1 headings
- Items like "Quick Start" under collapsed "Getting Started" sections may be missing from TOC
- **Example**: Noir docs missing "Quick Start" because it's in a collapsed Docusaurus category

### Client-Rendered Navigation (Modern GitBook)
Modern GitBook sites render navigation client-side. When the static sidebar has fewer than 10 items, the extractor supplements with content links and uses URL-based sorting to group related pages.
- **Example**: Zama Protocol's FHE sub-items (library, host contracts, etc.) are correctly grouped under "FHE on blockchain" using URL-based sorting

### Multiple Sidebar Sections (Docusaurus)
Docusaurus sites with multiple "docs plugins" (e.g., developer docs + operator docs) may include items from all sidebars in the initial extraction.
- **Example**: Aztec docs include both developer docs and node operator sections (Setup, Operation) from the same sidebar
- **Workaround**: Start from a more specific URL like `/developers/` instead of the root

### Vocs Expandable vs Non-Expandable Items
Vocs sites may have inconsistent depth for expandable items (with children) vs non-expandable items (simple links) due to different HTML structures.
- **Example**: MetaLeX "BORGs OS" (expandable) may appear at different depth than "Borg Auth" (non-expandable)

### Version Path Filtering
The extractor filters paths like `/nightly/`, `/next/`, `/canary/` to avoid duplicating content from multiple doc versions. Some version-specific content may be skipped.

### Doc Section Filtering
The extractor filters URLs that go into different documentation sections (e.g., `/solidity-guides/` when starting from `/protocol/`). Recognized section prefixes include: `developers`, `operators`, `nodes`, `guides`, `tutorials`, `api`, `reference`, `solidity-guides`, `relayer-sdk-guides`, `examples`.

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
│   ├── MintlifyExtractor      - Mintlify documentation sites
│   ├── VocsExtractor          - Vocs documentation sites
│   ├── DocusaurusExtractor    - Docusaurus v2/v3 sites
│   ├── ModernGitBookExtractor - Next.js GitBook sites
│   ├── GitBookExtractor       - Traditional GitBook sites
│   └── FallbackExtractor      - Generic fallback for any site
├── _extract_nav_links()   - Runs extractors in priority order
├── _follow_nav_links()    - Recursively processes navigation
├── _process_page_content() - Extracts and cleans page content
└── _generate_markdown()   - Produces final markdown output
```
