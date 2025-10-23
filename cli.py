import click
import asyncio
from gitbook_downloader import GitbookDownloader


@click.group()
def cli():
    """GitBook Downloader CLI"""
    pass


@cli.command()
@click.argument("url")
@click.option("--output", "-o", default=None, help="Output markdown file")
@click.option("--recursive", "-r", is_flag=True, help="Look for sub-nav links")
def download(url, output, recursive):
    """Download a GitBook by URL and save as markdown."""

    async def run():
        downloader = GitbookDownloader(url, recursive)
        markdown = await downloader.download()
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(markdown)
            click.echo(f"Saved to {output}")
        else:
            click.echo(markdown)

    asyncio.run(run())


if __name__ == "__main__":
    cli()
