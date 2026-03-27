import sys
def solve():
    data=sys.stdin.read().split()
    if not data:return
    p=0
    h=int(data[p]);p+=1
    w=int(data[p]);p+=1
    g=[data[p+i] for i in range(h)];p+=h
    ph=[[0]*(w+1) for _ in range(h+1)]
    pv=[[0]*(w+1) for _ in range(h+1)]
    for i in range(h):
        for j in range(w):
            vH=1 if j+1<w and g[i][j]=='.' and g[i][j+1]=='.' else 0
            vV=1 if i+1<h and g[i][j]=='.' and g[i+1][j]=='.' else 0
            ph[i+1][j+1]=ph[i][j+1]+ph[i+1][j]-ph[i][j]+vH
            pv[i+1][j+1]=pv[i][j+1]+pv[i+1][j]-pv[i][j]+vV
    q=int(data[p]);p+=1
    res=[]
    for _ in range(q):
        r1=int(data[p]);p+=1
        c1=int(data[p]);p+=1
        r2=int(data[p]);p+=1
        c2=int(data[p]);p+=1
        ans=0
        if c2>c1:
            ans+=ph[r2][c2-1]-ph[r1-1][c2-1]-ph[r2][c1-1]+ph[r1-1][c1-1]
        if r2>r1:
            ans+=pv[r2-1][c2]-pv[r1-1][c2]-pv[r2-1][c1-1]+pv[r1-1][c1-1]
        res.append(str(ans))
    sys.stdout.write('\n'.join(res)+'\n')
if __name__=="__main__":
    solve()