from math import gcd

class Solution:
    def maxGCD(self, root):
        self.max_g = 0
        self.ans = 0

        def dfs(node):
            if not node:
                return

            if node.left and node.right:
                g = gcd(node.left.data, node.right.data)
                if g > self.max_g or (g == self.max_g and node.data > self.ans):
                    self.max_g = g
                    self.ans = node.data

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans