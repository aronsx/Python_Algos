from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        res = time() - start
        print(f"Время выполнения заняло {res}.")
    return wrapper


@timer
def main(n):
    def fib_mem(n):
        if n < 2:
            return 1
        return fib_mem(n-2) + fib_mem(n-1)
    fib_mem(n)

main(30)
