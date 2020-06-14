"""Числа Фибоначчи"""


def fib(n, sum):
    if n < 1:
        return sum
    return fib(n-1, sum+n)


c = 998
# c = 998 - уже не работает
# необузданная рекурсия вызывает переполнение стека
print(fib(c, 0))
