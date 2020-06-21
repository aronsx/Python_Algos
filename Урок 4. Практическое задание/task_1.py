"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import timeit
import cProfile

import time


def timer(func):
    def wrapper():
        start = time.time()
        return func


start_1 = time.time()
N = int(input('Введите n: '))
Q = -0.5
START = 1
SUMM = 0

while N:
    N -= 1
    SUMM += START
    START *= Q

print(SUMM)
end_1 = time.time() - start_1
print(f'Время выполнения скрипта через цикл = {end_1}')


def memorize(func):
    def wrapper(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r

    return wrapper


# @memorize
def sequence(num, start=1):
    if not num:
        return 0
    return start + sequence(num - 1, start / -2)


start_2 = time.time()
# N = int(input('Введите n: '))
end_2 = time.time() - start_2
print(f'Время выполнения скрипта через рекурсию = {end_2}')
print(f'Скрипт через цикл выполняется бытрее на {end_1 - end_2}')

input('Продолжить')

print(sequence(N))
# print(memorize(sequence(N)))
print('Проверка через функции через timeit:',
      timeit.timeit('sequence(N)', setup='from __main__ import sequence, N', number=1000))
print('Работа cProfile: ')
# print(timeit.timeit('memorize(sequence(N))', setup='from __main__ import sequence, N, memorize', number=10))
try:
    cProfile.run(sequence(N))
    # cProfile.run(memorize(sequence(N)))
except TypeError as e:
    pass

input('Продолжить')

start_3 = time.time()
for char_num in range(32, 128):
    if (char_num - 2) % 10 == 0:
        print()
    print(f'{char_num:4} - {chr(char_num)}', end=' ')
end_3 = time.time() - start_3

print('\n \n')


def ascii_table(num):
    if num == 32:
        return f' {num:4} - {chr(num)}'
    if (num - 2) % 10 == 0:
        return f'{ascii_table(num - 1)}\n {num:4} - {chr(num)}'
    return f'{ascii_table(num - 1)}{num:4} - {chr(num)}'


start_4 = time.time()
print(ascii_table(127))
end_4 = time.time() - start_4

print(f'Время выполнения скрипта через цикл: {end_3}')
print(f'Время выполнения скрипта через цикл: {end_4}')
print(f'Скрипт через цикл выполняется бытрее на {end_3 - end_4}')


@memorize
def ascii_table_2(num):
    if num == 32:
        return f' {num:4} - {chr(num)}'
    if (num - 2) % 10 == 0:
        return f'{ascii_table(num - 1)}\n {num:4} - {chr(num)}'
    return f'{ascii_table(num - 1)}{num:4} - {chr(num)}'


print()
test1 = timeit.timeit('ascii_table(127)', setup='from __main__ import ascii_table', number=1000)
print('Проверка через функции через timeit:', test1)

test2 = timeit.timeit('ascii_table_2(127)', setup='from __main__ import ascii_table_2', number=1000)
print('Проверка через функции через timeit c меморизацией:', test2)

print(f'Функция с меморизацией работает на {test1 - test2} быстрее')
# cProfile.run(ascii_table(127))  # Не разобрался почему не работает
