def get_answer(n, m, k):
    if not k * n % m:
        return k * n // m
    return k * n // m + 1


if __name__ == '__main__':
    n, m, k = tuple(map(int, input().split()))
    print(get_answer(n, m, k))
