class Solution:
    def findPairs(self, arr):
        seen = set()
        n = len(arr)

        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                if s in seen:
                    return True
                seen.add(s)

        return False