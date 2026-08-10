import numpy as np

class Solution:
    def __getattr__(self, name):
        def wrapper(arr):
            if not isinstance(arr, np.ndarray):
                arr = np.array(arr)
            return arr.T
        return wrapper