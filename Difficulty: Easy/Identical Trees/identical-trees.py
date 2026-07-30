class Solution:
    def isIdentical(self, r1, r2):
        if not r1 and not r2:
            return True
        if not r1 or not r2:
            return False
        return (
            r1.data == r2.data and
            self.isIdentical(r1.left, r2.left) and
            self.isIdentical(r1.right, r2.right)
        )