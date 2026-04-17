class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res=[""]
        for digit in digits:
            tmp=[]
            for char in d[digit]:
                for s in res:
                    tmp.append(s+char)
            res=tmp
        return res