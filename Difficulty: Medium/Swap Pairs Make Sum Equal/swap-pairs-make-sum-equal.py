class Solution:
    def findSwapValues(self, a, b):
        sum_a = sum(a)
        sum_b = sum(b)

        diff = sum_a - sum_b

        if diff % 2 != 0:
            return False

        target = diff // 2
        values = set(b)

        for x in a:
            if x - target in values:
                return True

        return False