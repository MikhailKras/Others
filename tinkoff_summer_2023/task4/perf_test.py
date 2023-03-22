from task import get_answer

from random import randint

from time import process_time

n = 2 * 10 ** 3
max_time = 0
i = 0
while max_time < 1:
    lst = [randint(1, 2 * 10 ** 5) for _ in range(n)]
    start = process_time()
    get_answer(n, lst)
    end = process_time()
    print(max_time)
    if end - start > max_time:
        max_time = end - start
    i += 1
else:
    print(max_time)

