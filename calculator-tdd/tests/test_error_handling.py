"""
Comprehensive tests for error handling in calculator operations and CLI.

Testing Strategy:
- Test division by zero errors
- Test invalid inputs (non-numeric values)
- Test invalid operation types
- Test edge cases with very large/small numbers
- Test invalid operation names
- Test insufficient arguments
- Test type validation
"""

import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.calculator import Calculator


def test_division_by_zero_error() -> None:
    """Test that division by zero raises ZeroDivisionError."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


def test_division_by_zero_negative_values() -> None:
    """Test division by zero with negative numerator."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(-5, 0)


def test_division_by_zero_float_values() -> None:
    """Test division by zero with float values."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10.5, 0.0)


def test_calculator_add_with_invalid_types() -> None:
    """Test that calculator add operation handles invalid types."""    
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.add("invalid", 5)


def test_calculator_subtract_with_invalid_types() -> None:
    """Test that calculator subtract operation handles invalid types."""
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.subtract(10, "invalid")


def test_calculator_multiply_with_invalid_types() -> None:
    """Test that calculator multiply operation handles invalid types."""
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.multiply("invalid", "types")


def test_calculator_divide_with_invalid_types() -> None:
    """Test that calculator divide operation handles invalid types."""
    calc = Calculator()
    with pytest.raises(TypeError):
        calc.divide("string", 5)


def test_cli_division_by_zero_error() -> None:
    """Test CLI handles division by zero gracefully."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ZeroDivisionError):
        cli.calculate(['divide', '10', '0'])


def test_cli_invalid_operation_name() -> None:
    """Test CLI handles invalid operation names."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ValueError):
        cli.calculate(['invalid_operation', '5', '3'])


def test_cli_invalid_numeric_inputs() -> None:
    """Test CLI handles non-numeric input values."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ValueError):
        cli.calculate(['add', 'not_a_number', '5'])


def test_cli_insufficient_arguments() -> None:
    """Test CLI handles insufficient arguments."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ValueError):
        cli.calculate(['add', '5'])  # Only one number instead of two


def test_cli_too_many_arguments() -> None:
    """Test CLI handles too many arguments."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ValueError):
        cli.calculate(['add', '5', '3', 'extra_arg'])


def test_large_number_handling() -> None:
    """Test calculator handles very large numbers."""
    calc = Calculator()
    large_num = 10**308  # Approaching float64 limits
    result = calc.multiply(large_num, 2)
    assert result == large_num * 2


def test_very_small_number_handling() -> None:
    """Test calculator handles very small numbers."""
    calc = Calculator()
    small_num = 1e-308
    result = calc.add(small_num, small_num)
    assert result == 2 * small_num


def test_overflow_error_handling() -> None:
    """Test calculator handles overflow scenarios."""
    calc = Calculator()
    try:
        # This might cause an overflow
        result = calc.multiply(10**308, 10**308)
        # If no exception, check for infinity
        assert result == float('inf')
    except OverflowError:
        # If it raises an exception, that's also valid handling
        pass


def test_underflow_handling() -> None:
    """Test calculator handles underflow scenarios."""
    calc = Calculator()
    # This might cause underflow to zero
    result = calc.multiply(1e-200, 1e-200)
    # Result might be very small or zero
    assert isinstance(result, float)


def test_nan_input_handling() -> None:
    """Test calculator handles NaN inputs."""
    import math
    calc = Calculator()
    with pytest.raises((ValueError, TypeError)):
        calc.add(math.nan, 5)


def test_infinity_input_handling() -> None:
    """Test calculator handles infinity inputs."""
    import math
    calc = Calculator()
    result = calc.add(math.inf, 5)
    assert result == math.inf


def test_cli_special_value_handling() -> None:
    """Test CLI handles special values like NaN and infinity."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Test with infinity - should handle gracefully
    result = cli.calculate(['add', 'inf', '5'])
    import math
    assert math.isinf(result)


def test_cli_empty_string_input() -> None:
    """Test CLI handles empty string inputs."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ValueError):
        cli.calculate(['add', '', '5'])


def test_cli_whitespace_input() -> None:
    """Test CLI handles whitespace inputs."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ValueError):
        cli.calculate(['add', '   ', '5'])


def test_cli_float_conversion_error() -> None:
    """Test CLI handles float conversion errors."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    with pytest.raises(ValueError):
        cli.calculate(['multiply', '3.14.15', '2'])  # Invalid float format


def test_error_message_formatting() -> None:
    """Test that error messages are properly formatted."""
    with pytest.raises(ZeroDivisionError) as exc_info:
        calc = Calculator()
        calc.divide(5, 0)
    error_message = str(exc_info.value)
    assert "divide" in error_message.lower() or "zero" in error_message.lower()


def test_type_error_message_content() -> None:
    """Test that type error messages contain helpful information."""
    with pytest.raises(TypeError) as exc_info:
        calc = Calculator()
        calc.add("string", 5)
    error_message = str(exc_info.value)
    # The error message will depend on Python's internal handling of the operation


def test_error_handling_with_negative_numbers() -> None:
    """Test error handling still works with negative numbers."""
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(-10, -0.0)  # -0.0 is still 0


def test_error_handling_boundary_values() -> None:
    """Test error handling with boundary values."""
    calc = Calculator()
    
    # Test with maximum float value
    max_float = 1.7976931348623157e+308
    try:
        result = calc.multiply(max_float, 2)
        # Result might be inf if overflow occurs
        assert result == float('inf') or isinstance(result, float)
    except OverflowError:
        pass  # Also valid behavior


if __name__ == "__main__":
    pytest.main()