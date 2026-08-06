from collections import deque

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0

        q = deque([root])
        ans = float('-inf')

        while q:
            s = 0

            for _ in range(len(q)):
                node = q.popleft()
                s += node.data

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans = max(ans, s)

        return ans