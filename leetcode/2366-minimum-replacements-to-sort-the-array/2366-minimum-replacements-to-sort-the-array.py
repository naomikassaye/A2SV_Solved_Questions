class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        lastVal=nums[n-1]
        for i in range(n-2,-1,-1):
            if nums[i]>lastVal:
                k=(nums[i]+lastVal-1)//lastVal
                ans+=k-1
                lastVal=nums[i]//k
            else:
                lastVal=nums[i]
        return ans