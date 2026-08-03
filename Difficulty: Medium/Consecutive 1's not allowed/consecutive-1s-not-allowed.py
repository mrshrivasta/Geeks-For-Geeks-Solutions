class Solution:
    def countStrings(self, n):
        if n == 1:
            return 2

        end0 = 1
        end1 = 1

        for _ in range(2, n + 1):
            new0 = end0 + end1
            new1 = end0
            end0, end1 = new0, new1

        return end0 + end1