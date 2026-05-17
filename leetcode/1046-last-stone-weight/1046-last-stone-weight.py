import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h=[-x for x in stones]
        heapq.heapify(h)
        while len(h)>1:
            s1=heapq.heappop(h)
            s2=heapq.heappop(h)
            if s1!=s2:
                heapq.heappush(h,s1-s2)
        return -h[0] if h else 0