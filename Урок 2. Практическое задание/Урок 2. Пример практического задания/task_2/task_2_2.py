"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def recur_method(numb, even=0, odd=0):
    """Рекурсия"""
    # все цифры числа извлечены
    if numb == 0:
        return even, odd
    else:
        # достаем очередную цифру числа
        cur_n = numb % 10
        # число естественно становится короче
        numb = numb // 10
        # проверяем цифра четная или нечетная
        if cur_n % 2 == 0:
            even += 1
            return recur_method(numb, even, odd)
        else:
            odd += 1
            return recur_method(numb, even, odd)


try:
    NUMB = int(input("Введите натуральное число: "))
    print(f"Количество четных и нечетных цифр в числе равно: {recur_method(NUMB)}")
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
