import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        a=[]
        for i in range(n):
            a.append([tasks[i][0],tasks[i][1],i])
        a.sort()
        res=[]
        h=[]
        i=0
        time=a[0][0]
        while len(res)<n:
            while i<n and a[i][0]<=time:
                heapq.heappush(h,(a[i][1],a[i][2]))
                i+=1
            if h:
                p_time,idx=heapq.heappop(h)
                time+=p_time
                res.append(idx)
            elif i<n:
                time=a[i][0]
        return res