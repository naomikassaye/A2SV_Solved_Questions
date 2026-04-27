import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    ptr = 1
    for _ in range(t):
        n = int(data[ptr])
        ptr += 1
        p = [int(x) for x in data[ptr:ptr+n]]
        ptr += n
        res = [p[0]]
        for i in range(1, n - 1):
            if not (p[i-1] < p[i] < p[i+1] or p[i-1] > p[i] > p[i+1]):
                res.append(p[i])
        res.append(p[n-1])
        print(len(res))
        print(*(res))

if __name__ == '__main__':
    solve()