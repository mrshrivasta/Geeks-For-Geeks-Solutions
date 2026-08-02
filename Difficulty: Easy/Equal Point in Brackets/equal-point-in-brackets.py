class Solution:
    def findIndex(self, s):
        right_close = s.count(')')
        left_open = 0

        for i in range(len(s)):
            if left_open == right_close:
                return i
            if s[i] == '(':
                left_open += 1
            else:
                right_close -= 1

        return len(s)