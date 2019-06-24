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

