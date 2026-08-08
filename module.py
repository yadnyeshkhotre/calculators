def modulo(a,b):
    """
    Returns the remainder of the division of a by b.
    
    Parameters:
    a (int or float): The dividend.
    b (int or float): The divisor.
    
    Returns:
    int or float: The remainder of the division.
    
    Raises:
    ValueError: If b is zero, as division by zero is undefined.
    """
    if b == 0:
        raise ValueError("The divisor 'b' cannot be zero.")
    return a % b