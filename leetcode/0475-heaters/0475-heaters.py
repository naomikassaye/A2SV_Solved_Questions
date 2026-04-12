import bisect
class Solution:
    def findRadius(self,houses:List[int],heaters:List[int])->int:
        heaters.sort()
        r=0
        for h in houses:
            i=bisect.bisect_left(heaters,h)
            d1=heaters[i]-h if i<len(heaters) else float('inf')
            d2=h-heaters[i-1] if i>0 else float('inf')
            r=max(r,min(d1,d2))
        return r