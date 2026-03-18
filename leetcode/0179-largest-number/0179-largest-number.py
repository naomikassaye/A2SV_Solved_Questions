class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr=[str(n) for n in nums]
        size=len(arr)
        for i in range(size):
            for j in range(size-i-1):
                if arr[j]+arr[j+1]<arr[j+1]+arr[j]:
                    arr[j], arr[j+1]=arr[j+1], arr[j]
        ans="".join(arr)
        if ans[0]=="0":
            return "0"
        return ans


        