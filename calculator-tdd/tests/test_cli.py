"""
Comprehensive tests for the Calculator CLI interface.

Testing Strategy:
- Test each operation (add, subtract, multiply, divide)
- Test various input types (integers, floats)
- Test error conditions (division by zero, invalid input)
- Test help and invalid command handling
"""

import sys
from io import StringIO
from unittest.mock import patch
import pytest
from src.calculator import Calculator


def test_cli_add_operation() -> None:
    """Test the add operation through the CLI."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Simulate command line arguments for addition
    result = cli.calculate(['add', '5', '3'])
    assert result == 8.0


def test_cli_subtract_operation() -> None:
    """Test the subtract operation through the CLI."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Simulate command line arguments for subtraction
    result = cli.calculate(['subtract', '10', '4'])
    assert result == 6.0


def test_cli_multiply_operation() -> None:
    """Test the multiply operation through the CLI."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Simulate command line arguments for multiplication
    result = cli.calculate(['multiply', '6', '7'])
    assert result == 42.0


def test_cli_divide_operation() -> None:
    """Test the divide operation through the CLI."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Simulate command line arguments for division
    result = cli.calculate(['divide', '15', '3'])
    assert result == 5.0


def test_cli_division_by_zero() -> None:
    """Test that division by zero is handled properly."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Should raise an appropriate error when dividing by zero
    with pytest.raises(ZeroDivisionError):
        cli.calculate(['divide', '10', '0'])


def test_cli_invalid_operation() -> None:
    """Test handling of invalid operation names."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Should raise an error for invalid operation
    with pytest.raises(ValueError):
        cli.calculate(['invalid_op', '5', '3'])


def test_cli_invalid_numbers() -> None:
    """Test handling of invalid number inputs."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Should raise an error for non-numeric inputs
    with pytest.raises(ValueError):
        cli.calculate(['add', 'abc', '3'])


def test_cli_insufficient_arguments() -> None:
    """Test handling of insufficient arguments."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Should raise an error if insufficient arguments provided
    with pytest.raises(ValueError):
        cli.calculate(['add', '5'])


def test_cli_help_option() -> None:
    """Test the help option."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Should return help text when requested
    result = cli.calculate(['--help'])
    assert 'usage' in result.lower() or 'help' in result.lower()


def test_cli_integer_inputs() -> None:
    """Test CLI with integer inputs."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    result = cli.calculate(['add', '10', '20'])
    assert result == 30.0


def test_cli_float_inputs() -> None:
    """Test CLI with float inputs."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    result = cli.calculate(['multiply', '2.5', '4.0'])
    assert result == 10.0


def test_cli_negative_numbers() -> None:
    """Test CLI with negative numbers."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    result = cli.calculate(['subtract', '-5', '-10'])
    assert result == 5.0


def test_cli_large_numbers() -> None:
    """Test CLI with large numbers."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    large_num = '1000000'
    result = cli.calculate(['add', large_num, large_num])
    assert result == 2000000.0


def test_cli_zero_inputs() -> None:
    """Test CLI with zero inputs."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    result = cli.calculate(['multiply', '0', '5'])
    assert result == 0.0


def test_cli_output_format() -> None:
    """Test that CLI outputs results in expected format."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Test output format when running the CLI
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.run(['add', '2', '3'])
        output = fake_out.getvalue().strip()
        # Should output the result in a readable format
        assert '5.0' in output


def test_cli_error_messages() -> None:
    """Test that CLI displays appropriate error messages."""
    from src.calculator.__main__ import CalculatorCLI
    cli = CalculatorCLI()
    # Test error message display
    with patch('sys.stdout', new=StringIO()) as fake_out:
        cli.run(['divide', '10', '0'])
        output = fake_out.getvalue().strip()
        # Should contain an error message about division by zero
        assert 'error' in output.lower() or 'zero' in output.lower()


if __name__ == "__main__":
    pytest.main()