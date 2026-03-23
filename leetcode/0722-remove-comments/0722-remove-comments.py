class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        res = []
        buf = []
        inb = False
        
        for line in source:
            i=0
            while i<len(line):
                char=line[i]
                if inb:
                    if char=="*" and i+1<len(line) and line[i+1]=="/":
                        inb=False
                        i+=1
                else:
                    if char=="/" and i+1<len(line) and line[i+1]=="*":
                        inb=True
                        i+=1
                    elif char=="/" and i+1<len(line) and line[i+1]=="/":
                        break
                    else:
                        buf.append(char)
                i+=1
            
            if not inb and buf:
                res.append("".join(buf))
                buf=[]
                
        return res