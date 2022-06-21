# Personal workflow template

[![Release](https://img.shields.io/github/v/release/valentingol/my_workflow_template?include_prereleases)](https://github.com/valentingol/my_workflow_template/releases)
![PythonVersion](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-informational)
[![License](https://img.shields.io/github/license/valentingol/my_workflow_template?color=999)](https://stringfixer.com/fr/MIT_license)

![GitHub Release Date](https://img.shields.io/github/release-date/valentingol/my_workflow_template)
![GitHub last commit](https://img.shields.io/github/last-commit/valentingol/my_workflow_template)
[![GitHub User followers](https://img.shields.io/github/followers/valentingol?label=User%20followers&style=social)](https://github.com/valentingol)
[![GitHub User's User stars](https://img.shields.io/github/stars/valentingol?label=User%20Stars&style=social)](https://github.com/valentingol)

[![Pycodestyle](https://github.com/valentingol/my_workflow_template/actions/workflows/pycodestyle.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/pycodestyle.yaml)
[![Flake8](https://github.com/valentingol/my_workflow_template/actions/workflows/flake.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/flake.yaml)
[![Pydocstyle](https://github.com/valentingol/my_workflow_template/actions/workflows/pydocstyle.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/pydocstyle.yaml)
[![MyPy](https://github.com/valentingol/my_workflow_template/actions/workflows/mypy.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/mypy.yaml)
[![Isort](https://github.com/valentingol/my_workflow_template/actions/workflows/isort.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/isort.yaml)
[![PyLint](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_pylint.json)](https://github.com/valentingol/my_workflow_template/actions/workflows/pylint.yaml)

[![Tests](https://github.com/valentingol/my_workflow_template/actions/workflows/tests.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/tests.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_coverage.json)](https://github.com/valentingol/my_workflow_template/actions/workflows/tests.yaml)
[![Bandit](https://github.com/valentingol/my_workflow_template/actions/workflows/bandit.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/bandit.yaml)

**Disclaimer**: Even if it is a personal project, everybody can use it freely and modify it for their own needs.

![alt text](assets/github_actions.jpg)

This repository is a template for using some GitHub worflows:

- ✅ `pytest-cov` to check unit tests and get coverage (including an optional minimum coverage to pass)
- 🎨 `pycodestyle` and `flake` to check Python scripts style (PEP8)
- 🎨 `isort` to check the import order of Python scripts
- 🎨 `pylint` to have an overall grade of the style (incuding an optional minimum grade to pass)
- 📝 `pydocstyle` to check Python docstrings style (Numpy convention)
- 🏷️ `mypy` to check typing
- 🔒 `bandit` for security
- 🔄 Cache is preserved between runs (usefull for heavy requirements)
- ⌚ Last commit and release date
- 🧑‍🤝‍🧑 Github stats
- Some other badges are provided (such as release ⏫, licenses 📑 and python version 🔖).

All worflows create a badge available, for instace, in README.

This repository provides also a pre-commit configuration to check end-of-file, trailing whitespace, flake8, pydocstyle (numpy) and isort.

![alt text](assets/checks.png)

## HowTo

All feature of this template is easy to adapt on your project by changing names or versions on the `.github/workflows/` directory and on the badge paths on your markdown/rst files. All the worflows are independent and can be used individually.

First you need to create a [gist](https://gist.github.com/) The id of the gist is required for pylint and test/coverage badges. Then, you must add a secret in your repository (*Settings > Secrets > New repository secret*) that is a personal token with gist scope with name GIST_SECRET (details [here](https://github.com/Schneegans/dynamic-badges-action)).

## Notes

By default, there is no maximum unit test coverage but you can set the minimum coverage you want in `utils/github_actions/pytest_manager.py`. There is also a minimum grade for pylint that is 7.0/10 and can be set in `utils/github_actions/pylint_manager.py`. Details of pylint options are in `.pylintrc` and can also be changed at will. Pycodestyle, Flake, Pydocstyle, MyPy, Bandit should raise no warnings/errors to pass (but not YAPF).

## Contributing

Even if it is a personal template, feel free to contribute via issues or pull requests 🤗
