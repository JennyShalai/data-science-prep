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
