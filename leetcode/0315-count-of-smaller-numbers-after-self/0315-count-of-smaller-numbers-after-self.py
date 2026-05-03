class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        a=[(v,i) for i,v in enumerate(nums)]
        def solve(arr):
            if len(arr)<=1:return arr
            mid=len(arr)//2
            L,R=solve(arr[:mid]),solve(arr[mid:])
            i=j=0
            tmp=[]
            while i<len(L) and j<len(R):
                if L[i][0]<=R[j][0]:
                    ans[L[i][1]]+=j
                    tmp.append(L[i])
                    i+=1
                else:
                    tmp.append(R[j])
                    j+=1
            while i<len(L):
                ans[L[i][1]]+=j
                tmp.append(L[i])
                i+=1
            tmp.extend(R[j:])
            return tmp
        solve(a)
        return ans