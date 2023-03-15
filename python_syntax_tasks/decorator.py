import time

import random


def get_run_time(func):
    def wrapper(*args, **kwargs):
        start = time.process_time()
        result = func(*args, **kwargs)
        end = time.process_time()
        return {'result': result, 'run_time': end - start}
    return wrapper


@get_run_time
def create_random_list(first: int, last: int, amount: int, builtin_type: str = 'list') -> list:
    if builtin_type == 'list':
        random_list = [random.randint(first, last) for _ in range(amount)]
    elif builtin_type == 'generator':
        random_list = (random.randint(first, last) for _ in range(amount))
    else:
        raise 'incorrect builtin type'
    return random_list


res_list = 0
res_gen = 0
for i in range(100000):
    res_list += create_random_list(1, 100, 100)['run_time']
    res_gen += create_random_list(1, 100, 100, builtin_type="generator")['run_time']

res_list, res_gen = round(res_list, 3), round(res_gen, 3)
print(f'{res_list=}\n{res_gen=}')
