class Solution:
    def countTriplets(self, arr, l, r):
        arr.sort()

        def count(x):
            n = len(arr)
            ans = 0

            for i in range(n - 2):
                left, right = i + 1, n - 1
                while left < right:
                    if arr[i] + arr[left] + arr[right] <= x:
                        ans += right - left
                        left += 1
                    else:
                        right -= 1
            return ans

        return count(r) - count(l - 1)