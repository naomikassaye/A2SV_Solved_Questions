class NumMatrix:
    def __init__(self,mat:list[list[int]]):
        if not mat or not mat[0]:return
        R,C=len(mat),len(mat[0])
        self.p=[[0]*(C+1) for _ in range(R+1)]
        for r in range(R):
            for c in range(C):
                self.p[r+1][c+1]=mat[r][c]+self.p[r][c+1]+self.p[r+1][c]-self.p[r][c]

    def sumRegion(self,r1:int,c1:int,r2:int,c2:int)->int:
        return self.p[r2+1][c2+1]-self.p[r1][c2+1]-self.p[r2+1][c1]+self.p[r1][c1]