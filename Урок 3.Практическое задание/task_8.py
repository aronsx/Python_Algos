"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

1-я строка:
3
3
3
3
2-я строка:
3
3
3
3
3-я строка:
3
3
3
3
4-я строка:
3
3
3
3
5-я строка:
3
3
3
3

[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
[3, 3, 3, 3, 12]
"""
from random import randint  # захардкодил, чтобы было проще проверять

for idx in range(5):
    list_a = []
    for idy in range(4):
        list_a.append(randint(1, 9))
    SUM_STRING = 0
    for idz in list_a:
        SUM_STRING += idz
    list_a.append(SUM_STRING)
    print(list_a)
