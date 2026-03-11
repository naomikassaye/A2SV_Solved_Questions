class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        count = {}
        for x in changed:
            count[x] = count.get(x, 0) + 1

        res = []
        for x in changed:
            if count[x] == 0:
                continue
            
            count[x] -= 1
            
            double = x * 2

            if count.get(double, 0) > 0:
                count[double] -= 1
                res.append(x)
            else:
                return []

        return res