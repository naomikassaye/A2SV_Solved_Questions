class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()

        duplicate = -1
        missing = -1

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                duplicate = nums[i]
                break
    
        n = len(nums)
        for x in range(1, n + 1):
            if x not in nums:
                missing = x
                break

        return [duplicate, missing]
