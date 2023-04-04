def generate_combinations(digits):
    if len(digits) == 1:
        return [digits]
    else:
        res = []
        for i in range(len(digits)):
            remaining_digits = digits[:i] + digits[i + 1:]
            sub_combinations = generate_combinations(remaining_digits)
            for comb in sub_combinations:
                res.append([digits[i]] + comb)
        return res


digits = [1, 2, 3, 4, 5]
all_combs = generate_combinations(digits)
answer = sum(map(lambda lst: int(''.join(map(str, lst))), all_combs))
print(answer)
