class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans=float('inf')
        n=len(cookies)
        dist=[0]*k
        cookies.sort(reverse=True)
        def dfs(i):
            nonlocal ans
            if i==n:
                ans=min(ans,max(dist))
                return
            if max(dist)>=ans:
                return
            for j in range(k):
                dist[j]+=cookies[i]
                dfs(i+1)
                dist[j]-=cookies[i]
                if dist[j]==0:
                    break
        dfs(0)
        return ans