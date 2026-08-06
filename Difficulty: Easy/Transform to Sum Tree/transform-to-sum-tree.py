class Solution:
    def toSumTree(self, root):
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            old = node.data
            node.data = left + right

            return old + node.data

        dfs(root)