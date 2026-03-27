class Solution:
    def maxSubArray(self,nums:list[int])->int:
        res=nums[0]
        cur=nums[0]
        for i in range(1,len(nums)):
            x=nums[i]
            if cur<0:
                cur=x
            else:
                cur+=x
            if cur>res:
                res=cur
        return res