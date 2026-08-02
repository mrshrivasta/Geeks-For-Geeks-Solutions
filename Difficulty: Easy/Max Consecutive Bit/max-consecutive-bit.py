class Solution:
    def maxConsecBits(self, arr):
        max_count = 1
        curr = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                curr += 1
            else:
                curr = 1
            max_count = max(max_count, curr)

        return max_count