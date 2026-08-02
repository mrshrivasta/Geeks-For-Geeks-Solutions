class Solution:
    def minSoldiers(self, arr, k):
        lucky = 0
        cost = []

        for x in arr:
            if x % k == 0:
                lucky += 1
            else:
                cost.append(k - (x % k))

        need = (len(arr) + 1) // 2

        if lucky >= need:
            return 0

        cost.sort()
        return sum(cost[:need - lucky])