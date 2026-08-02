class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        last = {}

        for i, x in enumerate(arr):
            if x in last and i - last[x] <= k:
                return True
            last[x] = i

        return False