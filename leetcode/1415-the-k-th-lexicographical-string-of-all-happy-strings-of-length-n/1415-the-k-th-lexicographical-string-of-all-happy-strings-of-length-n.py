class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res=[]
        def backtrack(curr):
            if len(curr)==n:
                res.append(curr)
                return
            for char in "abc":
                if not curr or curr[-1]!=char:
                    backtrack(curr+char)
                    if len(res)==k:
                        return
        backtrack("")
        return res[k-1] if len(res)>=k else ""