class Solution:
    def getMaxOccuringChar(self, s):
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        ans = 0
        for i in range(1, 26):
            if freq[i] > freq[ans]:
                ans = i

        return chr(ans + ord('a'))