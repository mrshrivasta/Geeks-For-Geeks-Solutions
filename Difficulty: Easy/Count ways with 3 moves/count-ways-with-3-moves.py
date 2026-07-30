class Solution:
    def countWays(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4

        a, b, c = 1, 2, 4
        for _ in range(4, n + 1):
            a, b, c = b, c, a + b + c

        return c