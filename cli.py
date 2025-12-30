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
@click.option("--native", "-n", is_flag=True, help="Request native markdown")
def download(url, output, native):
    """Download a GitBook by URL and save as markdown."""

    async def run():
        downloader = GitbookDownloader(url, native)
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
