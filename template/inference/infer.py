"""Inference main functions."""
from typing import Any, Dict


def run(config: Dict[str, Any]) -> None:
    """Run Inference."""
    # Run inference
    print("mode:", config["mode"])
    print("Inference done.")
