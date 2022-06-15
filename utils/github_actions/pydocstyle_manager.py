"""Manage Pydocstyle output on worflow."""
import sys


if __name__ == '__main__':
    score = int((sys.argv[1]).split('=')[1])
    if score > 0:
        raise ValueError(f'Pydocstyle found {score} errors in python '
                         'docstrings. Please fix them.')
