from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for size in range(len(arr), 1, -1):
            maxidx = arr.index(size)
            if maxidx != size - 1:
                if maxidx != 0:
                    res.append(maxidx + 1)
                    arr[:maxidx+1] = reversed(arr[:maxidx+1])
                res.append(size)
                arr[:size] = reversed(arr[:size])
        return res