class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
        ans=[[] for _ in range(n)]
        def dfs(anc,curr,visited):
            visited[curr]=True
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    ans[neighbor].append(anc)
                    dfs(anc,neighbor,visited)
        for i in range(n):
            dfs(i,i,[False]*n)
        return ans