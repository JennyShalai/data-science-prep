# Python NUMPY

# Challenge 1:
# Use boolean indexing to return the elements of an array that are
# greater than or equal to two times the minimum element of the array.

import numpy as np

def elements_twice_min(arr):
    """
        Return all elements of array arr that are greater than or equal to 2 times
        the minimum element of arr.
        
        Parameters
        ----------
        arr: NumPy array (n, m)
        
        Returns
        -------
        NumPy Array, a vector of size between: 0 and (n * m) - 1
        """
    return arr[arr >= np.amin(arr) * 2]


# Challenge 2:
# Add two NumPy vectors or matrices together, if possible.
# If it is not possible to add the two vectors/matrices together
# (because their sizes differ), return False.

import numpy as np

def mat_addition(A, B):
    """
        Add vector/matrix arrays A and B together. If they cannot be added
        return False.
        
        Parameters
        ----------
        A: NumPy array size of (n,) or (n, m)
        B: NumPy array size of (p,) or (p, q)
        
        Returns
        -------
        NumPy Array of same size as A and B, or False if their sizes differ.
        """
    if A.shape == B. shape:
        return A + B
    else:
        return False
