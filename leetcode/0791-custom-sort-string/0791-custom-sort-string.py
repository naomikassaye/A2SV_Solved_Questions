from collections import Counter
class Solution:
    def customSortString(self,order:str,s:str)->str:
        cnt,res=Counter(s),[]
        for c in order:
            if c in cnt:
                res.append(c*cnt.pop(c))
        for c,n in cnt.items():
            res.append(c*n)
        return "".join(res)