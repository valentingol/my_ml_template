"""Test the training."""
from template.training.train import run


def test_train_run() -> None:
    """Test run."""
    # NOTE: should be split into multiple sub-blocks to test
    # For instance: one test for data loading, one for model
    # and optimizer creation, one for logging, one for model saving,
    # and one for training (model parameters update)
    run({"mode": "train"})
