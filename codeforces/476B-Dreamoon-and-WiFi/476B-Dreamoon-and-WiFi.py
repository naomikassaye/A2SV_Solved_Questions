import sys
import math

def solve():
    d = sys.stdin.read().split()
    if not d: return
    s1, s2 = d[0], d[1]
    t = s1.count('+') - s1.count('-')
    c = s2.count('+') - s2.count('-')
    q = s2.count('?')
    diff = t - c
    if (q + diff) % 2 != 0 or abs(diff) > q:
        print(f"{0.0:.12f}")
        return
    x = (q + diff) // 2
    ans = math.comb(q, x) / (2**q)
    print(f"{ans:.12f}")

if __name__ == "__main__":
    solve()