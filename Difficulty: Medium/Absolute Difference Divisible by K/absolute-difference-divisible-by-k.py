class Solution:
    @staticmethod
    def countPairs(arr, k):
        freq = {}
        ans = 0

        for num in arr:
            rem = num % k

            if rem in freq:
                ans += freq[rem]

            freq[rem] = freq.get(rem, 0) + 1

        return ans