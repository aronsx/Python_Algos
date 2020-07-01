"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
from random import randrange
from timeit import timeit


def bubble(lst):
    _list = lst[:]
    n = 1
    while n < len(_list):
        for idx in range(len(_list) - n):
            if _list[idx] < _list[idx + 1]:
                _list[idx], _list[idx + 1] = _list[idx + 1], _list[idx]
        n += 1
    return _list


def bubble_opt(lst):
    _list = lst[:]
    n = 1
    while n < len(_list):
        change = False
        for idx in range(len(_list) - n):
            if _list[idx] < _list[idx + 1]:
                _list[idx], _list[idx + 1] = _list[idx + 1], _list[idx]
                if not change:  # без проверки на каждой итерации в переменную присваивалось True, что в конечном итоге замедляло работу функции и она отрабатывала медленнее, чем первая функция.
                    change = True
        if not change:
            break
        n += 1
    return _list


list_a = [randrange(-100, 100) for _ in range(1000)]
print(list_a)  # исходный список
print(bubble(list_a))  # результат работы первой функции
print(bubble_opt(list_a))  # результат работы второй функции

print(timeit('bubble(list_a)', setup='from __main__ import bubble, list_a', number=100))
print(timeit('bubble_opt(list_a)', setup='from __main__ import bubble_opt, list_a', number=100))
