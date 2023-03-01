def get_fibonacci_number(n):
    dp = [-1] * (n + 1)
    dp[0] = dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    input_n = int(input())
    res_number = get_fibonacci_number(input_n)
    print(res_number, len(str(res_number)), sep='\n')
