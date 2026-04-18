class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        def f(c,u):
            if len(c)==n:
                res.append(c[:])
                return
            for i in range(n):
                if not u[i]:
                    u[i]=True
                    c.append(nums[i])
                    f(c,u)
                    c.pop()
                    u[i]=False
        f([],[False]*n)
        return res