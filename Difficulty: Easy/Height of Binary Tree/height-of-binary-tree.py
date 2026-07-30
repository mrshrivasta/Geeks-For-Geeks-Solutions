class Solution:
    def height(self, root):
        if not root:
            return -1
        return 1 + max(self.height(root.left), self.height(root.right))