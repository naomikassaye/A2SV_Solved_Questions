import sys
def solve():
    data=sys.stdin.read().split()
    if not data:return
    p=0
    t=int(data[p]);p+=1
    res=[]
    for _ in range(t):
        n=int(data[p]);p+=1
        x=int(data[p]);p+=1
        k=int(data[p]);p+=1
        s=data[p];p+=1
        fz=-1
        c=x
        for i in range(n):
            if i>=k:break
            if s[i]=='L':c-=1
            else:c+=1
            if c==0:
                fz=i+1
                break
        if fz==-1:
            res.append(0)
            continue
        ans=1
        rem=k-fz
        ct=-1
        c=0
        for i in range(n):
            if i>=rem:break
            if s[i]=='L':c-=1
            else:c+=1
            if c==0:
                ct=i+1
                break
        if ct!=-1:ans+=rem//ct
        res.append(ans)
    sys.stdout.write('\n'.join(map(str,res))+'\n')
if __name__=="__main__":
    solve()