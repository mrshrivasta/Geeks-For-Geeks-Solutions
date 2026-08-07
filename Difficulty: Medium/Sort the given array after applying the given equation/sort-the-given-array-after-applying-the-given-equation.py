class Solution:
    def sortArray(self, arr, A, B, C):
        def f(x):
            return A * x * x + B * x + C

        return sorted(f(x) for x in arr)