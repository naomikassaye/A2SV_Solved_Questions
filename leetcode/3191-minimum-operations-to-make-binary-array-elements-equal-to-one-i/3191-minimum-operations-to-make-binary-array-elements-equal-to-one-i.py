class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == 0:
                ans += 1
                nums[i] = 1
                nums[i+1] = 1 - nums[i+1]
                nums[i+2] = 1 - nums[i+2]
        
        return ans if nums[-1] == 1 and nums[-2] == 1 else -1