"""Test the inference."""
import shutil

from template import ProjectConfig
from template.inference.infer import run


def test_run() -> None:
    """Test run."""
    # NOTE: should be split into multiple sub-blocks to test
    # For instance: one test for data loading, one for model
    # creation, and one for logging and results saving
    config = ProjectConfig.load_config("tests/configs/unitest_infer.yaml")
    run(config)
    shutil.rmtree("tests/tmp")
