class Solution:
    def maxSumRangeQuery(self,nums:list[int],reqs:list[list[int]])->int:
        n=len(nums)
        f=[0]*(n+1)
        for s,e in reqs:
            f[s]+=1
            f[e+1]-=1
        for i in range(1,n):
            f[i]+=f[i-1]
        f.pop()
        f.sort()
        nums.sort()
        res=0
        mod=10**9+7
        for i in range(n):
            res=(res+f[i]*nums[i])%mod
        return res