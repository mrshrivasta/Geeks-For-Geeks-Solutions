class Solution:
    def findMax(self, arr):
        ans = 0
        for h in arr:
            ans = max(ans, h.feet * 12 + h.inches)
        return ans