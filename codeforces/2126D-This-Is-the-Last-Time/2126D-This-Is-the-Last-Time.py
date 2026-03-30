import sys
from bisect import bisect_right

class MaxST:
    def __init__(self,a):
        self.n=len(a)
        self.sz=1
        while self.sz<self.n:self.sz*=2
        self.t=[(-1,-1)]*(2*self.sz)
        for i in range(self.n):self.t[self.sz+i]=(a[i],i)
        for i in range(self.sz-1,0,-1):
            self.t[i]=max(self.t[2*i],self.t[2*i+1])
    def update(self,i,v):
        idx=self.sz+i
        self.t[idx]=(v,i)
        while idx>1:
            idx//=2
            self.t[idx]=max(self.t[2*idx],self.t[2*idx+1])
    def query(self,l,r):
        res=(-1,-1)
        l+=self.sz;r+=self.sz
        while l<=r:
            if l%2==1:res=max(res,self.t[l]);l+=1
            if r%2==0:res=max(res,self.t[r]);r-=1
            l//=2;r//=2
        return res

def solve():
    raw=sys.stdin.read().split()
    if not raw:return
    p=0
    t=int(raw[p]);p+=1
    for _ in range(t):
        n=int(raw[p]);p+=1
        k=int(raw[p]);p+=1
        cs=[]
        for _ in range(n):
            l,r,rl=int(raw[p]),int(raw[p+1]),int(raw[p+2]);p+=3
            cs.append((l,r,rl))
        cs.sort()
        ls=[c[0] for c in cs]
        rs=[c[1] for c in cs]
        st=MaxST(rs)
        q=[k]
        mx=k
        seen={k}
        while q:
            curr=q.pop()
            idx=bisect_right(ls,curr)-1
            if idx<0:continue
            while True:
                val,tidx=st.query(0,idx)
                if val>=curr:
                    nxt=cs[tidx][2]
                    if nxt>mx:mx=nxt
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)
                    st.update(tidx,-1)
                else:break
        print(mx)

if __name__=="__main__":
    solve()