"""Inference main functions."""
from template import ProjectConfig


def run(config: ProjectConfig) -> None:
    """Run Inference."""
    # Run inference
    print("mode:", config.mode)
    print("Inference done.")
