class Solution:
    def dfs(self, adj):
        visited = [False] * len(adj)
        res = []

        def dfs_visit(node):
            visited[node] = True
            res.append(node)
            for nei in adj[node]:
                if not visited[nei]:
                    dfs_visit(nei)

        dfs_visit(0)
        return res