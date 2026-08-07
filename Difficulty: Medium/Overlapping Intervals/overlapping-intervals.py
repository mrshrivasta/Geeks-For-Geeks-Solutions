class Solution:
    def mergeOverlap(self, arr):
        arr.sort()
        res = []

        for interval in arr:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res
        