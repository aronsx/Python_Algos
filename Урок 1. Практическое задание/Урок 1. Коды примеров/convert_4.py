"""Конвертация"""

NUMB = int(input("Число: "))
CHANGE_TYPE = input("Перевести в байты (b) или килобайты (k): ")
if CHANGE_TYPE == 'b':
    print(f"{NUMB} Кб = {NUMB * 1024} байт")
elif CHANGE_TYPE == 'k':
    print(f"{NUMB} байт = {NUMB / 1024} Кб")
