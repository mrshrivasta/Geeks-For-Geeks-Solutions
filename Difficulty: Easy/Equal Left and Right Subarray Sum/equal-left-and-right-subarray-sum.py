class Solution:
    def equalSum(self, arr):
        total = sum(arr)
        left = 0

        for i in range(len(arr)):
            total -= arr[i]
            if left == total:
                return i
            left += arr[i]

        return -1