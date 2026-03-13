class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter=[]
        for a in set(nums1) & set(nums2):
            inter.append(a)

        return inter
        