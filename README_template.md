
# [Title]

[Description + badges]

## Installation

In a new virtual environment, install the package with:

```bash
pip install -e .
```

For **development**, install the dev requirements with:

```bash
pip install -r requirements-dev.txt
```

## Quick start

To train a basic model:

```bash
python template/main.py
```

To train a basic model with a custom parameter (e.g. train.learning_rate):

```bash
python template/main.py --train.learning_rate=0.001
```

All parameters can be modified this way.

To make an inference:

```bash
python template/main.py --config configs/infer_exp/base.yaml
```

## Configurations

It is always interesting to customize the training with your own configurations.
This repository contains a lot of configuration organized in multiple sub-configurations.
The management of the configurations is simply done thanks to the smart configuration
manager [YAECS](https://github.com/valentingol/yaecs).

The default sub-configurations (for models, training, ...) are organized in
different json files in `configs/default`. You can launch your own experiment by
writing a new `.yaml` file that will be merged with the default configuration.
Some examples are available in `configs/exp`. For example, the following file
will override the default value of the name of the run as well as discriminator
learning rate to 0.001:

```yaml
# >> file 'configs/exp/my_config.yaml'
experiment_path: "../exp_configs/exp/my_exp"
model.layers: 2
```

Then you can run the experiment by adding the configuration in command line.

```bash
python template/main.py --config configs/exp/my_exp.yaml
```

*Note: The space between the `--config` and the configuration file is important.*

Moreover you can override parameters also by adding them in the **command line**.
For example this will override the default configuration with your experiment
configuration, then set the generator learning rate to 0.001 and the generator
random input dimension to 64:

```bash
python gan_facies/apps/train.py --config gan_facies/configs/exp/my_config.yaml --training.epochs=5\
 --data.flip_probability=0.5
```

*Note: The `=` between the `--param` and the value is important.*

An other way to manage experiments is to use the merging of configurations
in cascade provided by yaecs. In fact, if you put a **list** of configuration
file for `--config`, they will be merge together (from the begin of the list
to the end). Example:

```batch
python gan_facies/apps/train.py --config [configs/exp/model.yaml,configs/exp/data.yaml]
```

First `configs/exp/model.yaml` will be used (changing model configuration for instance)
then `configs/exp/data.yaml` will be merged (overwriting data configuration for instance).
You can create your own specific configurations (for data, models, metric, ...)
and merge as many of them as you want.

Finally, the configurations will be automatically saved (in `config.experiment_path`)
to ensure that you can always recover the exact configuration used for the runs.
The "hierarchy of merging" is also saved to understand quickly how the configuration
was merged (with what experiment file(s) and what command line parameters).

**A description of all configuration parameters is available in `CONFIG_SUMMARY.md`.**
