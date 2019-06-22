# Functions checkpoint


# Challenge 1:
def get_divisors(n):
    '''
        This function calculates and returns all of the divisors of n, between 1 and
        n, inclusive.
        Parameters
        ----------
        n: {int}
        Returns
        -------
        divisors: {list} all divisors of n in order from smallest to largest
        '''
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result


# Challenge 2:
def factorialn):
    '''
        Returns the factorial of the input integer:
        n * (n - 1) * (n - 2) * ... * 2 * 1
        Parameters
        ----------
        n: {int} number to compute factorial of (must be greater than 0)
        
        Returns
        -------
        n!: {int} factorial of n
        
        '''
    result = n
    while n > 2:
        result = result * (n - 1)
        n -= 1
    return result


# Challenge 3:
def is_prime(n):
    '''
        Return True if the input is prime, False otherwise
        Parameters
        ----------
        n: {int} input integer
        
        Returns
        -------
        is_prime: {bool} whether n is prime
        '''
    result = True
    for i in range(2, n - 1):
        if n % i == 0:
            result = False
            break
    return result


# Challenge 4:
'''As you write your own functions you will often call other functions from within them.
    Your task here is complete the function next_perfect_square.

    A number is a perfect square if it is the square of an integer, e.g. 9 = 3 * 3.
    For the following question, you have access to the function is_perfect_square,
    which returns True if the number is a perfect square, and False if it is not.
    Use this function to fill out the code stub below.'''

from math import sqrt
def next_perfect_square(number):
    '''
        Returns the next perfect square of the input number, if the input number
        is not a perfect square, returns -1.
        Ex:
        next_perfect_square(10)
        >>> -1
        next_perfect_square(9)
        >>> 16
        next_perfect_square(25)
        >>> 36
        next_perfect_square(37)
        >>> -1
        
        Parameters
        ----------
        number: {int}
        
        Returns
        -------
        next_perfect: {int} the next perfect square, or -1 if number is not a
        perfect square
        '''
    if is_perfect_square(number):
        n = sqrt(number)
        return (n+1)*(n+1)
    else:
        return -1


# Challenge 5:
import random
def flip_coin(p=0.5):
    '''
        Using random.random() simulate flipping a coin where the probability of
        flipping a head is p.
        
        Parameters
        ----------
        p: {float} probability of flipping a head (must be between 0 and 1)
        
        Returns
        -------
        flip: {str} "H" if coin is heads, otherwise "T"
        '''
    n = random.random()
    if n < p:
        return 'H'
    else:
        return 'T'
