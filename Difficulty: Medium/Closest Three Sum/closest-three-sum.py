class Solution:
    def closest3Sum(self, arr, target):
        arr.sort()
        n = len(arr)

        best = arr[0] + arr[1] + arr[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if abs(total - target) < abs(best - target):
                    best = total
                elif abs(total - target) == abs(best - target):
                    best = max(best, total)

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return best