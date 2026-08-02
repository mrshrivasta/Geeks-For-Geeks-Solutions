class Solution:
    def firstNonRepeating(self, arr):
        freq = {}

        # Count frequency of each element
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Find the first element with frequency 1
        for num in arr:
            if freq[num] == 1:
                return num

        return 0