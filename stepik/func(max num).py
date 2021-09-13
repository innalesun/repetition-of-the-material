# Напишите функцию Python, чтобы найти максимум трех чисел


# #вариант 1: на вход подается 1 аргумент - числа, введенные в консоль в одну строку через запятую
# def func_max(a):
#     l = [int(i) for i in a.split(',')]
#     return max(l)
#
#
# print(func_max(input()))

# l = [int(i) for i in input().split(',')]
# print(l)

# #вариант 2: на вход подается 1 аргумент - числа, введенные в консоль в одну строку через пробел
# def func_max(a):
#     l = [int(i) for i in a.split()]
#     return max(l)
#
#
# print(func_max(input()))

# вариант 3: на вход подается 3 аргументa- числа, введенные в консоль поочередно(столбиком)

l = []


def func_max(a, b, c):
    l.append(a)
    l.append(b)
    l.append(c)
    return max(l)


print(func_max(int(input()), int(input()), int(input())))
