"""Угадай число"""

print("Придумайте число от 10 до 15")
input("и нажмите Enter: ")

NUMB = input("Ваше число больше 13-х? (y/n) ")

if NUMB == 'y':
    NUMB = input("Ваше число 14? (y/n) ")
    if NUMB == 'n':
        print("Ваше число 15")
else:
    NUMB = input("Ваше число 11? (y/n) ")
    if NUMB == 'n':
        NUMB = input("Ваше число 12? (y/n) ")
        if NUMB == 'n':
            print("Ваше число 13")

print("Я угадал!")
