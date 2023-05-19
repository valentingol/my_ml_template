# Tutorial for Read the docs (automatic documentation on the web)

## Setup

Copy the `docs/` folder in the root of your project. Remove `_static/` content
(the folder should contains all the assets). Go to a virtual environment
(containing the current project preferably) and install the documentation
dependencies:

```bash
pip install -r docs/requirements.txt
```

## Launch sphinx autodoc

```bash
sphinx-apidoc -f -o docs <package>
```

Clean the built .rst files (remove empty or unused sections and files).

Modify `docs/index.rst` to add the pages to document.
You should also modify the homepage in this file.
Then, you can add new pages (in .rst or .md).

## Build the documentation with sphinx

```bash
sphinx-build -b html docs/ docs/_build
```

## Visualize the documentation

Open [docs/_build/index.html](docs/_build/index.html) in your browser.
