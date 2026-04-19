class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        l,r=0,m
        while l<=r:
            i=(l+r)//2
            j=(m+n+1)//2-i
            maxL1=nums1[i-1] if i>0 else float('-inf')
            minR1=nums1[i] if i<m else float('inf')
            maxL2=nums2[j-1] if j>0 else float('-inf')
            minR2=nums2[j] if j<n else float('inf')
            if maxL1<=minR2 and maxL2<=minR1:
                if (m+n)%2:
                    return max(maxL1,maxL2)
                return (max(maxL1,maxL2)+min(minR1,minR2))/2.0
            elif maxL1>minR2:
                r=i-1
            else:
                l=i+1