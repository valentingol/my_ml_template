"""Training functions."""
from typing import Any, Dict


def run(config: Dict[str, Any]) -> None:
    """Run training."""
    # Run training
    print("mode:", config["mode"])
    print("Training done.")
