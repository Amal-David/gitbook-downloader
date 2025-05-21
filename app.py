from flask import Flask, request, jsonify, render_template, send_file
import threading
from documentation_downloader import DocumentationDownloader, DownloadStatus # Updated
from scrapers.scraper_factory import ScraperFactory
# GitbookScraper is no longer needed here, ScraperFactory handles it.
from bs4 import BeautifulSoup
import requests # Needed for initial fetch in download_task
import logging
import os
from datetime import datetime
import asyncio
import concurrent.futures
import sys
from urllib.parse import quote, unquote # Keep for task_id encoding/decoding if used
from urllib.parse import urlparse
from slugify import slugify # Added for robust filename generation

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('app.log')
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Store active downloads
active_downloads = {}
executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

# Ensure downloads directory exists
os.makedirs('downloads', exist_ok=True)

@app.errorhandler(404)
def not_found_error(error):
    logger.error("Resource not found")
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error("Internal server error")
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(Exception)
def handle_exception(error):
    logger.error(f"Error: {str(error)}")
    return jsonify({"error": str(error)}), 500

def download_task(url, task_id):
    """Background task to download content using DocumentationDownloader"""
    # Initialize a basic status object for early error reporting
    # This will be replaced by the downloader's status object once instantiated.
    temp_status = DownloadStatus(status="initializing", current_url=url)
    active_downloads[task_id] = temp_status # Store early

    try:
        logger.info(f"Starting download task for {url} with task_id {task_id}")

        # 1. Fetch initial page content to determine scraper type
        logger.debug(f"Fetching initial content for {url} to determine scraper type.")
        try:
            response = requests.get(url, timeout=20) # Increased timeout for initial fetch
            response.raise_for_status()
            initial_soup = BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch initial content for {url}: {str(e)}")
            temp_status.status = "error"
            temp_status.error = f"Failed to fetch initial URL: {str(e)}"
            # active_downloads[task_id] is already temp_status
            return # Exit task

        # 2. Create scraper instance
        scraper_instance = ScraperFactory.create_scraper(initial_soup, url)
        
        if scraper_instance is None:
            logger.error(f"Could not create scraper for {url}. ScraperFactory returned None.")
            temp_status.status = "error"
            temp_status.error = "Failed to identify site type or create a suitable scraper."
            # active_downloads[task_id] is already temp_status
            return # Exit task
        
        logger.info(f"Using scraper: {type(scraper_instance).__name__} for {url}")

        # 3. Instantiate DocumentationDownloader
        downloader = DocumentationDownloader(base_url=url, scraper_instance=scraper_instance)
        active_downloads[task_id] = downloader # Replace temp_status with actual downloader

        # 4. Run the download (async part)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        content = None
        try:
            logger.info(f"Starting DocumentationDownloader.download() for {url}")
            # The timeout for the entire download process is handled within DocumentationDownloader
            content = loop.run_until_complete(downloader.download())
            logger.info(f"DocumentationDownloader.download() completed for {url}")
        except Exception as e: # Catch errors from downloader.download()
            logger.error(f"Error during downloader.download() for {url}: {str(e)}", exc_info=True)
            downloader.status.status = "error"
            downloader.status.error = str(e)
            # No need to return here, finally block will run, then normal error handling at end of function
        finally:
            logger.debug(f"Closing asyncio event loop for task {task_id}")
            loop.close()

        if downloader.status.status == "error": # Error happened inside downloader.download()
             logger.error(f"Download task for {url} failed with error: {downloader.status.error}")
             # active_downloads[task_id] already has the downloader with error status
             return

        if not content:
            logger.error(f"No content returned from download for {url}, despite no explicit error.")
            downloader.status.status = "error"
            downloader.status.error = "No content was generated by the downloader."
            # active_downloads[task_id] already has the downloader with error status
            return

        # 5. Save content to file
        output_dir = "downloads"
        os.makedirs(output_dir, exist_ok=True)
        
        # Sanitize domain name for filename
        parsed_url = urlparse(url)
        # Use slugify for robust domain part, ensure it's not empty if netloc is weird
        domain_part = slugify(parsed_url.netloc) if parsed_url.netloc else "untitled-site"
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Use os.path.join for path construction
        # Filename structure: downloads/domain-slug_YYYYMMDD_HHMMSS.md
        base_filename = f"{domain_part}_{timestamp}.md"
        filename = os.path.join(output_dir, base_filename)
        
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            logger.info(f"Content for {url} saved to {filename}")
            downloader.status.output_file = filename # Crucial: set output_file on success
            # downloader.status.status should already be "completed" if download() succeeded
            if downloader.status.status != "completed": # Ensure it's marked completed
                 logger.warning(f"Downloader status was {downloader.status.status}, setting to completed for {url}")
                 downloader.status.status = "completed"

        except IOError as e:
            logger.error(f"Failed to write content to file {filename} for url {url}: {str(e)}")
            downloader.status.status = "error"
            downloader.status.error = f"Failed to save content: {str(e)}"
            # active_downloads[task_id] already has the downloader with error status
            return

    except Exception as e:
        logger.error(f"Unhandled error in download_task for {url}: {str(e)}", exc_info=True)
        # If downloader object exists, update its status. Otherwise, temp_status is already in active_downloads
        if 'downloader' in locals() and downloader:
            downloader.status.status = 'error'
            downloader.status.error = str(e)
        elif task_id in active_downloads and isinstance(active_downloads[task_id], DownloadStatus):
             # This means error happened before downloader was created, temp_status is active
            active_downloads[task_id].status = 'error'
            active_downloads[task_id].error = str(e)
        # else: cannot update status if task_id not in active_downloads, which shouldn't happen

