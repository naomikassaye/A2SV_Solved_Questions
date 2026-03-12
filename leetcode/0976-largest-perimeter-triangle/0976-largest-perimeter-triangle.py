class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) == 3:
            maxx = max(nums)
            summ= sum(nums)
            if summ - maxx > maxx:
                return summ
            else: return 0
   
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0