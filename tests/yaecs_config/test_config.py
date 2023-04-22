"""Test yaecs_config/config.py."""
import shutil

import pytest_check as check

from template import ProjectConfig


def test_project_config() -> None:
    """Test ProjectConfig."""
    config = ProjectConfig.build_from_argv(fallback="tests/configs/unitest_train.yaml")
    check.not_equal(config.experiment_path, None)
    check.equal(config.model.layers, 1)
    shutil.rmtree("tests/tmp")
