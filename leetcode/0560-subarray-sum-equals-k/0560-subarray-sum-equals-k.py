class Solution:
    def subarraySum(self,nums:list[int],k:int)->int:
        res=0
        curr=0
        d={0:1}
        for x in nums:
            curr+=x
            if curr-k in d:
                res+=d[curr-k]
            d[curr]=d.get(curr,0)+1
        return res