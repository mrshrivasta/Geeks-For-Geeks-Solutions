class Solution:
    def findTreeHeight(self, root):
        def isLeaf(node):
            return (node.left and node.left.right == node and
                    node.right and node.right.left == node)

        def dfs(node):
            if not node:
                return -1
            if isLeaf(node):
                return 0
            return 1 + max(dfs(node.left), dfs(node.right))

        return dfs(root)rrr