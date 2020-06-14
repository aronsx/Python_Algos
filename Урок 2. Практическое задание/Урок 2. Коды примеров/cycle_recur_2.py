"""Реализации через цикл и рекурсию"""


def lst_sum_cycle(num_lst):
    """Цикл"""
    total_sum = 0
    for el in num_lst:
        total_sum = total_sum + el
    return total_sum


print(lst_sum_cycle([1, 3, 5, 7, 9]))


def lst_sum_rec(num_lst):
    """Рекурсия"""
    if len(num_lst) == 1:
        return num_lst[0]
    else:
        return num_lst[0] + lst_sum_rec(num_lst[1:])


print(lst_sum_rec([1, 3, 5, 7, 9]))
# 1 - 3, 5, 7, 9
# 3 - 5, 7, 9
# 5 - 7, 9
# 7 - 9