import sys
def solve():
    input=sys.stdin.read().split()
    if not input:return
    p=0
    t=int(input[p]);p+=1
    for _ in range(t):
        n=int(input[p]);p+=1
        r=[int(x) for x in input[p:p+n]];p+=n
        m=int(input[p]);p+=1
        b=[int(x) for x in input[p:p+m]];p+=m
        mr,mb,cr,cb=0,0,0,0
        for x in r:
            cr+=x
            if cr>mr:mr=cr
        for x in b:
            cb+=x
            if cb>mb:mb=cb
        print(mr+mb)
if __name__=="__main__":
    solve()