@app.route('/')
def index():
    logger.info("Serving index page")
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def start_download():
    logger.info("Received download request")
    try:
        if not request.is_json:
            logger.error("Request is not JSON")
            return jsonify({"error": "Content-Type must be application/json"}), 400
            
        data = request.get_json()
        logger.debug(f"Request data: {data}")
        
        if not data or 'url' not in data:
            logger.error("No URL provided")
            return jsonify({"error": "Please provide a URL"}), 400
            
        url = data['url']
        # Basic URL validation
        if not (url.startswith('http://') or url.startswith('https://')):
            logger.error(f"Invalid URL scheme: {url}")
            return jsonify({"error": "Invalid URL scheme. Must be http or https."}), 400

        logger.info(f"Request to start download for URL: {url}")
        
        # Use the URL directly as the task ID (consider a more robust ID generation if needed)
        task_id = url 
        
        if task_id in active_downloads:
            downloader_status = active_downloads[task_id].status
            # Check if status is an object or a string (if it's the temp_status string value)
            current_status_val = downloader_status.status if hasattr(downloader_status, 'status') else downloader_status
            
            if current_status_val in ['initializing', 'downloading', 'running', 'generating_markdown']:
                 logger.info(f"Download for {url} (task {task_id}) already in progress with status: {current_status_val}")
                 return jsonify({
                    "task_id": task_id,
                    "message": "Download already in progress",
                    "status": current_status_val
                }), 202 # Accepted, but already running
            elif current_status_val == 'completed':
                logger.info(f"Download for {url} (task {task_id}) already completed. Output: {active_downloads[task_id].status.output_file}")
                return jsonify({
                    "task_id": task_id,
                    "message": "Download already completed. Check status or result.",
                    "status": "completed",
                    "output_file": active_downloads[task_id].status.output_file
                }), 200 # OK, already done
            # Allow re-download if status is 'error' or an unknown state
            logger.info(f"Previous download for {url} (task {task_id}) had status {current_status_val}. Starting new download.")


        logger.info(f"Starting new download thread for URL: {url} with task_id: {task_id}")
        # Start new download in background
        thread = threading.Thread(
            target=download_task,
            args=(url, task_id)
        )
        thread.daemon = True
        thread.start()
        
        return jsonify({
            "task_id": task_id,
            "message": "Download started",
            "status": "running"
        })
        
    except Exception as e:
        logger.error(f"Error starting download: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

@app.route('/status/<path:task_id>')
def get_status(task_id):
    """Get the status of a download task"""
    try:
        logger.info(f"Status check for task: {task_id}")
        
        if task_id not in active_downloads:
            return jsonify({"error": "Task not found"}), 404
            
        downloader = active_downloads[task_id]
        status_data = {
            "status": downloader.status.status,
            "current_page": downloader.status.current_page,
            "total_pages": downloader.status.total_pages,
            "current_url": downloader_status.current_url,
            "pages_scraped_titles": downloader_status.pages_scraped_titles if hasattr(downloader_status, 'pages_scraped_titles') else [],
            "error": downloader_status.error,
            "output_file": downloader_status.output_file,
            "failed_pages_count": downloader_status.failed_pages_count if hasattr(downloader_status, 'failed_pages_count') else 0,
            "log_messages": downloader_status.log_messages if hasattr(downloader_status, 'log_messages') else []
        }
        
        if hasattr(downloader_status, "rate_limit_reset") and downloader_status.rate_limit_reset:
            status_data["rate_limit_reset"] = downloader_status.rate_limit_reset
            
        return jsonify(status_data)
    except Exception as e:
        logger.error(f"Error in get_status for task {task_id}: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

@app.route('/result/<path:task_id>')
def get_result(task_id):
    """Get the result of a completed download by serving the saved markdown file's content."""
    try:
        logger.info(f"Result requested for task: {task_id}")
        if task_id not in active_downloads:
            logger.warning(f"Task not found for result: {task_id}")
            return jsonify({"error": "Task not found"}), 404
            
        downloader_status = active_downloads[task_id].status
        
        if downloader_status.status != "completed":
            logger.warning(f"Task {task_id} not completed. Status: {downloader_status.status}")
            return jsonify({"error": "Task not completed or failed.", "status": downloader_status.status}), 400 # Bad Request or other appropriate status
            
        output_file = downloader_status.output_file
        if not output_file or not os.path.exists(output_file):
            logger.error(f"Output file not found for completed task {task_id}. Expected at {output_file}")
            return jsonify({"error": "Output file not found, even though task completed."}), 500
            
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()
            # Return as plain text/markdown directly, not JSON
            return content, 200, {'Content-Type': 'text/markdown; charset=utf-8'}
        except Exception as e:
            logger.error(f"Error reading result file {output_file} for task {task_id}: {str(e)}", exc_info=True)
            return jsonify({"error": f"Error reading result file: {str(e)}"}), 500
            
    except Exception as e:
        logger.error(f"Error in get_result for task {task_id}: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

@app.route('/download/<path:task_id>/markdown')
def download_markdown(task_id):
    """Download the markdown file for a completed task."""
    try:
        logger.info(f"Markdown download requested for task: {task_id}")
        if task_id not in active_downloads:
            logger.warning(f"Task not found for markdown download: {task_id}")
            return jsonify({"error": "Task not found"}), 404
            
        downloader_status = active_downloads[task_id].status
        
        if downloader_status.status != "completed":
            logger.warning(f"Task {task_id} not completed for markdown download. Status: {downloader_status.status}")
            return jsonify({"error": "Task not completed or failed. Cannot download.", "status": downloader_status.status}), 400
            
        output_file = downloader_status.output_file
        if not output_file or not os.path.exists(output_file):
            logger.error(f"Output file not found for markdown download of task {task_id}. Expected at {output_file}")
            return jsonify({"error": "Output file not found, even though task completed."}), 500
            
        try:
            # Generate a download name based on the original URL's domain
            # The base_url should be available on the downloader object itself, not just its status.
            # Assuming active_downloads[task_id] is the downloader instance.
            downloader_instance = active_downloads[task_id]
            domain = urlparse(downloader_instance.base_url).netloc or "download"
            download_name = f"{domain.replace('.', '_')}.md"

            return send_file(
                output_file,
                as_attachment=True,
                download_name=download_name,
                mimetype='text/markdown'
            )
                
        except Exception as e:
            logger.error(f"Error sending file {output_file} for task {task_id}: {str(e)}", exc_info=True)
            return jsonify({"error": f"Error preparing file for download: {str(e)}"}), 500
            
    except Exception as e:
        logger.error(f"Error in download_markdown for task {task_id}: {str(e)}", exc_info=True)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=8080, debug=True)
