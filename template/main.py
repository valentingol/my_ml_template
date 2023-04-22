"""Main function to run inference or training."""
import os.path as osp

from template import ProjectConfig
from template.inference.infer import run as run_infer
from template.training.train import run as run_train


def main() -> None:
    """Launch training using YAECS config."""
    config = ProjectConfig.build_from_argv(fallback="configs/exp/base.yaml")
    config.save(osp.join(config.experiment_path, "config.yaml"))
    if config.mode == "train":
        run_train(config)
    elif config.mode == "infer":
        run_infer(config)
    else:
        raise ValueError(
            f"Unknown mode: {config.mode} " "(should be 'train' or 'infer)."
        )


if __name__ == "__main__":
    main()
