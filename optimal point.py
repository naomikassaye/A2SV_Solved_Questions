import sys
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    x = sorted(map(int, data[1:]))
    print(x[(n - 1) // 2])
if __name__ == "__main__":
    solve()
