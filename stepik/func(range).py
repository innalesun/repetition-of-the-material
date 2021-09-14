# Напишите функцию Python, чтобы проверить, находится ли число в заданном диапазоне
# for i in range(5, 1, -1):
#     print(i)

def func_range(a, b, d):
    if a < b:
        if a <= d < b:
            print('Yes')
        else:
            print('No')

    elif a > b:
        if a >= d > b:
            print('Yes')
        else:
            print('No')


func_range(5, -8, -7)
