import pytest
from calculator import add


def test_add_positive_numbers() -> None:
    """Test addition with positive integers"""
    assert add(2, 3) == 5
    assert add(100, 200) == 300


def test_add_with_zero() -> None:
    """Test addition with zero"""
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 5) == 5


def test_add_negative_numbers() -> None:
    """Test addition with negative numbers"""
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2
    assert add(5, -3) == 2


def test_add_floats() -> None:
    """Test addition with floating point numbers"""
    assert add(0.1, 0.2) == pytest.approx(0.3)
    assert add(1.5, 2.5) == 4.0


def test_add_large_numbers() -> None:
    """Test addition with large numbers"""
    assert add(1000000, 2000000) == 3000000
