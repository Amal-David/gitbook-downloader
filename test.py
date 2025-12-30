"""
Test script for gitbook-downloader.

Downloads multiple documentation sites to verify the downloader still works correctly.
Creates a new tests-N folder (tests-1, tests-2, etc.) each run to preserve previous results.

Usage:
    python test.py
"""

import subprocess
import os

# Documentation URLs and their associated filenames
DOCS = [
    ["https://docs.zamm.eth.limo/", "zamm-docs.md"],
    ["https://gmtribe.gitbook.io/gmtribe/", "gmtribe-docs.md"],
    ["https://docs.metadao.fi/", "metadao-docs.md"],
    ["https://metalex-docs.vercel.app/", "metalex-docs.md"],
]


def find_next_test_folder():
    """Find the next available tests-N folder."""
    n = 1
    while os.path.exists(f"tests-{n}"):
        n += 1
    return f"tests-{n}"


def main():
    # Find and create the next test folder
    folder = find_next_test_folder()
    os.makedirs(folder)
    print(f"Created folder: {folder}")

    # Run download for each documentation URL
    for link, filename in DOCS:
        output_path = os.path.join(folder, filename)
        cmd = ["poetry", "run", "python", "cli.py", "download", link, "-o", output_path]
        print(f"\nDownloading: {link}")
        print(f"Output: {output_path}")
        subprocess.run(cmd)


if __name__ == "__main__":
    main()
