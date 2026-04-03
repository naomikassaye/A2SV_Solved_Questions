class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        while l<r:
            m=(l+r)//2
            cur,d=0,1
            for w in weights:
                if cur+w>m:
                    d+=1
                    cur=w
                else:
                    cur+=w
            if d<=days:
                r=m
            else:
                l=m+1
        return l