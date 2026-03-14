class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        snums=sorted(nums)
        smap={}
        for i,n in enumerate(snums):
            if n not in smap:
                smap[n]=i
        res=[]
        for n in nums:
            res.append(smap[n])
        return res

                