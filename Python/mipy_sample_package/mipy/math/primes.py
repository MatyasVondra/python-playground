"""
This module contains some simple functions that work with primes.
"""

from typing import List


def is_prime(n: int) -> bool:
    """Checks where the given number is a prime
    
    No sophisticated algorithm is used, just checking divisibility.
    
    Args:
        n (int): input number - prime suspect
    
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
    
    
def get_primes(numbers: List[int]) -> List[int]:
    """Returns a list of primes from a given list of numbers.
    
    Args:
        numbers (List[int]): list of numbers to be examined
    
    Returns:
        List[int]: primes from the original list
    
    """
    return [num for num in numbers if is_prime(num)]
