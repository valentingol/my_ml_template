"""Training functions."""
from template import ProjectConfig


def run(config: ProjectConfig) -> None:
    """Run training."""
    # Run training
    assert config.experiment_path is not None
    print("Training done.")
