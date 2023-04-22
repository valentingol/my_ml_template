"""Inference main functions."""
from template import ProjectConfig


def run(config: ProjectConfig) -> None:
    """Run Inference."""
    # Run inference
    assert config.experiment_path is not None
    print("Inference done.")
