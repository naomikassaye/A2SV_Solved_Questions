class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:return 0
        lo,hi=min(nums),max(nums)
        if lo==hi:return 0
        bsize=max(1,(hi-lo)//(n-1))
        bcnt=(hi-lo)//bsize+1
        bmin=[float('inf')]*bcnt
        bmax=[float('-inf')]*bcnt
        for x in nums:
            i=(x-lo)//bsize
            bmin[i]=min(bmin[i],x)
            bmax[i]=max(bmax[i],x)
        ans=0
        prev=lo
        for i in range(bcnt):
            if bmin[i]==float('inf'):continue
            ans=max(ans,bmin[i]-prev)
            prev=bmax[i]
        return ans