# Personal workflow template

[![Release](https://img.shields.io/github/v/release/valentingol/my_ml_template?include_prereleases)](https://github.com/valentingol/my_ml_template/releases)
![PythonVersion](https://img.shields.io/badge/python-3.8%20%7E%203.11-informational)
![PytorchVersion](https://img.shields.io/badge/pytorch-1.8%20%7E%201.13%20%7C%202.0-informational)
[![License](https://img.shields.io/github/license/valentingol/my_ml_template?color=999)](https://stringfixer.com/fr/MIT_license)

![GitHub Release Date](https://img.shields.io/github/release-date/valentingol/my_ml_template)
![GitHub last commit](https://img.shields.io/github/last-commit/valentingol/my_ml_template)
[![GitHub User followers](https://img.shields.io/github/followers/valentingol?label=User%20followers&style=social)](https://github.com/valentingol)
[![GitHub User's User stars](https://img.shields.io/github/stars/valentingol?label=User%20Stars&style=social)](https://github.com/valentingol)

[![Torch_logo](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Wandb_logo](https://img.shields.io/badge/Weights_&_Biases-FFBE00?style=for-the-badge&logo=WeightsAndBiases&logoColor=white)](https://wandb.ai/site)

[![Ruff_logo](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Black_logo](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Ruff](https://github.com/valentingol/my_ml_template/actions/workflows/ruff.yaml/badge.svg)](https://github.com/valentingol/my_ml_template/actions/workflows/ruff.yaml)
[![Flake8](https://github.com/valentingol/my_ml_template/actions/workflows/flake.yaml/badge.svg)](https://github.com/valentingol/my_ml_template/actions/workflows/flake.yaml)
[![Pydocstyle](https://github.com/valentingol/my_ml_template/actions/workflows/pydocstyle.yaml/badge.svg)](https://github.com/valentingol/my_ml_template/actions/workflows/pydocstyle.yaml)
[![MyPy](https://github.com/valentingol/my_ml_template/actions/workflows/mypy.yaml/badge.svg)](https://github.com/valentingol/my_ml_template/actions/workflows/mypy.yaml)
[![PyLint](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_pylint.json)](https://github.com/valentingol/my_ml_template/actions/workflows/pylint.yaml)

[![Tests](https://github.com/valentingol/my_ml_template/actions/workflows/tests.yaml/badge.svg)](https://github.com/valentingol/my_ml_template/actions/workflows/tests.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_coverage.json)](https://github.com/valentingol/my_ml_template/actions/workflows/tests.yaml)
[![Bandit](https://github.com/valentingol/my_ml_template/actions/workflows/bandit.yaml/badge.svg)](https://github.com/valentingol/my_ml_template/actions/workflows/bandit.yaml)

**Disclaimer**: Even if it is a personal project, everybody can use it freely
and modify it for their own needs.

![alt text](assets/github_actions.jpg)

This repository is a template for using in ML projects. It includes:

- Inference and training template scripts
- ⚙️ [YAECS](https://github.com/valentingol/yaecs) as configuration manager
  (compatible with WandB, ClearML, ...)
- ✅ `pytest-cov` to check unit tests and get coverage (including an optional
  minimum coverage to pass)
- 🎨 `ruff` to check the style and auto-format it, including:
  - `pycodestyle` and `flake` to check overall Python scripts style (PEP8)
  - `isort` to check the import order of Python scripts
  - `pydocstyle` to check Python docstrings style (Numpy convention)
- 🎨 `pylint` to have an overall grade of the style (including an optional minimum
grade to pass)
- 🎨 `black` to auto-format Python scripts
- 🏷️ `mypy` to check typing and type hints

Some GitHub actions 🏭 are provided:

- 🔒 `bandit` for security
- 🎨 `flake8`, `mypy`, `pydocstyle`, `pylint`, `ruff` for style
- Cache is preserved between GH action runs (useful for heavy requirements packages)

And finally, some badges:

- 🆙 Release, last commit and release date
- 🧑‍🤝‍🧑 Github stats
- 📑 licenses
- 🔖 python version (and pytorch version)
- Pytorch and Wandb badges
- And more...

All workflows create a badge available, for instance, in README.

This repository provides also a pre-commit configuration to check end-of-file,
trailing whitespace, flake8 and pydocstyle (numpy).

![alt text](assets/checks.svg)

## HowTo

All feature of this template is easy to adapt on your project by changing names
or versions on the `.github/workflows/` directory and on the badge paths on your
markdown/rst files. All the worflows are independent and can be used individually.
You can also remove any workflow you don't need.

Before all, you need to create a [gist](https://gist.github.com/) The id of the
gist is required for pylint and test/coverage badges. Then, you must add a secret
in your repository (*Settings > Secrets > New repository secret*) that is a personal
token with gist scope with name GIST_SECRET (details
[here](https://github.com/Schneegans/dynamic-badges-action)).

## Notes

By default, there is no maximum unit test coverage but you can set the minimum
coverage you want in `utils/github_actions/pytest_manager.py`. There is also a
minimum grade for pylint that is 7.0/10 and can be set in
`utils/github_actions/pylint_manager.py`. Details of pylint options are in
`.pylintrc` and can also be changed at will.

## Contributing

Even if it is a personal template, feel free to contribute via issues or pull
requests 🤗.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.
