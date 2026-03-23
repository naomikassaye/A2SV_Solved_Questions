import sys
def solve():
    input=sys.stdin.read().split()
    if not input:
        return
    t=int(input[0])
    pointer=1

    for _ in range(t):
        n=int(input[pointer])
        s=input[pointer+1]
        pointer+=2

        if "aa" in s:
            print(2)
            continue
        if "aba" in s or "aca" in s:
            print(3)
            continue
        if "abca" in s or "acba" in s:
            print(4)
            continue

        if "abbacca" in s or "accabba" in s:
            print(7)
            continue
        print(-1)
if __name__=="__main__":
    solve()