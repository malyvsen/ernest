from pathlib import Path

import asyncclick as click
import httpx

import ernest

DATA_URL = "https://www.gutenberg.org/ebooks/67138.txt.utf-8"
BOOK_PATH = Path(ernest.__file__).parents[1] / "data" / "book.txt"


@click.command()
async def main():
    """Download the text of the book."""

    async with httpx.AsyncClient() as client:
        response = await client.get(DATA_URL, follow_redirects=True)
        response.raise_for_status()

    text = response.text
    num_bytes = BOOK_PATH.write_text(text)
    click.echo(f"Wrote {num_bytes} bytes to {BOOK_PATH.as_posix()}")


if __name__ == "__main__":
    main()
