import sys

def solve():
    data=sys.stdin.read().split()
    if not data:return
    p=0
    t=int(data[p]);p+=1
    for _ in range(t):
        n=int(data[p]);p+=1
        a=[int(x) for x in data[p:p+n]];p+=n
        b=[int(x) for x in data[p:p+n]];p+=n
        ops=[]
        changed=True
        while changed:
            changed=False
            for i in range(n-1):
                if a[i]>a[i+1]:
                    a[i],a[i+1]=a[i+1],a[i]
                    ops.append((1,i+1))
                    changed=True
            for i in range(n-1):
                if b[i]>b[i+1]:
                    b[i],b[i+1]=b[i+1],b[i]
                    ops.append((2,i+1))
                    changed=True
            for i in range(n):
                if a[i]>b[i]:
                    a[i],b[i]=b[i],a[i]
                    ops.append((3,i+1))
                    changed=True
        print(len(ops))
        for opT,idx in ops:
            print(f"{opT} {idx}")

if __name__=="__main__":
    solve()