class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expec = n * (n + 1) // 2
        act = sum(nums)
        return expec - act