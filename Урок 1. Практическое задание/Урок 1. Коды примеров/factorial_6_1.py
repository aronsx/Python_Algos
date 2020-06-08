"""
вычисление факториала через цикл while
n! = 1*2*...*n
"""

NUMB = int(input("Введите число, для которого ищем факториал: "))

FACTORIAL = 1
while NUMB > 1:
    FACTORIAL *= NUMB
    NUMB -= 1

print(f"Факториал: {FACTORIAL}")
