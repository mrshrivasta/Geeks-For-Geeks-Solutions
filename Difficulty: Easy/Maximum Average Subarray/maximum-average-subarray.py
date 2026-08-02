class Solution:
    def findMaxAverage(self, arr, k):
        curr_sum = sum(arr[:k])
        max_sum = curr_sum
        ans = 0

        for i in range(k, len(arr)):
            curr_sum += arr[i] - arr[i - k]
            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = i - k + 1

        return ans