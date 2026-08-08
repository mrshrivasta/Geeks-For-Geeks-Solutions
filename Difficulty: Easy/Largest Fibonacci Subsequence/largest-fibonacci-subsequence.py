class Solution:
    def findFibSubset(self, arr):
        max_val = max(arr)

        fib = set()
        a, b = 0, 1

        while a <= max_val:
            fib.add(a)
            a, b = b, a + b

        return [x for x in arr if x in fib]