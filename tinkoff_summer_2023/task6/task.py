import sys
input = sys.stdin.readline

n, s = map(int, input().split())
ql = [0] * (n+1)
qr = [0] * (n+1)


def read():
    global n, s, ql, qr
    for i in range(1, n+1):
        ql[i], qr[i] = map(int, input().split())


def ok(c):
    cntBigR = cntBigL = 0
    for i in range(1, n+1):
        if qr[i] >= c:
            cntBigR += 1
        if ql[i] > c:
            cntBigL += 1
    if cntBigR < (n + 1) // 2:
        return False
    assert cntBigL < (n + 1) // 2
    sum = 0
    for i in range(n, (n + 1) // 2 - 1, -1):
        if ql[i] <= c:
            sum += (c - ql[i])
    return sum <= s


def solver():
    global s, ql, qr
    for i in range(1, n+1):
        ql[i], qr[i] = map(int, input().split())
        s -= ql[i]
    assert s >= 0
    ql.sort()
    qr.sort()
    l = ql[(n + 1) // 2]
    r = 10**9 + 10
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if ok(mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(ans)


def solve():
    global n
    n, s = map(int, input().replace('\n', '').split())
    solver()


solve()
