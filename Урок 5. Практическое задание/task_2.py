"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""

from  collections import deque
# try:
#     number_1 = collections.deque(int(num, 16) for num in list(input('Введите первое число: ')))
#     number_2 = collections.deque(int(num, 16) for num in list(input('Введите второе число: ')))
#     print(number_1)
#     print(number_2)
# except ValueError as ve:
#     print('Вы ввели не число: ', ve)

test = deque('f123d')
test2 = deque('234d')
print(int(test))
print(test)
print(test2)

