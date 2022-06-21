"""Setup file for the package."""
from setuptools import find_packages, setup

# Installation
config = {
        'name': 'my_worflow_template', 'version': '1.2',
        'description': 'Personal worflow template.',
        'author': 'Valentin Goldite',
        'author_email': 'valentin.goldite@gmail.com',
        'packages': find_packages(), 'zip_safe': True
        }

setup(**config)
