"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""


def print_result_dif(letter_a, letter_b):
    """Выводит количество букв между введенными буквами"""
    print(f'Букв между: {abs(ord(letter_a) - ord(letter_b)) - 1 if letter_a != letter_b else 0}')


def print_letter_num(letter_a, letter_b, start):
    """Выводит положение каждой буквы в алфавите"""
    print(f'Первая буква стоит на месте {ord(letter_a) - start + 1}')
    print(f'Вторая буква стоит на месте {ord(letter_b) - start + 1}')


first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')

if ord(first_letter) > 1000 and ord(second_letter) > 1000:
    print_result_dif(first_letter, second_letter)
    print_letter_num(first_letter, second_letter, 1072)
elif ord(first_letter) < 123 and ord(second_letter) < 123:
    print_result_dif(first_letter, second_letter)
    print_letter_num(first_letter, second_letter, 97)
else:  # не учитывал язки, отличные от en, ru
    print('Вы ввели буквы из рвзных языков')
