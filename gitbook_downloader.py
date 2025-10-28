from urllib.parse import urlparse

class GitbookDownloader:
    """
    Backward-compatible alias for DocumentationDownloader.
    Exposes base_url and domain attributes.
    """
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc