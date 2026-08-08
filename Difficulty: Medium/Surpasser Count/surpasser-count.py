class Solution:
    def findSurpasser(self, arr):
        n = len(arr)
        ans = [0] * n

        sorted_vals = sorted(arr)
        rank = {value: i for i, value in enumerate(sorted_vals)}

        bit = [0] * (n + 1)

        def update(i):
            i += 1
            while i <= n:
                bit[i] += 1
                i += i & -i

        def query(i):
            total = 0
            while i > 0:
                total += bit[i]
                i -= i & -i
            return total

        for i in range(n - 1, -1, -1):
            r = rank[arr[i]]
            ans[i] = query(n) - query(r + 1)
            update(r)

        return ans