# Personal workflow template

[![Release](https://img.shields.io/github/v/release/valentingol/my_workflow_template?include_prereleases)](https://github.com/valentingol/my_workflow_template/releases)
![PythonVersion](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-informational)
[![License](https://img.shields.io/github/license/valentingol/my_workflow_template?color=999)](https://stringfixer.com/fr/MIT_license)

[![Pycodestyle](https://github.com/valentingol/my_workflow_template/actions/workflows/pycodestyle.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/pycodestyle.yaml)
[![Flake8](https://github.com/valentingol/my_workflow_template/actions/workflows/flake.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/flake.yaml)
[![PyLint](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_pylint.json)](https://github.com/valentingol/my_workflow_template/actions/workflows/pylint.yaml)

[![Tests](https://github.com/valentingol/my_workflow_template/actions/workflows/tests.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/tests.yaml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_coverage.json)](https://github.com/valentingol/my_workflow_template/actions/workflows/tests.yaml)

[![Bandit](https://github.com/valentingol/my_workflow_template/actions/workflows/bandit.yaml/badge.svg)](https://github.com/valentingol/my_workflow_template/actions/workflows/bandit.yaml)

This repository is a template for using some GitHub worflows:

- ✅ `pytest-cov` to check tests and get overage
- 🎨 `pycodestyle` and `flake` to check Python scripts style (PEP8)
- 🎨 `pylint` to have an overall grade of the style (incuding a minimum grade to pass)
- 🔒 `bandit` for security

All worflows create a badge available, for instace, in README.

Some other badges are provided (such as release, licenses and python version).

## HowTo

All feature of this template is easy to adapt on your project by changing names or versions.

Don't forget to create a [gist](https://gist.github.com/) and add a secret in your repository that is a personal token with gist scope with name GIST_SECRET (details [here](https://github.com/Schneegans/dynamic-badges-action).
