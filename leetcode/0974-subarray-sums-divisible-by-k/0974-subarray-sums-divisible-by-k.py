class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count={0:1}
        prefixsum=0
        res=0
        for n in nums:
            prefixsum+=n
            remainder=prefixsum%k
            if remainder in count:
                res+=count[remainder]
                count[remainder]+=1
            else:
                count[remainder]=1
        return res