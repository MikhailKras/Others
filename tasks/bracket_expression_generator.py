def solution(cur: str, opened: int, closed: int, n: int) -> None:
    if len(cur) == 2*n:
        print(cur)
        return
    if opened < n:
        solution(cur+'(', opened+1, closed, n)
    if closed < opened:
        solution(cur+')', opened, closed+1, n)


def parens(n):
    return solution("", 0, 0, n)


parens(20)



