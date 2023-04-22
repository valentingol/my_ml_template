# Configuration summary

Description of all configuration parameters organized in the sub-configs.
Some configurations **must** be overwritten in experiment config file depending on
the context of use.

Moreover, the most important configuration parameters that impact
performance and may be fitted for your dataset and setup in priority are
indicated with an asterisk (\*) at the beginning of the line.

## Main

Default configuration in `configs/default/main.yaml`.
Associated name space: `config.*`.

- (\*) `experiment_path` (str): the path of the experiment (will contain the config).

  **Must be overwritten in experiment config file**

- ...

## Train

Default configuration in `configs/default/main.yaml`.
Associated name space: `config.train.*`.

- `learning_rate` (float): the learning rate of the optimizer.

  Default: 0.001.

## Infer

Default configuration in `configs/default/main.yaml`.
Associated name space: `config.infer.*`.

- (\*) `model_path`: the path of the model to load for inference.

  **Must be overwritten in experiment config file**

## Data

Default configuration in `configs/configs/main.yaml`.
Associated name space: `config.data.*`.

- ...

## Model

Default configuration in `configs/default/main.yaml`.
Associated name space: `config.model.*`.

- ...
