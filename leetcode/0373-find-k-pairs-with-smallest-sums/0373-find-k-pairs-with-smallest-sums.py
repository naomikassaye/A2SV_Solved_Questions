import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans=[]
        pq=[]
        if not nums1 or not nums2:return ans
        for i in range(min(len(nums1),k)):
            heapq.heappush(pq,(nums1[i]+nums2[0],i,0))
        while k>0 and pq:
            s,i,j=heapq.heappop(pq)
            ans.append([nums1[i],nums2[j]])
            if j+1<len(nums2):
                heapq.heappush(pq,(nums1[i]+nums2[j+1],i,j+1))
            k-=1
        return ans