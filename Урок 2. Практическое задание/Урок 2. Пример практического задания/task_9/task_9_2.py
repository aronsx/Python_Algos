"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
"""


def recur_method(quantity, steps, highest_numb, max_sum):
    """Рекурсия"""
    summ = 0
    try:
        numb = input("Введите число: ")
        for i in numb:
            summ += int(i)
        if summ > max_sum:
            max_sum = summ
            highest_numb = numb
        steps += 1
        if steps == quantity:
            return f"Наибольшее число по сумме цифр: {highest_numb}, сумма его цифр: {max_sum}"
        else:
            return recur_method(quantity, steps, highest_numb, max_sum)
    except ValueError:
        print("Вы вместо числа ввели строку (((. Исправьтесь")

STEPS = 0
HIGHEST_NUMB = 0
MAX_SUM = 0

try:
    QUANT = int(input("Введите количество чисел: "))
    print(recur_method(QUANT, STEPS, HIGHEST_NUMB, MAX_SUM))
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
