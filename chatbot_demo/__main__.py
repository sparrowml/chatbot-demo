import fire

from .app import dev


def main() -> None:
    """Call CLI commands."""
    fire.Fire({"dev": dev})