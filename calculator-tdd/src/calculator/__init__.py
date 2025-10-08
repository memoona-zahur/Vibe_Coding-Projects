class Calculator:
    """A basic calculator class with arithmetic operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers."""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract second number from first number."""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers."""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide first number by second number."""
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
