# GitBook Downloader Test & Fix Prompt

## Task Overview

Run `test.py` to download all documentation sites, then verify that:
1. **Table of Contents (TOC)** - Proper order, indentation, and no missing pages
2. **Content Quality** - Each page's content is human-readable and LLM-readable

Fix any extractor issues found and re-run tests iteratively until everything works properly.

## How to Execute

```bash
poetry run python test.py
```

This creates a `tests-N/` folder (incrementing N) with markdown files for each documentation site.

## Reference Screenshots

Screenshots of expected sidebar/TOC structure are in `test-screenshots/`:
- `zamm-docs.png` - ZAMM (Vocs)
- `gmtribe-docs.png` - GMTribe (Modern GitBook)
- `metadao-docs.png` - MetaDAO (Mintlify)
- `metalex-docs.png` - MetaLeX (Vocs)
- `aztec-docs.png` - Aztec (Docusaurus)
- `noir-docs.png` - Noir (Docusaurus)
- `zama-protocol-docs.png` - Zama Protocol (Modern GitBook)
- `zama-solidity-docs.png` - Zama Solidity (Modern GitBook)

Note: Some screenshots may not show fully expanded navigation or all categories.

## Codebase Structure

### Key Files
- `gitbook_downloader.py` - Main module with all extractors and download logic
- `test.py` - Test runner with list of documentation URLs
- `cli.py` - CLI entry point

### Extractor Classes (in priority order)
| Extractor | Lines | Target Sites |
|-----------|-------|--------------|
| `MintlifyExtractor` | ~78-110 | Mintlify docs (MetaDAO) |
| `VocsExtractor` | ~144-222 | Vocs docs (ZAMM, MetaLeX) |
| `DocusaurusExtractor` | ~225-319 | Docusaurus v2/v3 (Aztec, Noir) |
| `ModernGitBookExtractor` | ~322-445 | Next.js GitBook (GMTribe, Zama) |
| `GitBookExtractor` | ~113-141 | Legacy GitBook |
| `FallbackExtractor` | ~448-500 | Content link extraction fallback |

### Important Flags
- `has_global_nav` - True for sites where sidebar is identical on all pages (skip re-extraction)
- `nav_preserves_order` - True when extraction order should be used for TOC sorting (vs URL-based sorting)

### Key Methods
- `_extract_nav_links()` - Selects extractor and extracts navigation structure
- `_follow_nav_links()` - Fetches pages and recursively extracts sub-navigation
- `_generate_markdown()` - Generates final markdown with TOC and content
- `_get_page_sort_key()` - URL-based sorting for sites without reliable nav order

## Verification Checklist

### 1. TOC Verification (compare against screenshots)

For each generated markdown file, verify:

- [ ] **Order** - Items appear in same order as sidebar screenshot
- [ ] **Indentation** - Hierarchy levels match (sections at depth 0, items at depth 1, sub-items at depth 2, etc.)
- [ ] **Section Headers** - Section names appear as `**Bold Text**` without links
- [ ] **Page Links** - Pages appear as `- [Title](#anchor)` with proper indentation
- [ ] **Completeness** - All visible navigation items from screenshot are present
- [ ] **No Duplicates** - No repeated entries (except section header + same-titled page is OK)

### 2. Content Verification

For each page in the markdown, verify:

- [ ] **Human Readable**
  - Clean prose without HTML artifacts or escaped characters
  - Proper markdown formatting (headers, lists, code blocks, links)
  - No broken or malformed markdown syntax
  - Images referenced with proper markdown syntax (even if not downloadable)

- [ ] **LLM Readable**
  - Clear section boundaries with `# Title` headers
  - Source URL included after each title: `Source: https://...`
  - Content separated by `---` dividers
  - No excessive whitespace or formatting noise
  - Code blocks properly fenced with language hints where applicable
  - Tables formatted in markdown (not HTML)

- [ ] **Content Integrity**
  - Main content extracted (not just navigation/footer)
  - No truncated or missing sections
  - Technical content (code examples, API references) preserved accurately

### 3. Common Issues to Watch For

| Issue | Symptom | Likely Cause |
|-------|---------|--------------|
| Missing pages | TOC shorter than screenshot | Collapsed sections not expanded, client-rendered nav |
| Wrong nesting | Items at wrong depth | Incorrect depth tracking in extractor |
| Missing section headers | No bold headers in TOC | Categories with URLs treated as links, not headers |
| Duplicate entries | Same item appears twice | Deduplication tracking by wrong key |
| Wrong titles | Page title differs from nav | Using page `<h1>` instead of nav link text |
| Items under wrong section | Grouped incorrectly | URL-based sorting needed but not enabled |
| HTML in content | Raw `<div>`, `<span>` tags | Content extraction not using proper selectors |
| Broken markdown | Malformed syntax | Edge cases in content conversion |

## Iteration Process

1. **Run tests**: `poetry run python test.py`
2. **Compare TOCs**: Check each `tests-N/*.md` file against corresponding screenshot
3. **Check content**: Read through content sections for readability issues
4. **Identify extractor**: Determine which extractor handles the problematic site
5. **Debug extraction**: Add logging or test specific URLs in isolation
6. **Fix code**: Edit `gitbook_downloader.py`
7. **Re-test**: Run test.py again (can test subset if only one extractor changed)
8. **Repeat**: Until all sites pass verification

## Testing Individual Sites

To test a single site without running all:

```python
from gitbook_downloader import GitbookDownloader
import asyncio

async def test():
    downloader = GitbookDownloader('https://example.com/docs/', False)
    md = await downloader.download()
    print(md[:5000])  # Preview output

asyncio.run(test())
```

## Success Criteria

All 8 documentation sites should:
1. Have TOC structure matching their sidebar screenshots
2. Have all pages downloaded with readable content
3. Be usable as context for an LLM without preprocessing
4. Be readable by a human reviewing the documentation offline

## Known Limitations

These are inherent limitations of static HTML extraction that may not be fully fixable:

### 1. Collapsed Navigation (Docusaurus, Vocs)
- **Symptom**: Nav link titles missing or different from sidebar
- **Cause**: JavaScript-rendered collapsed sections aren't in static HTML
- **Workaround**: Pages are fetched via content links, but title comes from page H1 instead of nav link text
- **Example**: Noir's "Quick Start" page fetched but may appear with different title

### 2. Client-Rendered Navigation (Modern GitBook)
- **Symptom**: Items appear at end of TOC instead of logical position
- **Cause**: Navigation rendered client-side; items discovered late in crawl
- **Workaround**: Items have correct depth but ordering follows discovery order
- **Example**: Zama Protocol's "FHE library" appears at end instead of under "FHE on blockchain"

### 3. Section Entry Pages
- **Symptom**: Section entry page at same depth as section header
- **Cause**: URL `/section` has same depth as `/section/item` minus 1
- **Workaround**: Depth adjustment applied when fallback supplements nav extraction

### 4. Version Path Filtering
- **Symptom**: Some version-specific pages skipped
- **Cause**: Extractor filters paths like `/nightly/`, `/next/` to avoid duplicates
- **Workaround**: Start from specific version URL if needed
