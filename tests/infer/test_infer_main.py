"""Test the inference."""
import shutil

from pytest_mock import MockerFixture

from template import ProjectConfig
from template.infer.main import main, run


def test_main(mocker: MockerFixture) -> None:
    """Test main."""
    mocker.patch("template.train.main.run")
    main()


def test_run() -> None:
    """Test run."""
    # NOTE: should be split into multiple sub-blocks to test
    # For instance: one test for data loading, one for model
    # creation, and one for logging and results saving
    config = ProjectConfig.load_config("tests/configs/unitest_infer.yaml")
    run(config)
    shutil.rmtree("tests/tmp")
