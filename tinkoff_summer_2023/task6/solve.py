def get_answer(n, s, lefts, rights):
    def check(c):
        counter_r = 0
        counter_l = 0
        for i in range(n):
            if rights[i] >= c:
                counter_r += 1
            if lefts[i] > c:
                counter_l += 1
        if counter_r < (n - 1)/2:
            return False
        assert counter_l < (n - 1) / 2
        sum_s = 0
        for i in range(n - 1, (n - 1)//2 - 1, -1):
            if lefts[i] <= c:
                sum_s += (c - lefts[i])
        return sum_s <= s

    for i in range(n):
        s -= lefts[i]
    lefts.sort()
    rights.sort()
    l = lefts[(n - 1)//2]
    r = 10 ** 9
    ans = 0
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid):
            l = mid
            ans = mid
        else:
            r = mid - 1
    return ans


if __name__ == '__main__':
    n, s = map(int, input().split())
    lefts = []
    rights = []
    for _ in range(n):
        l, r = map(int, input().split())
        lefts.append(l)
        rights.append(r)
    print(get_answer(n, s, lefts, rights))
