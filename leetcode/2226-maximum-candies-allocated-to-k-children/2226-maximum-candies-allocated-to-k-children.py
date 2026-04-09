class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l,r=1,sum(candies)//k
        ans=0
        while l<=r:
            m=(l+r)//2
            if sum(c//m for c in candies)>=k:
                ans=m
                l=m+1
            else:
                r=m-1
        return ans