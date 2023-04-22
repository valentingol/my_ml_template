"""Inference main functions."""
import os.path as osp

from template import ProjectConfig


def run(config: ProjectConfig) -> None:
    """Run Inference."""
    # Run inference
    assert config.experiment_path is not None
    print("Inference done.")


def main() -> None:
    """Launch inference using YAECS config."""
    config = ProjectConfig.build_from_argv(fallback="configs/infer_exp/base.yaml")
    config.save(osp.join(config.experiment_path, "config.yaml"))
    run(config)


if __name__ == "__main__":
    main()
