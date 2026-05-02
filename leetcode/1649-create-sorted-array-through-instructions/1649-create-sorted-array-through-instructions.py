class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m=max(instructions)
        bit=[0]*(m+1)
        def update(i):
            while i<=m:
                bit[i]+=1
                i+=i&(-i)
        def query(i):
            res=0
            while i>0:
                res+=bit[i]
                i-=i&(-i)
            return res
        ans,mod=0,10**9+7
        for i,x in enumerate(instructions):
            ans=(ans+min(query(x-1),i-query(x)))%mod
            update(x)
        return ans