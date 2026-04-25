import sys

def solve():
    d = sys.stdin.read().split()
    if not d: return
    t, p = int(d[0]), 1
    for _ in range(t):
        n = int(d[p])
        a = list(map(int, d[p+1:p+1+n]))
        p, ans, last = p+n+1, 0, a[n-1]
        for i in range(n-2):
            r, l = i+2, n
            ai = a[i]
            for j in range(i+1, n-1):
                s = ai + a[j]
                while r < n and a[r] < s: r += 1
                while l > 0 and a[l-1] > last - s: l -= 1
                low = j + 1
                if l > low: low = l
                if r > low: ans += (r - low)
        sys.stdout.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()