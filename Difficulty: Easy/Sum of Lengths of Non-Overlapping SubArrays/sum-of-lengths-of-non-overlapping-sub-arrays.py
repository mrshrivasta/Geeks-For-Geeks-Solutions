class Solution:
    def calculateMaxSumLength(self, arr, k):
        ans = 0
        n = len(arr)
        i = 0

        while i < n:
            while i < n and arr[i] > k:
                i += 1

            if i >= n:
                break

            j = i
            has_k = False

            while j < n and arr[j] <= k:
                if arr[j] == k:
                    has_k = True
                j += 1

            if has_k:
                ans += (j - i)

            i = j

        return ans