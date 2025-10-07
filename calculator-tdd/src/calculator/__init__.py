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
