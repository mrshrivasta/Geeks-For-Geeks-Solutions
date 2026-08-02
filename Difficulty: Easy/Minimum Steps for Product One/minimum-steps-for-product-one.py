class Solution:
    def makeProductOne(self, arr, N):
        steps = 0
        neg = 0
        zeros = 0

        for x in arr:
            if x > 0:
                steps += x - 1
            elif x < 0:
                steps += -1 - x
                neg += 1
            else:
                zeros += 1
                steps += 1

        if neg % 2 == 0 or zeros > 0:
            return steps
        else:
            return steps + 2