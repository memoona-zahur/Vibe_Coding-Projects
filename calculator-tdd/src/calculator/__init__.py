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
        return a + b
    
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
        return a - b
    
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
        return a * b
    
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
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


def hello() -> str:
    return "Hello from calculator!"


def divide(a: int | float, b: int | float) -> float:
    """Divide a by b and return the result.
    
    Args:
        a: Numerator (int or float)
        b: Denominator (int or float)
        
    Returns:
        Quotient of a and b (always float)
    """
    return a / b
def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiply two numbers and return the result.
    
    Args:
        a: The first number
        b: The second number
        
    Returns:
        The product of a and b
    """
    return a * b
def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers and return the result."""
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract b from a and return the result.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float)
        
    Returns:
        Difference of a and b (int or float)
    """
    return a - b
