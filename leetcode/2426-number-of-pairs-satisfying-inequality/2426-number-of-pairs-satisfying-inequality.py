class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        a = [x - y for x, y in zip(nums1, nums2)]
        self.ans = 0
        def solve(arr):
            if len(arr) <= 1: return arr
            mid = len(arr) // 2
            left = solve(arr[:mid])
            right = solve(arr[mid:])
            i = 0
            for x in right:
                while i < len(left) and left[i] <= x + diff:
                    i += 1
                self.ans += i
            merged = []
            p1 = p2 = 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] <= right[p2]:
                    merged.append(left[p1])
                    p1 += 1
                else:
                    merged.append(right[p2])
                    p2 += 1
            merged.extend(left[p1:])
            merged.extend(right[p2:])
            return merged
        solve(a)
        return self.ans