"""Test the inference."""
from template.inference.infer import run


def test_infer_run() -> None:
    """Test run."""
    # NOTE: should be split into multiple sub-blocks to test
    # For instance: one test for data loading, one for model
    # creation, and one for logging and results saving
    run({"mode": "infer"})
