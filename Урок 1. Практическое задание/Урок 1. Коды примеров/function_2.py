"""Функция y"""

while True:
    NUMB_X = int(input('Введите x: '))
    if NUMB_X > 0:
        NUMB_Y = 2 * NUMB_X - 10
    elif NUMB_X == 0:
        NUMB_Y = 0
    else:
        NUMB_Y = 2 * abs(NUMB_X) - 1

    print(NUMB_Y)
