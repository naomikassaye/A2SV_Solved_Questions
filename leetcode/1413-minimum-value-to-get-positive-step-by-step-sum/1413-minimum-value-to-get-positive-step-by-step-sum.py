class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        tot=0
        res=[]
        for i in range(len(nums)):
            tot+=nums[i]
            res.append(tot)
        x=min(res)
        return max(1, 1-x)
        