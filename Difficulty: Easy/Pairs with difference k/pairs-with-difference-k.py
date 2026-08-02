from collections import Counter

class Solution:
    def countPairs(self, arr, k):
        freq = Counter(arr)
        ans = 0

        for x in freq:
            if x + k in freq:
                ans += freq[x] * freq[x + k]

        return ans