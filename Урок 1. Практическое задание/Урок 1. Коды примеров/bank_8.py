"""Банковский вклад"""

AMOUNT = int(input("Сколько хотите взять денег: "))
PCT = float(input("Под какой процент вам их дают: "))
YEARS = float(input("Насколько лет берете: "))

PCT = PCT / 100
MONTH_PAY = (AMOUNT * PCT * (1 + PCT)**YEARS) / (12 * ((1 + PCT)**YEARS - 1))
print(f"Ваш месячный платеж составит: {round((MONTH_PAY), 2)}")

SUMMA = MONTH_PAY * YEARS * 12
print(f"За весь период вы заплатите: {round((SUMMA), 2)}")
print(f"Это составит {round(((SUMMA / AMOUNT) * 100), 2)} от первоначальной суммы")
