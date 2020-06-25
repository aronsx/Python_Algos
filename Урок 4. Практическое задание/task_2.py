"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from sys import getsizeof


def num_generator():
    i = 2
    while True:
        yield i
        i += 1

def get_elem_i(func):
    def wrapper

def eratosfen(input_list):
    for divider in input_list:
        for divided in input_list:
            if divider != divided and divided % divider == 0:
                list_a.remove(divided)
    return input_list


def linear_simple(input_list):
    """Решение без метода решета Эратосфена, можно передать генератор"""
    simple_list = [2]
    for divider in input_list:
        count = 0
        for divided in simple_list:
            if divider != divided and divider % divided == 0:
                count += 1
        if not count:
            simple_list.append(divider)
    return simple_list[1:]


len_list = 100
list_a = [item for item in range(2, len_list + 1)]
list_b = list(range(len_list + 1)[2:])
list_c = (item for item in range(2, len_list + 1))
list_d = {item for item in range(2, len_list + 1)}
list_e = num_generator()

print(linear_simple(list_c))
print(eratosfen(list_a))


