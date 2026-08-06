class Solution:
    def check(self, root):
        self.level = -1

        def dfs(node, depth):
            if not node:
                return True

            if not node.left and not node.right:
                if self.level == -1:
                    self.level = depth
                return self.level == depth

            return dfs(node.left, depth + 1) and dfs(node.right, depth + 1)

        return dfs(root, 0)