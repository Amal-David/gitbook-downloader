from setuptools import setup, find_packages

setup(
    name="gitbook-downloader",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'beautifulsoup4',
        'aiohttp',
        'markdownify',
        'python-slugify',
    ],
    package_data={
        '': ['templates/*'],
    },
) 