class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        cand, cnt, n = -1, 0, len(nums)
        for x in nums:
            if cnt == 0:
                cand, cnt = x, 1
            elif x == cand:
                cnt += 1
            else:
                cnt -= 1
        tot = nums.count(cand)
        cur = 0
        for i in range(n - 1):
            if nums[i] == cand:
                cur += 1
            if cur * 2 > (i + 1) and (tot - cur) * 2 > (n - i - 1):
                return i
        return -1