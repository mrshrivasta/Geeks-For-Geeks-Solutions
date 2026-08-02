class Solution:
    def fourSum(self, arr, x):
        n = len(arr)
        pair_sum = {}

        for i in range(n):
            for j in range(i + 1, n):
                curr = arr[i] + arr[j]
                need = x - curr

                if need in pair_sum:
                    for a, b in pair_sum[need]:
                        if a != i and a != j and b != i and b != j:
                            return True

                if curr not in pair_sum:
                    pair_sum[curr] = []
                pair_sum[curr].append((i, j))

        return False