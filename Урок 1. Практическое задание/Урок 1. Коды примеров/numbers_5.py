"""Определение простого числа"""

import sys
import math

NUMBER = int(input("Введите число: "))

if NUMBER < 2:
    print("Число должно быть больше 1")
    sys.exit(1)
elif NUMBER == 2:
    print("Это простое число")
    sys.exit(1)

# первый делитель
i = 2
# 19 -> 4.36
LIMIT = int(math.sqrt(NUMBER))
# 3 <= 4.36
# 4 <= 4.36
# 5 <= 4.36
while i <= LIMIT:
    if NUMBER % i == 0:
        print("Это сложное число")
        sys.exit(1)
    # переход к следующему делителю
    i += 1

print("Это простое число")
