def get_answer(n, lst):
    counter_dict = dict()
    l = 1
    max_counter = 0
    for i in range(n):
        counter_dict[lst[i]] = counter_dict.get(lst[i], 0) + 1
        if counter_dict[lst[i]] > max_counter:
            max_counter = counter_dict[lst[i]]
        min_counter = min(counter_dict.values())
        if max_counter - min_counter == 1:
            counter_max_counter = list(counter_dict.values()).count(max_counter)
            counter_min_counter = list(counter_dict.values()).count(min_counter)
            if counter_max_counter == 1:
                l = i + 1
                continue
            elif counter_min_counter == 1 and min_counter == 1:
                sort_dict_values = sorted(counter_dict.values())
                if len(sort_dict_values) > 1:
                    if sorted(counter_dict.values())[1] == max_counter:
                        l = i + 1

        if min_counter == 1:
            counter_min_counter = list(counter_dict.values()).count(min_counter)
            if counter_min_counter == 1:
                sort_dict_values = sorted(counter_dict.values())
                if len(sort_dict_values) > 1:
                    if sorted(counter_dict.values())[1] == max_counter:
                        l = i + 1
                        continue

        if max_counter == min_counter == 1:
            l = i + 1
    return l


if __name__ == '__main__':
    n = int(input())
    lst = list(map(int, input().split()))
    print(get_answer(n, lst))
