class Solution:
    def maxLen(self, arr):
        first = {0: -1}
        balance = 0
        ans = 0

        for i, num in enumerate(arr):
            balance += 1 if num == 1 else -1

            if balance in first:
                ans = max(ans, i - first[balance])
            else:
                first[balance] = i

        return ans