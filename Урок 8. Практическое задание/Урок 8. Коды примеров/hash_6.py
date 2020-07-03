"""
Для шифрования строк предназначен модуль hashlib.
"""

import hashlib

'''
рара

рар
ра
р
а
ар
ара
'''

'''
Сохраняем хэши всех подстрок в множество.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
'''

s = input("Введите строку из маленьких латинских букв: ")
r = set()

N = len(s)
for i in range(N):
    if i == 0:
        N = len(s) - 1
    else:
        N = len(s)
    for j in range(N, i, -1):
        print(s[i:j])
        '''
        возвращается как строковый объект двойной длины, содержащий только
        шестнадцатеричные цифры. Это может использоваться для безопасного
        обмена значениями в электронной почте или других недвоичных средах.
        digest() - набор байтов
        hexdigest() - строка
        '''
        r.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
print(r)


print("Количество различных подстрок в строке '%s' равно %d" % (s, len(r)))


import hashlib


user_str = input('Введите строку состоящую из маленьких букв\n')
lists = []
for i in range(0, len(user_str) + 1):
    for j in range(i + 1, len(user_str) + 1):
        lists.append(hashlib.sha1(user_str[i:j].encode('utf-8')).hexdigest())

lists.remove(hashlib.sha1(user_str.encode('utf-8')).hexdigest())


print(f'Колличество различных подстрок в строке {user_str} равно {len(set(lists))}')




from collections import Counter
import hashlib


string = list('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab')


s = 0
substring = Counter()

for letter_start in range(len(string)):


    if s == 0:
        e = len(string) - 1
    else:
        e = len(string)

    for letter_end in range(e - s):
        hash_obj = hashlib.md5()

        hash_obj.update(''.join(string[s:e]).encode())
        substring[hash_obj.hexdigest()] += 1
        if len(string[s:e]) == 1:
            print(string[s:e], hash_obj.hexdigest())
        e -= 1
    s += 1

