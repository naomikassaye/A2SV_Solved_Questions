class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}
        def solve(l, r):
            if l == r:
                 return nums[l]
            if (l, r) in memo:
                 return memo[(l, r)]
            memo[(l, r)] = max(nums[l] - solve(l + 1, r), nums[r] - solve(l, r - 1))
            return memo[(l, r)]
        return solve(0, len(nums) - 1) >= 0