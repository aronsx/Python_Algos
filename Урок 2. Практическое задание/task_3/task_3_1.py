"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

Подсказка:
Используйте арифм операции для формирования числа, обратного введенному

Пример:
Введите число: 123
Перевернутое число: 321

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

USER_INPUT = int(input('Введите число: '))

REVERSE_NUM = 0

while USER_INPUT:
    REVERSE_NUM = REVERSE_NUM * 10 + USER_INPUT % 10
    USER_INPUT = USER_INPUT // 10

print(REVERSE_NUM)
