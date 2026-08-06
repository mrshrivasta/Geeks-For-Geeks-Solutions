from collections import deque

class Solution:
    def maxNodeLevel(self, root):
        if not root:
            return 0

        q = deque([root])
        level = 0
        ans = 0
        mx = 0

        while q:
            cnt = len(q)

            if cnt > mx:
                mx = cnt
                ans = level

            for _ in range(cnt):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return ans