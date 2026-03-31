class Solution:
    def checkSubarraySum(self,nums:list[int],k:int)->bool:
        c=0
        d={0:-1}
        for i,x in enumerate(nums):
            c=(c+x)%k
            if c in d:
                if i-d[c]>=2:return True
            else:
                d[c]=i
        return False