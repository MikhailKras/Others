def print_mat(mat):
    for row in matrix:
        print(*row)
    print('-' * 20)


n = 5
matrix = [[0 for _ in range(n)] for _ in range(n)]

j = 1
if n % 2:
    matrix[n // 2][n // 2] = n ** 2
for delta in range(n // 2):
    for i in range(delta, n - 1 - delta):
        matrix[0+delta][i] = j
        j += 1
    print_mat(matrix)
    for i in range(delta, n - 1 - delta):
        matrix[i][n - 1 - delta] = j
        j += 1
    print_mat(matrix)
    for i in range(n - 1 - delta, delta, -1):
        matrix[n - 1 - delta][i] = j
        j += 1
    print_mat(matrix)
    for i in range(n - 1 - delta, delta, -1):
        matrix[i][0+delta] = j
        j += 1
    print_mat(matrix)



