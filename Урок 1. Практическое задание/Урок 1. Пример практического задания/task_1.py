"""
Задание 1.
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
#print(124 // 100) = 1 - отбросить остаток
#print((124 // 10) % 10) = 2 - остаток от деления числа 12 на 10
#print(124 % 10) = 4 - остаток от деления числа 124 на 10

Пример: Целое трехзначное число 123
Сумма = 6
Произведение = 6

Подсказка: для получения отдельных цифр числа используйте арифм. операции
и НЕ ИСПОЛЬЗУЙТЕ операции с массивами
"""

try:
    NUMB = int(input("Введите целое трехзначное число: "))

    RES_1 = NUMB // 100
    RES_2 = (NUMB // 10) % 10
    RES_3 = NUMB % 10

    print(f"Сумма = {RES_1 + RES_2 + RES_3}")
    print(f"Произведение = {RES_1 * RES_2 * RES_3}")

except ValueError:
    print("Вы вместо трехзначного числа ввели строку (((. Исправьтесь")
