class Solution:
    def findMissing(self, a, b):
        s = set(b)
        ans = []

        for x in a:
            if x not in s:
                ans.append(x)

        return ans