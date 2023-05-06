|Release| |PythonVersion| |PytorchVersion| |License|

|GitHub Release Date| |GitHub last commit| |GitHub User followers|
|GitHub User’s User stars|

|Torch_logo| |Wandb_logo|

|Ruff_logo| |Black_logo|

|Ruff| |Flake8| |Pydocstyle| |MyPy| |PyLint|

|Tests| |Coverage| |Bandit|

**Disclaimer**: Even if it is a personal project, everybody can use it
freely and modify it for their own needs.

This repository is a template for using in ML projects. It includes:

*  Inference and training template scripts
*  ⚙️ `YAECS <https://github.com/valentingol/yaecs>`__ as configuration
   manager (compatible with WandB, ClearML, …)
*  ✅ ``pytest-cov`` to check unit tests and get coverage (including an
   optional minimum coverage to pass)
*  🎨 ``ruff`` to check the style and auto-format it, including:

   *  ``pycodestyle`` and ``flake`` to check overall Python scripts
      style (PEP8)
   *  ``isort`` to check the import order of Python scripts
   *  ``pydocstyle`` to check Python docstrings style (Numpy convention)

*  🎨 ``pylint`` to have an overall grade of the style (including an
   optional minimum grade to pass)
*  🎨 ``black`` to auto-format Python scripts
*  🏷️ ``mypy`` to check typing and type hints

Some GitHub actions 🏭 are provided:

*  🔒 ``bandit`` for security
*  🎨 ``flake8``, ``mypy``, ``pydocstyle``, ``pylint``, ``ruff`` for
   style
*  Cache is preserved between GH action runs (useful for heavy
   requirements packages)

And finally, some badges:

*  🆙 Release, last commit and release date
*  🧑‍🤝‍🧑 Github stats
*  📑 licenses
*  🔖 python version (and pytorch version)
*  Pytorch and Wandb badges
*  And more…

All workflows create a badge available, for instance, in README.

This repository provides also a pre-commit configuration to check
end-of-file, trailing whitespace, flake8 and pydocstyle (numpy).

HowTo
-----

All feature of this template is easy to adapt on your project by
changing names or versions on the ``.github/workflows/`` directory and
on the badge paths on your markdown/rst files. All the worflows are
independent and can be used individually. You can also remove any
workflow you don’t need.

Before all, you need to create a `gist <https://gist.github.com/>`__ The
id of the gist is required for pylint and test/coverage badges. Then,
you must add a secret in your repository (*Settings > Secrets > New
repository secret*) that is a personal token with gist scope with name
GIST_SECRET (details
`here <https://github.com/Schneegans/dynamic-badges-action>`__).

.. |Release| image:: https://img.shields.io/github/v/release/valentingol/my_ml_template?include_prereleases
   :target: https://github.com/valentingol/my_ml_template/releases
.. |PythonVersion| image:: https://img.shields.io/badge/python-3.7%20%7E%203.11-informational
.. |PytorchVersion| image:: https://img.shields.io/badge/pytorch-1.8%20%7E%201.13%20%7C%202.0-informational
.. |License| image:: https://img.shields.io/github/license/valentingol/my_ml_template?color=999
   :target: https://stringfixer.com/fr/MIT_license
.. |GitHub Release Date| image:: https://img.shields.io/github/release-date/valentingol/my_ml_template
.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/valentingol/my_ml_template
.. |GitHub User followers| image:: https://img.shields.io/github/followers/valentingol?label=User%20followers&style=social
   :target: https://github.com/valentingol
.. |GitHub User’s User stars| image:: https://img.shields.io/github/stars/valentingol?label=User%20Stars&style=social
   :target: https://github.com/valentingol
.. |Torch_logo| image:: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
   :target: https://pytorch.org/
.. |Wandb_logo| image:: https://img.shields.io/badge/Weights_&_Biases-FFBE00?style=for-the-badge&logo=WeightsAndBiases&logoColor=white
   :target: https://wandb.ai/site
.. |Ruff_logo| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json
   :target: https://github.com/charliermarsh/ruff
.. |Black_logo| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
.. |Ruff| image:: https://github.com/valentingol/my_ml_template/actions/workflows/ruff.yaml/badge.svg
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/ruff.yaml
.. |Flake8| image:: https://github.com/valentingol/my_ml_template/actions/workflows/flake.yaml/badge.svg
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/flake.yaml
.. |Pydocstyle| image:: https://github.com/valentingol/my_ml_template/actions/workflows/pydocstyle.yaml/badge.svg
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/pydocstyle.yaml
.. |MyPy| image:: https://github.com/valentingol/my_ml_template/actions/workflows/mypy.yaml/badge.svg
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/mypy.yaml
.. |PyLint| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_pylint.json
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/pylint.yaml
.. |Tests| image:: https://github.com/valentingol/my_ml_template/actions/workflows/tests.yaml/badge.svg
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/tests.yaml
.. |Coverage| image:: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/valentingol/106c646ac67294657bccf02bbe22208f/raw/workflow_template_coverage.json
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/tests.yaml
.. |Bandit| image:: https://github.com/valentingol/my_ml_template/actions/workflows/bandit.yaml/badge.svg
   :target: https://github.com/valentingol/my_ml_template/actions/workflows/bandit.yaml

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   template
   license
