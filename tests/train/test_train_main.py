"""Test the training."""
import shutil

from pytest_mock import MockerFixture

from template import ProjectConfig
from template.train.main import main, run


def test_main(mocker: MockerFixture) -> None:
    """Test main."""
    mocker.patch("template.train.main.run")
    main()


def test_run() -> None:
    """Test run."""
    # NOTE: should be split into multiple sub-blocks to test
    # For instance: one test for data loading, one for model
    # and optimizer creation, one for logging, one for model saving,
    # and one for training (model parameters update)
    config = ProjectConfig.load_config("tests/configs/unitest_train.yaml")
    run(config)
    shutil.rmtree("tests/tmp")
