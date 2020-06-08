"""
Вычисление факториала с помощью цикла for
"""

NUMB = int(input("Введите число, для которого ищем факториал: "))

FACTORIAL = 1
for i in range(2, NUMB+1):
    FACTORIAL *= i

print(f"Факториал: {FACTORIAL}")
