class Solution:
    def countSort(self, s):
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(26):
            ans.append(chr(i + ord('a')) * count[i])

        return "".join(ans)