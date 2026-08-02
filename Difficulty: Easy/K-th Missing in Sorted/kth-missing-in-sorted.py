class Solution:
    def KthMissingElement(self, arr, k):
        for i in range(1, len(arr)):
            gap = arr[i] - arr[i - 1] - 1
            if k <= gap:
                return arr[i - 1] + k
            k -= gap
        return -1