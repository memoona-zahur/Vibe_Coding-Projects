"""
Command Line Interface for the calculator.
"""
import sys
import argparse
from typing import Union, List, Optional, NoReturn
from . import Calculator


class CalculatorCLI:
    """Command Line Interface for the calculator."""
    
    def __init__(self) -> None:
        self.calc = Calculator()
    
    def parse_arguments(self) -> argparse.Namespace:
        """Parse command line arguments."""
        parser = argparse.ArgumentParser(
            description="A command line calculator"
        )
        parser.add_argument(
            'operation',
            choices=['add', 'subtract', 'multiply', 'divide'],
            help='Operation to perform'
        )
        parser.add_argument(
            'numbers',
            nargs='*',
            help='Numbers to perform operation on (2 required)'
        )
        
        return parser.parse_args()
    
    def calculate(self, args: List[str]) -> Union[float, str]:
        """Perform calculation based on provided arguments."""
        if len(args) == 0:
            # If no arguments provided, return help text
            return self._get_help_text()
        
        operation = args[0]
        
        if operation in ['--help', '-h']:
            return self._get_help_text()
        
        if len(args) != 3:  # operation + 2 numbers
            raise ValueError(f"Operation {operation} requires exactly 2 numbers")
        
        try:
            num1 = float(args[1])
            num2 = float(args[2])
        except ValueError:
            raise ValueError("Invalid number format provided")
        
        # Perform the requested operation
        if operation == 'add':
            return self.calc.add(num1, num2)
        elif operation == 'subtract':
            return self.calc.subtract(num1, num2)
        elif operation == 'multiply':
            return self.calc.multiply(num1, num2)
        elif operation == 'divide':
            return self.calc.divide(num1, num2)
        else:
            raise ValueError(f"Unknown operation: {operation}")
    
    def _get_help_text(self) -> str:
        """Return help text."""
        return """
Calculator CLI Usage:
    python -m calculator <operation> <num1> <num2>

Operations:
    add       - Add two numbers
    subtract  - Subtract second number from first
    multiply  - Multiply two numbers
    divide    - Divide first number by second

Examples:
    python -m calculator add 5 3
    python -m calculator multiply 4.5 2
        """
    
    def _show_help(self) -> None:
        """Display help information."""
        print(self._get_help_text())
    
    def run(self, args: Optional[List[str]] = None) -> None:
        """Run the calculator CLI with given arguments."""
        if args is None:
            args = sys.argv[1:]
        
        try:
            if '--help' in args or '-h' in args:
                self._show_help()
                return
            
            if len(args) == 0:
                # Show help if no arguments provided
                self._show_help()
                return
            
            result = self.calculate(args)
            if isinstance(result, str):  # Help text
                print(result)
            else:  # Numeric result
                print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: Cannot divide by zero")


def main() -> None:
    """Main entry point for the calculator CLI."""
    cli = CalculatorCLI()
    cli.run()


if __name__ == "__main__":
    main()