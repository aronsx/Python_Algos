"""Генерация случайного целого и дробного числа в диапазоне"""

from random import random

LEFT = int(input("Минимальная граница: "))
RIGHT = int(input("Максимальная граница: "))
NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
print(NUMB)

LEFT = float(input("Минимальная граница: "))
RIGHT = float(input("Максимальная граница: "))
NUMB = random() * (RIGHT - LEFT) + LEFT
print(round(NUMB, 3))
