"""Поиск максимального числа"""

# Вариант 1
NUMB_A = int(input('Первое число: '))
NUMB_B = int(input('Второе число: '))
NUMB_C = int(input('Третье число: '))
MIDDLE = NUMB_A
if MIDDLE < NUMB_B:
    MIDDLE = NUMB_B
if MIDDLE < NUMB_C:
    MIDDLE = NUMB_C
print(MIDDLE)


# Вариант 2
NUMB_A = int(input('Первое число: '))
NUMB_B = int(input('Второе число: '))
NUMB_C = int(input('Третье число: '))

if NUMB_A > NUMB_B:
    if NUMB_A > NUMB_C:
        print(NUMB_A)
    else:
        print(NUMB_C)
else:
    if NUMB_B > NUMB_C:
        print(NUMB_B)
    else:
        print(NUMB_C)
