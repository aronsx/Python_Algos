"""Функция Аккермана"""


def recursion(m, n):
    """Рекурсивное решение функции"""
    # Базовый случай
    # Последний шаг рекурсии
    if m == 0:
        return n + 1
    # Шаг рекурсии / рекурсивное условие
    elif m > 0 and n == 0:
        return recursion(m - 1, 1)
    # Шаг рекурсии / рекурсивное условие
    elif m > 0 and n > 0:
        return recursion(m - 1, recursion(m, n - 1))


print(recursion(0, 2))
