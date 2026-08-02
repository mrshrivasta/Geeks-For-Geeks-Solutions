class Solution:
    def leftCandies(self, n, m):
        cycle = n * (n + 1) // 2

        m %= cycle

        for i in range(1, n + 1):
            if m >= i:
                m -= i
            else:
                break

        return m