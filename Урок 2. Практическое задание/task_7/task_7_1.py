"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""

N = int(input('Введите число N: '))
SUMM = 0

for num in range(N):
    SUMM += num + 1
print(SUMM == N * (N + 1) / 2)
