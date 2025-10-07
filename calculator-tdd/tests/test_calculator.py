"""Comprehensive tests for calculator functions."""
import pytest
from calculator import divide


def test_divide_positive_numbers() -> None:
    """Test division of positive numbers."""
    assert divide(10, 2) == 5.0


def test_divide_negative_numbers() -> None:
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_by_one() -> None:
    """Test division by one."""
    assert divide(5, 1) == 5.0
    assert divide(-5, 1) == -5.0


def test_divide_zero_by_number() -> None:
    """Test division of zero by a number."""
    assert divide(0, 5) == 0.0
    assert divide(0, -3) == 0.0


def test_divide_number_by_self() -> None:
    """Test division of a number by itself."""
    assert divide(5, 5) == 1.0
    assert divide(-5, -5) == 1.0


def test_divide_floating_point() -> None:
    """Test division with floating point numbers."""
    assert divide(7.5, 2.5) == 3.0
    assert abs(divide(10, 3) - 3.333333333333333) < 1e-10  # Test for precision


def test_divide_large_numbers() -> None:
    """Test division with large numbers."""
    assert divide(1000000, 1000) == 1000.0


def test_divide_small_numbers() -> None:
    """Test division with small numbers."""
    assert divide(0.1, 0.01) == 10.0


def test_divide_complex_operations() -> None:
    """Test more complex division operations."""
    result = divide(divide(100, 2), 5)
    assert result == 10.0


def test_divide_by_zero() -> None:
    """Test division by zero - this should be handled properly."""
    # This test expects a ZeroDivisionError to be raised
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_divide_zero_by_zero() -> None:
    """Test zero divided by zero - this should raise ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(0, 0)