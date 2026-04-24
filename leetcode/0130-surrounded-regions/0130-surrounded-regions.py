class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:return
        m,n=len(board),len(board[0])
        q=[]
        for r in range(m):
            if board[r][0]=="O":q.append((r,0))
            if board[r][n-1]=="O":q.append((r,n-1))
        for c in range(n):
            if board[0][c]=="O":q.append((0,c))
            if board[m-1][c]=="O":q.append((m-1,c))
        while q:
            r,c=q.pop()
            if board[r][c]=="O":
                board[r][c]="#"
                if r>0:q.append((r-1,c))
                if r<m-1:q.append((r+1,c))
                if c>0:q.append((r,c-1))
                if c<n-1:q.append((r,c+1))
        for r in range(m):
            for c in range(n):
                if board[r][c]=="O":board[r][c]="X"
                elif board[r][c]=="#":board[r][c]="O"