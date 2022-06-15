"""Unitary tests for src/some_code.py."""
import pytest

from src.some_code import add_integers


def test_add_integers():
    """Test add_integers function."""
    # Correct use case
    out = add_integers(5, -8)
    assert isinstance(out, int)

    # Wrong use case
    with pytest.raises(TypeError, match='.*integer.*'):
        add_integers(0, 0.5)
