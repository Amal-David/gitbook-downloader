# Gitbook Documentation Downloader for LLMs

> 📢 **Announcement:** [docingest](https://github.com/Amal-David/docingest) is now open source! It's a comprehensive documentation ingestion engine that supports **Gitbook, ReadTheDocs, Mintlify, Docusaurus**, and many more providers — a full successor to this tool. ⭐ [Star it on GitHub](https://github.com/Amal-David/docingest) if you find it useful.

A web application that converts Gitbook documentation into markdown format, optimized for use with coding agents and AI assistants like Claude Code, Codex, Hermes, Pi, and others.

> ℹ️ **Looking for broader support?** Check out [docingest](https://github.com/Amal-David/docingest) (also hosted at [docingest.com](https://docingest.com)) for a more comprehensive engine supporting ReadTheDocs, Mintlify, Docusaurus, and others. This Gitbook-specific tool may still be preferable for pure Gitbook sites.

## Purpose

- Download technical documentation for use with coding agents
- Create knowledge bases for Claude Code, Codex, Hermes, Pi, and other AI assistants
- Feed documentation into context windows of AI chatbots
- Generate markdown files optimized for LLM processing

## Features

- Scrape Gitbook documentation sites
- Convert HTML content to LLM-friendly markdown format
- View converted content in browser
- Download documentation as a single markdown file
- Handles internal links and navigation
- Preserves document structure

## Installation

1. Clone this repository
2. Install dependencies:
```bash
poetry install
```

## Usage

### Using Web Interface
1. Start the web server:
```bash
poetry run python app.py
```

2. Open your browser and navigate to `http://localhost:8080`

3. Enter the URL of a Gitbook documentation site

4. Choose to either:
   - View the converted content in your browser
   - Download the content as a markdown file

5. Use the downloaded markdown with:
   - Claude Code (drop into your project or paste into context)
   - Codex (use as reference material)
   - Hermes (include in your knowledge base)
   - Pi (paste into conversation)
   - Any other LLM or coding agent that accepts markdown input

### Using CLI Tool

You can use CLI to download the documentation as well:
```bash
poetry run python cli.py download <gitbook_url> --output <output_file.md>
```

## Technical Details

The application uses:
- Flask for the web interface
- BeautifulSoup4 for HTML parsing
- Requests for fetching web content
- Python-slugify for URL/filename handling

## Note

This tool is designed specifically for Gitbook-based documentation sites and optimized for LLM consumption. It may not work correctly with other documentation platforms.
