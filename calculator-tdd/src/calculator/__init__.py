def hello() -> str:
    return "Hello from calculator!"


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
