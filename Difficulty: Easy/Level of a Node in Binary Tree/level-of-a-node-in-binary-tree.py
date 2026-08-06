from collections import deque

class Solution:
    def getLevel(self, root, target):
        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            node, level = q.popleft()

            if node.data == target:
                return level

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return 0