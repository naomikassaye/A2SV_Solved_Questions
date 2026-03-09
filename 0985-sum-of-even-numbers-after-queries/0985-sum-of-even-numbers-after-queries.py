class Solution:
    def sumEvenAfterQueries(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        evensum = 0
        for x in nums:
            if x % 2 == 0:
                evensum += x
        
        res = []
        
        for val, index in queries:
            if nums[index] % 2 == 0:
                evensum -= nums[index]
            
            nums[index] += val
            
            if nums[index] % 2 == 0:
                evensum += nums[index]
        
            res.append(evensum)
            
        return res