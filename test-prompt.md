# GitBook Downloader Test & Fix Prompt

## Prerequisites

**Before starting, read the README.md file entirely** to understand:
- Supported platforms and their extractors
- Features and architecture
- Known limitations and their causes
- How to add new extractors

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

**Use your vision/multimodal capabilities** to view and analyze these screenshots in `test-screenshots/`. Compare the generated TOC against each screenshot to verify structure:

| Screenshot | Site | Extractor |
|------------|------|-----------|
| `zamm-docs.png` | ZAMM | VocsExtractor |
| `gmtribe-docs.png` | GMTribe | ModernGitBookExtractor |
| `metadao-docs.png` | MetaDAO | MintlifyExtractor |
| `metalex-docs.png` | MetaLeX | VocsExtractor |
| `aztec-docs.png` | Aztec | DocusaurusExtractor |
| `noir-docs.png` | Noir | DocusaurusExtractor |
| `zama-protocol-docs.png` | Zama Protocol | ModernGitBookExtractor |
| `zama-solidity-docs.png` | Zama Solidity | ModernGitBookExtractor |

Note: Some screenshots may not show fully expanded navigation or all categories.

## Example Correct Output

### TOC Format Example

A correctly formatted TOC should look like this:

```markdown
## Table of Contents

**Getting Started**
  - [Introduction](#introduction)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Quick Start](#quick-start)
  - [Configuration](#configuration)
**Core Concepts**
  - [Architecture](#architecture)
  - [Components](#components)
```

Key formatting rules:
- Section headers: `**Bold Text**` at depth 0, no link
- Page links: `- [Title](#anchor)` with 2-space indentation per depth level
- Sub-items: Additional 2-space indent under parent

### Content Format Example

Each page should be formatted as:

```markdown
---

# Page Title

Source: https://example.com/docs/page-name

Main content here with proper markdown formatting...

## Subheading

More content...

```python
code_example = "properly fenced"
```

---
```

## Codebase Structure

### Key Files
- `gitbook_downloader.py` - Main module with all extractors and download logic
- `test.py` - Test runner with list of documentation URLs
- `cli.py` - CLI entry point

### Extractor Classes (in priority order)

| Extractor | Target Sites | Key Method | Detection |
|-----------|--------------|------------|-----------|
| `MintlifyExtractor` | Mintlify (MetaDAO) | `extract_links()` | `mintlify` in scripts |
| `VocsExtractor` | Vocs (ZAMM, MetaLeX) | `extract_links()` | `vocs` sidebar class |
| `DocusaurusExtractor` | Docusaurus (Aztec, Noir) | `extract_links()` | `docusaurus` meta tag |
| `ModernGitBookExtractor` | Next.js GitBook (GMTribe, Zama) | `extract_links()` | `gitbook-` classes |
| `GitBookExtractor` | Legacy GitBook | `extract_links()` | `.book-summary` element |
| `FallbackExtractor` | Any (last resort) | `extract_links()` | Always matches |

To find an extractor in code: `grep -n "class MintlifyExtractor" gitbook_downloader.py`

### Important Flags
- `has_global_nav` - True for sites where sidebar is identical on all pages (skip re-extraction)
- `nav_preserves_order` - True when extraction order should be used for TOC sorting (vs URL-based sorting)

### Key Methods
- `_extract_nav_links()` - Selects extractor and extracts navigation structure
- `_follow_nav_links()` - Fetches pages and recursively extracts sub-navigation
- `_generate_markdown()` - Generates final markdown with TOC and content
- `_get_page_sort_key()` - URL-based sorting for sites without reliable nav order

### URL Filtering Functions
- `normalize_url()` - Converts relative URLs to absolute, strips fragments
- `should_skip_url()` - Filters mailto:, images, PDFs, api-docs
- `is_different_version_path()` - Detects version paths like `/nightly/`, `/next/`
- `is_different_doc_section()` - Detects different doc sections like `/developers/` vs `/operators/`

## Verification Checklist

### Tier 1: Blocking Issues (must fix)

- [ ] **TOC Order** - Items appear in same order as sidebar screenshot
- [ ] **No Missing Pages** - All visible navigation items from screenshot are present
- [ ] **Content Extracted** - Pages have actual content, not just navigation/footer

### Tier 2: Important Issues (should fix)

- [ ] **Correct Indentation** - Hierarchy levels match (depth 0, 1, 2, etc.)
- [ ] **No Duplicates** - No repeated entries (except section header + same-titled page is OK)
- [ ] **Clean Content** - No HTML artifacts (`<div>`, `<span>`) or escaped characters
- [ ] **Proper Markdown** - Headers, lists, code blocks formatted correctly

### Tier 3: Polish (fix if time permits)

- [ ] **Section Headers** - Section names appear as `**Bold Text**` without links
- [ ] **Source URLs** - Each page has `Source: https://...` after title
- [ ] **Code Fencing** - Code blocks have language hints (```python, ```js)
- [ ] **Table Formatting** - Tables in markdown, not HTML

