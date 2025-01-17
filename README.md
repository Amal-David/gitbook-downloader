# Gitbook Documentation Downloader for LLMs

A web application that converts Gitbook documentation into markdown format, optimized for use with Large Language Models (LLMs) like ChatGPT, Claude, and LLaMA. Checkout [docingest](https://docingest.com) for a hosted version of this with support for multiple other documentation providers like readthedocs, mintlify, docusaurus etc

## Purpose

- Download technical documentation for training custom LLMs
- Create knowledge bases for ChatGPT, Claude, and other AI assistants
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
pip install -r requirements.txt
```

## Usage

1. Start the web server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter the URL of a Gitbook documentation site

4. Choose to either:
   - View the converted content in your browser
   - Download the content as a markdown file

5. Use the downloaded markdown with:
   - ChatGPT (paste into conversation)
   - Claude (upload as a file)
   - Custom LLaMA models (include in training data)
   - Any other LLM that accepts markdown input

## Technical Details

The application uses:
- Flask for the web interface
- BeautifulSoup4 for HTML parsing
- Requests for fetching web content
- Python-slugify for URL/filename handling

## Note

This tool is designed specifically for Gitbook-based documentation sites and optimized for LLM consumption. It may not work correctly with other documentation platforms.
