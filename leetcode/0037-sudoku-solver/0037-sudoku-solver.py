class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxs=[set() for _ in range(9)]
        todo=[]
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    todo.append((r,c))
                else:
                    v=board[r][c]
                    rows[r].add(v)
                    cols[c].add(v)
                    boxs[(r//3)*3+c//3].add(v)
        def backtrack(i):
            if i==len(todo):return True
            r,c=todo[i]
            b=(r//3)*3+c//3
            for v in "123456789":
                if v not in rows[r] and v not in cols[c] and v not in boxs[b]:
                    board[r][c]=v
                    rows[r].add(v)
                    cols[c].add(v)
                    boxs[b].add(v)
                    if backtrack(i+1):return True
                    rows[r].remove(v)
                    cols[c].remove(v)
                    boxs[b].remove(v)
                    board[r][c]="."
            return False
        backtrack(0)