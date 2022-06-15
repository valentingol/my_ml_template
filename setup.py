"""Setup file for the package."""
from setuptools import setup, find_packages


# Installation
config = {
    'name': 'my_worflow_template',
    'version': '1.1',
    'description': 'Personal worflow template.',
    'author': 'Valentin Goldite',
    'author_email': 'valentin.goldite@gmail.com',
    'packages': find_packages(),
    'zip_safe': True
}

setup(**config)
