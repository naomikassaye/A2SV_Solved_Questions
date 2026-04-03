import sys
def solve():
    data = sys.stdin.read().split()
    if not data: return
    n, k, q = int(data[0]), int(data[1]), int(data[2])
    diff = [0] * 200005
    idx = 3
    for _ in range(n):
        l, r = int(data[idx]), int(data[idx+1])
        diff[l] += 1
        diff[r+1] -= 1
        idx += 2
    curr = 0
    pref = [0] * 200005
    for i in range(1, 200001):
        curr += diff[i]
        pref[i] = pref[i-1] + (1 if curr >= k else 0)
    out = []
    for _ in range(q):
        a, b = int(data[idx]), int(data[idx+1])
        out.append(str(pref[b] - pref[a-1]))
        idx += 2
    sys.stdout.write('\n'.join(out) + '\n')
if __name__ == '__main__':
    solve()