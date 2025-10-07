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
