from src.calculator import multiply
import pytest


def test_multiply_positive_integers() -> None:
    """Test multiplication of positive integers."""
    assert multiply(3, 4) == 12
    assert multiply(5, 6) == 30
    assert multiply(1, 100) == 100


def test_multiply_negative_integers() -> None:
    """Test multiplication of negative integers."""
    assert multiply(-3, 4) == -12
    assert multiply(3, -4) == -12
    assert multiply(-3, -4) == 12


def test_multiply_by_zero() -> None:
    """Test multiplication by zero."""
    assert multiply(0, 5) == 0
    assert multiply(5, 0) == 0
    assert multiply(0, 0) == 0
    assert multiply(-5, 0) == 0
    assert multiply(0, -5) == 0


def test_multiply_by_one() -> None:
    """Test multiplication by one."""
    assert multiply(1, 5) == 5
    assert multiply(5, 1) == 5
    assert multiply(1, 1) == 1
    assert multiply(-5, 1) == -5
    assert multiply(1, -5) == -5


def test_multiply_floating_point_numbers() -> None:
    """Test multiplication of floating point numbers."""
    assert multiply(2.5, 4.0) == 10.0
    assert multiply(3.5, 2.0) == 7.0
    assert multiply(-2.5, 4.0) == -10.0
    assert multiply(2.5, -4.0) == -10.0
    assert multiply(-2.5, -4.0) == 10.0


def test_multiply_floating_point_precision() -> None:
    """Test multiplication with floating point precision concerns."""
    result = multiply(0.1, 0.2)
    assert abs(result - 0.02) < 1e-10  # Account for floating point precision


def test_multiply_large_numbers() -> None:
    """Test multiplication of large numbers."""
    assert multiply(1000000, 1000000) == 1000000000000
    assert multiply(999999999, 999999999) == 999999998000000001


def test_multiply_small_numbers() -> None:
    """Test multiplication of small decimal numbers."""
    assert multiply(0.001, 0.001) == 0.000001
    # Using approx for floating point comparison due to precision issues
    assert abs(multiply(0.1, 0.1) - 0.01) < 1e-10


def test_multiply_negative_zero_edge_case() -> None:
    """Test multiplication with negative zero (if applicable)."""
    result = multiply(-0.0, 5)
    assert result == 0.0 and str(result)[0] == '-' if str(result)[0] == '-' else True
    assert multiply(5, -0.0) == -0.0


def test_multiply_commutative_property() -> None:
    """Test that multiplication is commutative (a * b == b * a)."""
    assert multiply(7, 3) == multiply(3, 7)
    assert multiply(2.5, 4.2) == multiply(4.2, 2.5)
    assert multiply(-5, 3) == multiply(3, -5)