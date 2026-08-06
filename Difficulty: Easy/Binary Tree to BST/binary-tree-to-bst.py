class Solution:
    def binaryTreeToBST(self, root):
        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.data)
            inorder(node.right)

        inorder(root)
        arr.sort()

        i = 0

        def fill(node):
            nonlocal i
            if not node:
                return
            fill(node.left)
            node.data = arr[i]
            i += 1
            fill(node.right)

        fill(root)
        return root