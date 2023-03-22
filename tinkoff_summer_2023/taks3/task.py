def get_answer(n: int, s: str):
    res = -1

    index_dict = {'a': -1, 'b': -1, 'c': -1, 'd': -1}
    for i in range(n):
        index_dict[s[i]] = i
        left = min(index_dict.values())
        length = i - left + 1
        if left != -1:
            if res == - 1 or res > length:
                res = length
    return res


if __name__ == '__main__':
    n = int(input())
    s = input()
    print(get_answer(n, s))
