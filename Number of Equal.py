import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2:2+n]]
    b = [int(x) for x in data[2+n:]]
    i = 0
    j = 0
    ans = 0
    while i < n and j < m:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            val = a[i]
            cnt1 = 0
            while i < n and a[i] == val:
                cnt1 += 1
                i += 1
            cnt2 = 0
            while j < m and b[j] == val:
                cnt2 += 1
                j += 1
            ans += cnt1 * cnt2
    sys.stdout.write(str(ans) + '\n')

if __name__ == '__main__':
    solve()
