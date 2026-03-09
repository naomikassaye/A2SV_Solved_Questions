class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        countmap = {}
        for n in nums:
            countmap[n] = 1 + countmap.get(n, 0)

        buck = [[] for _ in range(len(nums) + 1)]

        for num, count in countmap.items():
            buck[count].append(num)

        res = []
        for i in range(len(buck) - 1, 0, -1):
            for n in buck[i]:
                res.append(n)
                if len(res) == k:
                    return res