class Solution:
    def largestBst(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))

            l_bst, l_size, l_min, l_max = dfs(node.left)
            r_bst, r_size, r_min, r_max = dfs(node.right)

            if l_bst and r_bst and l_max < node.data < r_min:
                size = l_size + r_size + 1
                self.ans = max(self.ans, size)
                return (
                    True,
                    size,
                    min(l_min, node.data),
                    max(r_max, node.data)
                )

            return (False, 0, 0, 0)

        dfs(root)
        return self.ans