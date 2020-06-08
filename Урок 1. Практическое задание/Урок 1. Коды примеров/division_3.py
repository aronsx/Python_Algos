"""Деление"""

NUMB_A = int(input('a = '))
NUMB_B = int(input('b = '))
if NUMB_B != 0:
    if NUMB_A % NUMB_B == 0:
        print(f"{NUMB_A} делится на {NUMB_B} без остатка")
    else:
        print(f"{NUMB_A} не делится на {NUMB_B} без остатка")
        print(f"Остаток: {NUMB_A % NUMB_B}")
    print(f"Частное: {NUMB_A // NUMB_B}")
else:
    print("Вы ввели недопустимый делитель")
