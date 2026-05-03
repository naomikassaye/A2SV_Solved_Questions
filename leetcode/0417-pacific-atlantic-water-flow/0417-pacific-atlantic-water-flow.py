class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        m,n=len(heights),len(heights[0])
        pac,atl=set(),set()
        def dfs(r,c,visit,prevH):
            if r<0 or r>=m or c<0 or c>=n or (r,c) in visit or heights[r][c]<prevH:
                return
            visit.add((r,c))
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r+dr,c+dc,visit,heights[r][c])
        for c in range(n):
            dfs(0,c,pac,heights[0][c])
            dfs(m-1,c,atl,heights[m-1][c])
        for r in range(m):
            dfs(r,0,pac,heights[r][0])
            dfs(r,n-1,atl,heights[r][n-1])
        res=[]
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res