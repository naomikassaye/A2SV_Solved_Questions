class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        for i in range(n):
            if color[i]==-1:
                color[i]=0
                st=[i]
                while st:
                    u=st.pop()
                    for v in graph[u]:
                        if color[v]==-1:
                            color[v]=1-color[u]
                            st.append(v)
                        elif color[v]==color[u]:
                            return False
        return True