class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
  
        n = len(s)
        res = [""] * n
        
        for i, char in enumerate(s):
            
            targetpos = indices[i]
            res[targetpos] = char
            
        return "".join(res)