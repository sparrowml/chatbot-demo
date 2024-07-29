import fire

from .app import dev
from .evaluate import evaluate_model


def main() -> None:
    """Call CLI commands."""
    fire.Fire({"dev": dev, "evaluate-model": evaluate_model})
