import math


class Calculator:
    """A basic calculator class with arithmetic operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        # Validate inputs
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Cannot add {type(a).__name__} and {type(b).__name__}")
        
        # Check for special float values
        if math.isnan(a) or math.isnan(b):
            raise ValueError("Cannot perform operation with NaN value")
        
        # Perform the calculation
        result = a + b
        
        # Convert result to float, handling very large numbers gracefully
        try:
            return float(result)
        except OverflowError:
            # If the result is too large to represent as a finite float, return infinity
            return float('inf')
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract second number from first number."""
        # Validate inputs
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Cannot subtract {type(b).__name__} from {type(a).__name__}")
        
        # Check for special float values
        if math.isnan(a) or math.isnan(b):
            raise ValueError("Cannot perform operation with NaN value")
        
        # Perform the calculation
        result = a - b
        
        # Convert result to float, handling very large numbers gracefully
        try:
            return float(result)
        except OverflowError:
            # If the result is too large to represent as a finite float, return infinity
            return float('inf')
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        # Validate inputs
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Cannot multiply {type(a).__name__} and {type(b).__name__}")
        
        # Check for special float values
        if math.isnan(a) or math.isnan(b):
            raise ValueError("Cannot perform operation with NaN value")
        
        # Convert inputs to float first to avoid integer overflow during operations
        try:
            float_a = float(a)
            float_b = float(b)
        except OverflowError:
            raise OverflowError("Input value too large to convert to float")
        
        # Perform the calculation with floats
        result = float_a * float_b
        
        # Check for NaN in result
        if math.isnan(result):
            raise ValueError("Result is not a number (NaN)")
        
        return result
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide first number by second number."""
        # Validate inputs
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"Cannot divide {type(a).__name__} by {type(b).__name__}")
        
        # Check for special float values
        if math.isnan(a) or math.isnan(b):
            raise ValueError("Cannot perform operation with NaN value")
        
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        # Perform the calculation
        result = a / b
        
        # Convert result to float (this should typically work since division of floats returns float)
        # But handle any edge cases
        try:
            return float(result)
        except OverflowError:
            # If the result is too large to represent as a finite float, return infinity
            return float('inf')


def hello() -> str:
    return "Hello from calculator!"
