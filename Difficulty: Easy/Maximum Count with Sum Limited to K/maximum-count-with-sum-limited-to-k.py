class Solution:
    def toyCount(self, arr, k):
        arr.sort()
        count = 0

        for cost in arr:
            if cost > k:
                break
            k -= cost
            count += 1

        return count