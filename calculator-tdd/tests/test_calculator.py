from src.calculator import subtract


def test_subtract_positive_numbers() -> None:
    """Test subtraction of two positive numbers."""
    assert subtract(5, 3) == 2


def test_subtract_negative_result() -> None:
    """Test subtraction that results in a negative number."""
    assert subtract(3, 5) == -2


def test_subtract_with_zero() -> None:
    """Test subtraction involving zero."""
    assert subtract(5, 0) == 5
    assert subtract(0, 5) == -5
    assert subtract(0, 0) == 0


def test_subtract_negative_numbers() -> None:
    """Test subtraction of negative numbers."""
    assert subtract(-5, -3) == -2
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8


def test_subtract_floating_point() -> None:
    """Test subtraction with floating point numbers."""
    assert abs(subtract(5.5, 2.2) - 3.3) < 1e-9
    assert abs(subtract(0.1, 0.2) - (-0.1)) < 1e-9


def test_subtract_large_numbers() -> None:
    """Test subtraction with very large numbers."""
    assert subtract(1000000, 1) == 999999
    assert subtract(1, 1000000) == -999999


def test_subtract_same_numbers() -> None:
    """Test subtraction of identical numbers (should equal zero)."""
    assert subtract(5, 5) == 0
    assert subtract(-3, -3) == 0
    assert subtract(0, 0) == 0


def test_subtract_decimal_precision() -> None:
    """Test subtraction with decimal precision."""
    result = subtract(0.3, 0.1)
    expected = 0.2
    assert abs(result - expected) < 1e-9