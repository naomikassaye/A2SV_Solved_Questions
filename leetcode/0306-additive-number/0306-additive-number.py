class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                s1,s2=num[:i],num[i:j]
                if (len(s1)>1 and s1[0]=="0") or (len(s2)>1 and s2[0]=="0"):
                    continue
                
                n1,n2=int(s1),int(s2)
                rest=num[j:]
                while rest:
                    n3=n1+n2
                    s3=str(n3)
                    if not rest.startswith(s3):
                        break
                    rest=rest[len(s3):]
                    n1,n2=n2,n3
                    if not rest:
                        return True
        return False