import heapq

class Solution:
    def getMedian(self, arr):
        left = []    # max heap (store negative values)
        right = []   # min heap
        ans = []

        for num in arr:
            if not left or num <= -left[0]:
                heapq.heappush(left, -num)
            else:
                heapq.heappush(right, num)

            if len(left) > len(right) + 1:
                heapq.heappush(right, -heapq.heappop(left))
            elif len(right) > len(left):
                heapq.heappush(left, -heapq.heappop(right))

            if len(left) == len(right):
                ans.append((-left[0] + right[0]) / 2.0)
            else:
                ans.append(float(-left[0]))

        return ans