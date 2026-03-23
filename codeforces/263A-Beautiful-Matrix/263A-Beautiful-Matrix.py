import sys
def solve():
    for r in range(5):
        ln=sys.stdin.readline().strip()
        if not ln:
            continue
        row=list(map(int,ln.split()))
        if 1 in row:
            c=row.index(1)
            ans=abs(r-2)+abs(c-2)
            print(ans)
            return
if __name__=="__main__":
    solve()