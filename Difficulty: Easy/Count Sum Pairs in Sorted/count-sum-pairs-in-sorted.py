class Solution:
    def countPairs(self, arr, target):
        left, right = 0, len(arr) - 1
        count = 0

        while left < right:
            s = arr[left] + arr[right]

            if s == target:
                if arr[left] == arr[right]:
                    n = right - left + 1
                    count += n * (n - 1) // 2
                    break

                lcnt = 1
                rcnt = 1

                while left + 1 < right and arr[left] == arr[left + 1]:
                    lcnt += 1
                    left += 1

                while right - 1 > left and arr[right] == arr[right - 1]:
                    rcnt += 1
                    right -= 1

                count += lcnt * rcnt
                left += 1
                right -= 1

            elif s < target:
                left += 1
            else:
                right -= 1

        return count