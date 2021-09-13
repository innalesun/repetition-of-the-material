# Напишите функцию Python для умножения всех чисел в списке. Перейти к редактору
# Список образцов : (8, 2, 3, -1, 7)
# Ожидаемый результат : -336

def func_multi(t):
    multi = 1
    for el in t:
        multi *= el
    return multi


print(func_multi(tuple([int(i) for i in input().split(',')])))
