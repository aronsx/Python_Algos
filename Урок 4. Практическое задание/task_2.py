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
from timeit import timeit


def num_generator():
    i = 2
    while True:
        yield i
        i += 1


def get_elem_i(func):
    def wrapper(*args, **kwargs):
        i = kwargs.get('i')
        a = func(*args, **kwargs)
        return a[i - 1]

    return wrapper


def modify_list(func):
    def wrapper(*args, **kwargs):
        i = kwargs.get('i')
        _list = get_list(i)
        a = func(_list, **kwargs)
        return a[i - 1]

    return wrapper


# @get_elem_i
@modify_list
def eratosfen(input_list, **kwargs):
    _list = input_list[:]
    for divider in _list:
        for divided in _list:
            if divider != divided and divided % divider == 0:
                _list.remove(divided)
    return _list


# @get_elem_i
@modify_list
def linear_simple(input_list, **kwargs):
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


def get_list(i):  # генерю каждый раз исключительно для тестов
    _len = i * 10
    _list = [item for item in range(2, _len + 1)]
    return _list


i_elem = 10
len_list = i_elem * 10
list_a = [item for item in range(2, len_list + 1)]
list_f = list_a[:]
# list_b = list(range(len_list + 1)[2:])
# list_c = (item for item in range(2, len_list + 1))
# list_d = {item for item in range(2, len_list + 1)}
# list_e = num_generator()

# print(linear_simple(list_f, i=i_elem))
print(linear_simple(i=1))
print(linear_simple(i=10))
print(linear_simple(i=100))
print(linear_simple(i=1000))
# print(eratosfen(list_a, i=i_elem))
print(eratosfen(i=1))
print(eratosfen(i=10))
print(eratosfen(i=100))
print(eratosfen(i=1000))

# print(timeit('eratosfen(list_a, 1)', setup='from __main__ import eratosfen')
