# пример факториала: 5!=1х2х3х4х5=120.
# Напишите функцию Python для вычисления факториала числа (неотрицательное целое число).
# Функция принимает число в качестве аргумента

def foo(n):
    if n != 0:
        return n * foo(n - 1)
    return 1


print(foo(int(input())))
