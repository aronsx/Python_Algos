"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

USER_NUM = int(input('Введите число: '))

EVEN = 0
UNEVEN = 0
LAST_NUM = 0

while USER_NUM:
    last_num = USER_NUM % 10
    if last_num % 2 == 0:
        EVEN += 1
    else:
        UNEVEN += 1
    USER_NUM = USER_NUM // 10

print('Четные:', EVEN)
print('Не четные:', UNEVEN)
