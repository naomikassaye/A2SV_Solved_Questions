class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                xi, yi, ri = bombs[i]
                xj, yj, rj = bombs[j]
                if (xi - xj)**2 + (yi - yj)**2 <= ri**2:
                    adj[i].append(j)
        ans = 0
        for i in range(n):
            q = [i]
            visited = {i}
            while q:
                u = q.pop()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
            ans = max(ans, len(visited))
        return ans