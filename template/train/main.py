"""Training functions."""
import os.path as osp

from template import ProjectConfig


def run(config: ProjectConfig) -> None:
    """Run training."""
    # Run training
    assert config.experiment_path is not None
    print("Training done.")


def main() -> None:
    """Launch training using YAECS config."""
    config = ProjectConfig.build_from_argv(fallback="configs/exp/base.yaml")
    config.save(osp.join(config.experiment_path, "config.yaml"))
    run(config)


if __name__ == "__main__":
    main()
