from flask import Flask, request, jsonify, render_template, send_file
import threading
from gitbook_downloader import GitbookDownloader
import logging
import os
from datetime import datetime
import asyncio
import concurrent.futures
import sys
from urllib.parse import quote, unquote
from urllib.parse import urlparse

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
    """Background task to download content"""
    try:
        logger.info(f"Starting download task for {url}")
        downloader = GitbookDownloader(url, native_md=False)
        active_downloads[task_id] = downloader
        
        # Create new event loop for this thread
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            # Run the download
            content = loop.run_until_complete(downloader.download())
        finally:
            loop.close()
            
        # Save content to file
        output_dir = "downloads"
        os.makedirs(output_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/gitbook_{timestamp}.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Content saved to {filename}")
            
        downloader.status.status = "completed"
        downloader.status.current_url = filename
        downloader.status.output_file = filename
        
    except Exception as e:
        logger.error(f"Error in download task: {str(e)}")
        if task_id in active_downloads:
            active_downloads[task_id].status.status = 'error'
            active_downloads[task_id].status.error = str(e)

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
        logger.info(f"Starting download for URL: {url}")
        
        # Use the URL directly as the task ID
        task_id = url
        
        if task_id in active_downloads:
            if active_downloads[task_id].status.status in ['running', 'generating_markdown']:
                return jsonify({
                    "task_id": task_id,
                    "message": "Download already in progress",
                    "status": active_downloads[task_id].status.status
                })
        
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
            "current_url": downloader.status.current_url,
            "pages_scraped": downloader.status.pages_scraped,
            "error": getattr(downloader.status, "error", None),
            "output_file": getattr(downloader.status, "output_file", None)
        }
        
        if hasattr(downloader.status, "rate_limit_reset"):
            status_data["rate_limit_reset"] = downloader.status.rate_limit_reset
            
        return jsonify(status_data)
    except Exception as e:
        logger.error(f"Error in get_status: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/result/<path:task_id>')
def get_result(task_id):
    """Get the result of a completed download"""
    try:
        if task_id not in active_downloads:
            return jsonify({"error": "Task not found"}), 404
            
        downloader = active_downloads[task_id]
        if not hasattr(downloader.status, "output_file"):
            return jsonify({"error": "Output file not found"}), 404
            
        try:
            # Return the current content even if not completed
            if hasattr(downloader, 'pages') and downloader.pages:
                content = downloader._generate_markdown()
                return content
            else:
                return jsonify({"error": "No content available yet"}), 404
        except Exception as e:
            logger.error(f"Error reading result file: {str(e)}")
            return jsonify({"error": f"Error reading result: {str(e)}"}), 500
            
    except Exception as e:
        logger.error(f"Error in get_result: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/download/<path:task_id>/markdown')
def download_markdown(task_id):
    """Download the markdown file"""
    try:
        if task_id not in active_downloads:
            return jsonify({"error": "Task not found"}), 404
            
        downloader = active_downloads[task_id]
        
        try:
            # Generate fresh markdown content
            content = downloader._generate_markdown()
            if not content:
                return jsonify({"error": "No content available"}), 404
                
            # Create a temporary file with the content
            domain = urlparse(downloader.base_url).netloc
            temp_file = f'temp_{domain}.md'
            with open(temp_file, 'w', encoding='utf-8') as f:
                f.write(str(content))  # Ensure content is string
            
            return send_file(
                temp_file,
                as_attachment=True,
                download_name=f"{domain}.md",
                mimetype='text/markdown'
            )
                
        except Exception as e:
            logger.error(f"Error sending file: {str(e)}")
            return jsonify({"error": f"Error downloading file: {str(e)}"}), 500
            
    except Exception as e:
        logger.error(f"Error in download_markdown: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=8080, debug=True)
