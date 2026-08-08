class Solution:
    def sameFreq(self, s):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        counts = [f for f in freq if f > 0]

        if len(set(counts)) == 1:
            return True

        for i in range(26):
            if freq[i] > 0:
                freq[i] -= 1

                new_counts = [f for f in freq if f > 0]

                if len(new_counts) > 0 and len(set(new_counts)) == 1:
                    return True

                freq[i] += 1

        return False