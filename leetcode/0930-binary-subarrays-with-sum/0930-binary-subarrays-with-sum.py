class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res=0
        lsum=0
        d={0:1}
        for x in nums:
            lsum+=x
            tar=lsum-goal
            if tar in d:
                res+=d[tar]
            if lsum in d:
                d[lsum]+=1
            else:
                d[lsum]=1
        return res
            