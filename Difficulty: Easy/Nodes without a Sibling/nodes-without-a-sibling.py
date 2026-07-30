class Solution:
    def noSibling(self, root):
        ans = []

        def dfs(node):
            if not node:
                return

            if node.left and not node.right:
                ans.append(node.left.data)
            if node.right and not node.left:
                ans.append(node.right.data)

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if not ans:
            return [-1]

        ans.sort()
        return ans