### Common Issues Reference

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

## Handling Failures

### Network/Site Issues

| Issue | How to Detect | Action |
|-------|---------------|--------|
| Site down | Connection refused, 5xx errors | Skip site, note in output, don't count as extractor bug |
| Rate limited | 429 errors, connection throttled | Add delays between requests or retry later |
| Timeout | Requests hanging >60s | Check if site has excessive pages (>500), may need pagination |
| SSL errors | Certificate verification failed | Check if site URL changed or cert expired |

### When to Stop Trying

- **Stop fixing** if you've spent >30 minutes on a single issue without progress
- **Document as limitation** if the issue is inherent to static HTML extraction (JS-rendered content)
- **Ask for help** if the fix requires architectural changes to the extractor system

### Partial Success is OK

A site can pass verification even with minor issues:
- A few pages with slightly different titles (H1 vs nav text) - acceptable
- Missing deeply nested items from collapsed JS menus - document as limitation
- Extra pages from related sections - acceptable if core content is correct

## Iteration Process

1. **Run tests**: `poetry run python test.py`
2. **Compare TOCs**: Use vision to compare each `tests-N/*.md` file against corresponding screenshot
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

    # Preview just the TOC
    toc_end = md.find('\n---\n')
    print("=== TOC ===")
    print(md[:toc_end])

    # Preview first page content
    print("\n=== FIRST PAGE ===")
    print(md[toc_end:toc_end+2000])

asyncio.run(test())
```

## Success Criteria

All 8 documentation sites should:
1. Have TOC structure matching their sidebar screenshots (Tier 1 issues resolved)
2. Have all pages downloaded with readable content
3. Be usable as context for an LLM without preprocessing
4. Be readable by a human reviewing the documentation offline

## Known Limitations

These are inherent limitations of static HTML extraction that may not be fully fixable:

### 1. Collapsed Navigation (Docusaurus, Vocs)
- **Symptom**: Nav items missing from TOC or with different titles
- **Cause**: JavaScript-rendered collapsed sections aren't in static HTML
- **Workaround**: Pages are fetched via content links, title comes from page H1
- **Example**: Noir's "Quick Start" under "Getting Started" may be missing because the section is collapsed

### 2. Client-Rendered Navigation (Modern GitBook)
- **Symptom**: Items discovered late may appear at end of TOC
- **Cause**: Navigation rendered client-side; static HTML has incomplete sidebar
- **Workaround**: When fewer than 10 items found, fallback extraction supplements with URL-based sorting
- **Example**: Zama Protocol's FHE sub-items now correctly grouped using URL-based sorting

### 3. Multiple Sidebar Sections (Docusaurus)
- **Symptom**: TOC includes items from unrelated documentation areas
- **Cause**: Docusaurus sites with multiple "docs plugins" show all in sidebar
- **Workaround**: Start from a more specific URL (e.g., `/developers/` instead of root)
- **Example**: Aztec docs include both developer docs and node operator sections (Setup, Operation)

### 4. Vocs Depth Inconsistency
- **Symptom**: Expandable items at different depth than non-expandable siblings
- **Cause**: Different HTML structure for expandable vs non-expandable items
- **Workaround**: None currently - inherent to Vocs HTML structure
- **Example**: MetaLeX "BORGs OS" (expandable) at depth 2, "Borg Auth" (non-expandable) at depth 1

### 5. Version Path Filtering
- **Symptom**: Some version-specific pages skipped
- **Cause**: Extractor filters paths like `/nightly/`, `/next/`, `/canary/`
- **Workaround**: Start from specific version URL if needed

### 6. Doc Section Filtering
- **Symptom**: Pages from other doc sections not crawled
- **Cause**: Extractor prevents crawling into different sections (e.g., `/solidity-guides/` from `/protocol/`)
- **Workaround**: Start from the specific section URL you want to download

## Final Steps: Update Documentation

### 1. Update README.md

After completing all testing and fixes, **update README.md** if you discovered:
- New known limitations not documented
- Changes to extractor behavior
- New workarounds or fixes
- Architecture changes

This ensures the documentation stays current for future contributors.

### 2. Update This Prompt File (test-prompt.md)

**Critical**: Before finishing, review and update this prompt file itself with essential information that would help future runs be more effective:

| What to Update | When to Update |
|----------------|----------------|
| **Extractor table** | If you added a new extractor class or changed detection logic |
| **Test site list** | If `test.py` URLs changed or new sites were added |
| **Screenshot list** | If new reference screenshots were added to `test-screenshots/` |
| **Known limitations** | If you discovered new inherent limitations |
| **Example output** | If the output format changed |

Focus on updating the current information in the prompt file, not adding new information, since the coding agent will already have enough updated information from the README.md file.

**Why this matters**: This prompt file is used by coding agents to understand the task. Outdated information causes agents to waste time or make incorrect assumptions. Keeping this file accurate improves the success rate of future automated runs.
