class Solution:
    def splitString(self,s:str)->bool:
        def d(i,p):
            if i==len(s):
                return True
            for j in range(i+1,len(s)+1):
                v=int(s[i:j])
                if p-v==1 and d(j,v):
                    return True
            return False
        for i in range(1,len(s)):
            v=int(s[:i])
            if d(i,v):
                return True
        return False