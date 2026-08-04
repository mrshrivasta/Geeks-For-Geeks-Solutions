class Solution:
    def printPalindromes(self, m, n):
        result = []
        for num in range(m, n + 1):
            s = str(num)
            if s == s[::-1]:
                result.append(num)
        return result