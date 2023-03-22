def get_answer(n, a_list):
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + a_list[i - 1]
    last_dict = {0: 0}
    last_i = 0
    ans = 0
    for j in range(1, n + 1):
        if prefix_sum[j] not in last_dict:
            last_dict[prefix_sum[j]] = j
            continue
        i = last_dict[prefix_sum[j]] + 1
        if i <= last_i:
            continue
        counter_l = i - last_i
        counter_r = n - j + 1
        ans += counter_l * counter_r
        last_i = i
        last_dict[prefix_sum[j]] = j
    return ans


if __name__ == '__main__':
    n = int(input())
    a_list = list(map(int, input().split()))
    print(get_answer(n, a_list))
#
# n = int(input())  # Вводим длину массива
# a = list(map(int, input().split()))  # Сам массив вводим
# p = [0] * (n + 1)  # Массив префиксных сумм
# for i in range(1, n + 1):
#     p[i] = p[i - 1] + a[i - 1]  # Считаем префиксные суммы
# last = {0: 0}  # Таблица для того, чтобы быстро узнавать где последний раз видели такую же префиксную сумму
# lastI = 0  # Предыдущая позиция i для j, такой что [i, j] является разумным
# ans = 0  # Храним ответ
# for j in range(1, n + 1):
#     if p[j] not in last:  # Если такой префикс не встречался раньше
#         last[p[j]] = j  # Запомним, что префиксная сумма p[j] последний раз встречалась на позиции j.
#         continue
#     i = last[p[j]] + 1  # Так как мы нашли, такой i, что p[j] = p[i], тогда a[i + 1], a[i + 2], ... + a[j] = 0
#     if i <= lastI:
#         continue
#     cntL = i - lastI  # Количество вариантов выбрать l для нормального подотрезка
#     cntR = n - j + 1  # Количество способов выбрать r для нормального подотрезка
#     ans += cntL * cntR  # Количество способов выбрать l, r.
#     lastI = i
#     last[p[j]] = j
# print(ans)
