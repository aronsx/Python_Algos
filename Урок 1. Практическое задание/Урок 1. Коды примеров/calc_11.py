"""Расчет краски"""

from math import pi

D_PARAM = float(input("Диаметр бака: "))
H_PARAM = float(input("Высота бака: "))
S_PARAM = int(input("Окрашиваемая площадь одной банкой: "))

CIRCLE = pi * D_PARAM**2 / 4
CYLINDER = pi * D_PARAM * H_PARAM
# учитываем и внутреннюю поверхность
TOTAL = CIRCLE * 4 + CYLINDER * 2
# количество банок краски
QTY = TOTAL / S_PARAM
QTY = int(QTY) + 1
print(f"Количество требуемых банок: {QTY}")
