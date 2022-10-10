
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    res = []
    n = len(matrix[0])  # nums of col
    m = len(matrix)  # nums of rows
    counter = 0

    for delta in range(max(n, m) // 2):
        for i in range(delta, n - 1 - delta):
            if counter == n * m:
                break
            res.append(matrix[delta][i])
            counter += 1

        for i in range(delta, m - 1 - delta):
            if counter == n * m:
                break
            res.append(matrix[i][n - 1 - delta])
            counter += 1

        for i in range(n - 1 - delta, delta, -1):
            if counter == n * m:
                break
            res.append(matrix[m - 1 - delta][i])
            counter += 1

        for i in range(m - 1 - delta, delta, -1):
            if counter == n * m:
                break
            res.append(matrix[i][delta])
            counter += 1

    if n % 2 and n == m:
        res.append(matrix[n // 2][n // 2])

    return res


print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
