"""Manage Pydocstyle output on worflow."""
import sys


def check_output() -> None:
    """Check output of Pydocstyle.

    Raises
    ------
    ValueError
        If Pydocstyle find errors.
    """
    args = sys.argv[1:]
    for arg in args:
        if arg.startswith('--n_errors='):
            n_errors = float(arg.split('=')[1])

    raise ValueError(f'Pydocstyle found {n_errors} errors in python '
                     'docstrings. Please fix them.')


if __name__ == '__main__':
    check_output()
