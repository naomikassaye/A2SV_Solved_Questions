class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        target=len(graph)-1
        def backtrack(u,path):
            if u==target:
                ans.append(list(path))
                return
            for v in graph[u]:
                path.append(v)
                backtrack(v,path)
                path.pop()
        backtrack(0,[0])
        return ans