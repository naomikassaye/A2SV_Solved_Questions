import sys
def solve():
    d=sys.stdin.read().split()
    if not d:return
    p=0
    t_c=int(d[p])
    p+=1
    r=[]
    for _ in range(t_c):
        s=d[p]
        t=d[p+1]
        p+=2
        cs,ct=[0]*26,[0]*26
        for c in s:cs[ord(c)-97]+=1
        for c in t:ct[ord(c)-97]+=1
        ok=True
        for i in range(26):
            if ct[i]<cs[i]:
                ok=False
                break
        if not ok:
            r.append("Impossible")
            continue
        ex=[ct[i]-cs[i] for i in range(26)]
        res=[]
        for char in s:
            idx=ord(char)-97
            for i in range(idx):
                if ex[i]>0:
                    res.append(chr(97+i)*ex[i])
                    ex[i]=0
            res.append(char)
        for i in range(26):
            if ex[i]>0:res.append(chr(97+i)*ex[i])
        r.append("".join(res))
    sys.stdout.write("\n".join(r)+"\n")
if __name__=="__main__":
    solve()