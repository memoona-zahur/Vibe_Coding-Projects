# Calculator

A Python calculator library built with TDD (Test-Driven Development) approach. This library provides basic arithmetic operations with proper error handling and validation.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division
- Error handling for invalid inputs and operations (e.g., division by zero)
- Type validation for numeric inputs
- Command-line interface for quick calculations
- Comprehensive test suite following TDD principles
- Proper handling of special float values (NaN, infinity)

## Installation

This project requires Python 3.12 or higher. Make sure you have both Python 3.12+ and [UV](https://github.com/astral-sh/uv) installed.

To install the dependencies for this project using UV:

```bash
uv sync
```

To activate the virtual environment:

```bash
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

## Supported Platforms

This calculator library is compatible with:
- Linux (including WSL)
- macOS
- Windows

The library works with Python 3.12 or higher and uses UV for package management.

## Usage

### Module Import

You can import and use the calculator directly in your Python projects:

```python
from calculator import Calculator, add, subtract, multiply, divide

# Using the Calculator class
calc = Calculator()
result = calc.add(5, 3)
print(result)  # Output: 8

# Using individual functions
result = add(10, 5)
print(result)  # Output: 15

result = multiply(4, 7)
print(result)  # Output: 28
```

### Command-Line Interface (CLI)

You can perform calculations directly from the command line:

```bash
# Addition
python -m calculator add 5 3
# Output: Result: 8.0

# Subtraction
python -m calculator subtract 10 4
# Output: Result: 6.0

# Multiplication
python -m calculator multiply 6 7
# Output: Result: 42.0

# Division
python -m calculator divide 15 3
# Output: Result: 5.0

# Show help
python -m calculator --help
```

## Running Tests

To run the test suite:

```bash
uv run pytest
```

To run tests with coverage:

```bash
uv run pytest --cov=calculator
```

To run a specific test file:

```bash
uv run pytest tests/test_calculator.py
```

## Operations Examples

### Addition
```python
from calculator import Calculator
calc = Calculator()

# Basic addition
result = calc.add(5, 3)
print(result)  # Output: 8.0

# With floating point numbers
result = calc.add(2.5, 3.7)
print(result)  # Output: 6.2

# Error handling
try:
    result = calc.add("5", 3)
except TypeError as e:
    print(f"Error: {e}")
```

### Subtraction
```python
from calculator import Calculator
calc = Calculator()

# Basic subtraction
result = calc.subtract(10, 4)
print(result)  # Output: 6.0

# With floating point numbers
result = calc.subtract(5.5, 2.2)
print(result)  # Output: 3.3
```

### Multiplication
```python
from calculator import Calculator
calc = Calculator()

# Basic multiplication
result = calc.multiply(3, 4)
print(result)  # Output: 12.0

# With floating point numbers
result = calc.multiply(2.5, 4.0)
print(result)  # Output: 10.0

# Error handling for NaN
import math
try:
    result = calc.multiply(math.nan, 5)
except ValueError as e:
    print(f"Error: {e}")
```

### Division
```python
from calculator import Calculator
calc = Calculator()

# Basic division
result = calc.divide(10, 2)
print(result)  # Output: 5.0

# With floating point numbers
result = calc.divide(7.5, 2.5)
print(result)  # Output: 3.0

# Error handling for division by zero
try:
    result = calc.divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

## Development

This project uses test-driven development. All tests are located in the `tests/` directory. Before implementing any new features, write tests first to ensure proper functionality and maintain code quality.
