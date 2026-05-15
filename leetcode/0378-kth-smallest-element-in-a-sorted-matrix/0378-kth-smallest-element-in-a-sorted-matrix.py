class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        l,r=matrix[0][0],matrix[n-1][n-1]
        def count_less_equal(m):
            cnt=0
            row,col=n-1,0
            while row>=0 and col<n:
                if matrix[row][col]<=m:
                    cnt+=row+1
                    col+=1
                else:
                    row-=1
            return cnt
        while l<r:
            mid=(l+r)//2
            if count_less_equal(mid)<k:
                l=mid+1
            else:
                r=mid
        return l