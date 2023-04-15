"""Some code to be checked by linters, tests and so on."""


def add_integers(arg1: int, arg2: int) -> int:
    """Add two integers."""
    if not isinstance(arg1, int) or not isinstance(arg2, int):
        raise TypeError("arg1 and arg2 must be integers")
    return arg1 + arg2
