class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dig={}
        rows=len(mat)
        cols=len(mat[0])
        for r in range(rows):
            for c in range(cols):
                key=r+c
                if key not in dig:
                    dig[key]=[]
                dig[key].append(mat[r][c])
        res=[]
        for k in range(rows+cols-1):
            if k%2==0:
                res.extend(dig[k][::-1])
            else:
                res.extend(dig[k])
        return res