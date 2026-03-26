class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        s = []
        nge = {}
        
        for n in nums2:
            while s and s[-1] < n:
                nge[s.pop()] = n
            s.append(n)
        
        while s:
            nge[s.pop()] = -1
        
        res = []
        for x in nums1:
            res.append(nge[x])
        
        return res
