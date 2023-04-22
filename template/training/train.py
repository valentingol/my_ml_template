"""Training functions."""
from template import ProjectConfig


def run(config: ProjectConfig) -> None:
    """Run training."""
    # Run training
    print("mode:", config.mode)
    print("Training done.")
