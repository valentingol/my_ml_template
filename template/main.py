"""Main function to run inference or training."""
import os.path as osp
import random

from cliconfig import Config, create_processing_value, make_config, save_config

from template.inference.infer import run as run_infer
from template.training.train import run as run_train


def main() -> None:
    """Launch training using YAECS config."""
    config = get_config()
    if config.mode == "train":
        run_train(config.dict)
    elif config.mode == "infer":
        run_infer(config.dict)
    else:
        raise ValueError(f"Unknown mode: {config.mode} (should be 'train' or 'infer).")


def get_config() -> Config:
    """Get and save the config."""
    run_id_proc = create_processing_value(
        lambda _: random.randint(0, 1_000_000), "run_id"
    )
    config = make_config("configs/default/main.yaml", process_list=[run_id_proc])
    cfg_path = osp.join(config.config_dir, str(config.run_id), "config.yaml")
    save_config(config, cfg_path)
    return config


if __name__ == "__main__":
    main()
