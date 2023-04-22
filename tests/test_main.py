"""Test main.py."""
import os
import shutil

import pytest_check as check
from pytest_mock import MockerFixture


def test_main(mocker: MockerFixture) -> None:
    """Test main."""
    if os.path.exists("tests/tmp"):
        shutil.rmtree("tests/tmp")
    mocker.patch("template.inference.infer.run")
    mocker.patch("template.training.train.run")
    # training mode
    run = os.system(
        "python template/main.py --mode='train' --experiment_path='tests/tmp/1'"
    )
    check.equal(run, 0)
    check.is_true(os.path.exists("tests/tmp/1_0/config.yaml"))
    check.is_true(os.path.exists("tests/tmp/1_0/config_hierarchy.yaml"))
    # inference mode
    run = os.system(
        "python template/main.py --mode='infer' --experiment_path='tests/tmp/2'"
    )
    check.equal(run, 0)
    check.is_true(os.path.exists("tests/tmp/1_0/config.yaml"))
    check.is_true(os.path.exists("tests/tmp/1_0/config_hierarchy.yaml"))
    # unknown mode
    run = os.system(
        "python template/main.py --mode='UNKNOWN' --experiment_path='tests/tmp/3'"
    )
    check.not_equal(run, 0)

    shutil.rmtree("tests/tmp")
