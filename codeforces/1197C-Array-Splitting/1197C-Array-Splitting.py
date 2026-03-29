import sys
def solve():
    data=sys.stdin.read().split()
    if not data:return
    n=int(data[0])
    k=int(data[1])
    a=[int(x) for x in data[2:]]
    diffs=[]
    for i in range(n-1):
        diffs.append(a[i+1]-a[i])
    diffs.sort(reverse=True)
    ans=a[n-1]-a[0]
    for i in range(k-1):
        ans-=diffs[i]
    print(ans)
if __name__=="__main__":
    solve()