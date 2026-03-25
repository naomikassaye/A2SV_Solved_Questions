from typing import List
class Solution:
    def spiralMatrixIII(self,rows:int,cols:int,rStart:int,cStart:int)->List[List[int]]:
        result=[]
        total=rows*cols
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        r,c=rStart,cStart
        step=1
        d=0
        result.append([r,c])
        while len(result)<total:
            for _ in range(2):
                for _ in range(step):
                    r+=dirs[d][0]
                    c+=dirs[d][1]
                    if 0<=r<rows and 0<=c<cols:
                        result.append([r,c])
                        if len(result)==total:
                            return result
                d=(d+1)%4
            step+=1
        return result