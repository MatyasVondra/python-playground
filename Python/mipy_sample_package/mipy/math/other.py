"""
This module is a collection of math tools, that did not fit anywhere else.
"""


def faktorial(n: int) -> int:
    """Calculates the factorial of number n
    
    Args:
        n (int): given integer
        
    Returns:
        int: n!
    """
    if n < 0:
        print("not defined for negative numbers")
    elif n == 0:
        return 1
    else:
        fak = 1
        for i in range(2, n+1):
            fak *= i
        return fak

    
    
def polynom(x, *coefs):
    """Evaluates polynomial with coefficients coef at point x.
    
    Args:
        x (int | float | complex): point at which the polynomial is evaluated.
        coefs (int | float | complex): coefficients of the polynomial, from the lowest term to the highest
    
    Returns
        int | float | complex: Value of the polynomial at point x
    """
    val = 0.0
    for i, coef in enumerate(coefs):
        val += coef * x**i
    return val


def solve_quadratic_equation(*, a: int | float, b: int | float, c: int | float):
    """ Returns the real solutions to equation ax^2 + bx + c = 0
    
    Always returns a tuple of values.
    
    Args:
        a (int | float): quadratic term coefficient. Must be non-zero
        b (int | float): linear term coefficient.
        c (int | float): absolute term coefficient
        
    Returns:
        Tuple: Containing the solutions of the equation.
        
        Containing two floats, if one or two real solutions exist
        
        Containing two Nones, if no real solution exists.
        
    Raises:
        ValueError: if coefficient a is zero.
    
    """
    if abs(a) < 1e-14:
        raise ValueError("Coefficient 'a' must not be zero.")

    D = b**2 - 4 * a * c
    if abs(D) < 1e-14:
        return -b / (2 * a), -b / (2 * a)
    elif D > 0.0:
        return (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)
    else:
        return None, None
