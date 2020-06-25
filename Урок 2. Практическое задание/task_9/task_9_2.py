"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

MAX_SUM_NUM = 0
MAX_NUM = 0


def get_max_sum(count, max_sum=0, max_num=0):
    def num_sum(num, sum_n=0):  # сделать рекурсию передаем число и предыдущую сумму
        a, b = 0, 0
        if not num:
            return sum_n
        else:
            a += num % 10
            b //= 10
            return next_num(b, a)

    next_num = int(input('Введите очередное число: '))
    print(num_sum(next_num))
    # cache, input_cache = 0, next_num

    # num_sum(next_num)
    # while next_num:
    #     cache += next_num % 10
    #     next_num //= 10
    # if max_sum_num < cache:
    #     max_sum_num = cache
    #     max_num1 = input_cache
    get_max_sum(count - 1)


print(f'Наибольшее число по сумме цифр: {MAX_NUM}, сумма его цифр: {MAX_SUM_NUM} ')
count_num = int(input('Введите количество чисел: '))


get_max_sum(count_num)


# def num_sum(num, sum_n=0):  # сделать рекурсию передаем число и предыдущую сумму
#     if not num:
#         return sum_n
#     else:
#         sum_n += num % 10
#         num //= 10
#         return num_sum(num, sum_n)


# print(num_sum(count_num))
