"""Test main.py."""
import os
import shutil

import pytest_check as check
from pytest_mock import MockerFixture


def test_main(mocker: MockerFixture) -> None:
    """Test main."""
    if os.path.exists("../tmp"):
        shutil.rmtree("../tmp")
    mocker.patch("template.inference.infer.run")
    mocker.patch("template.training.train.run")
    # Training mode
    run = os.system(
        "python template/main.py --config 'tests/configs/unitest_train.yaml'"
    )
    check.equal(run, 0)
    check.is_true(os.path.exists("../tmp"))
    shutil.rmtree("../tmp")
    # Inference mode
    run = os.system(
        "python template/main.py --config 'tests/configs/unitest_infer.yaml'"
    )
    check.equal(run, 0)
    check.is_true(os.path.exists("../tmp"))
    shutil.rmtree("../tmp")
    # Unknown mode
    run = os.system("python template/main.py --mode='UNKNOWN'")
    check.not_equal(run, 0)
    if os.path.exists("../tmp"):
        shutil.rmtree("../tmp")
