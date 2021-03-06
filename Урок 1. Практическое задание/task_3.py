"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""

X1_VAL = int(input("Введите x1: "))
Y1_VAL = int(input("Введите y1: "))
X2_VAL = int(input("Введите x2: "))
Y2_VAL = int(input("Введите y2: "))

try:
    k = (Y2_VAL - Y1_VAL) / (X2_VAL - X1_VAL)
    b = Y1_VAL - k * X1_VAL
    print(f'Уравнение прямой: y = {k}x + {b}')
except ZeroDivisionError as zero_err:
    print('Ошибка:', zero_err)
