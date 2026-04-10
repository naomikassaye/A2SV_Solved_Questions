class Solution:
    def hIndex(self,citations:List[int])->int:
        n=len(citations)
        if n==0:
            return 0
        l,r=-1,n
        while r-l>1:
            m=l+(r-l)//2
            if citations[m]==n-m:
                return n-m
            if citations[m]<n-m:
                l=m
            else:
                r=m
        return n-r