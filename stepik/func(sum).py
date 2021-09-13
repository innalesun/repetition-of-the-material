# Напишите функцию Python для суммирования всех чисел в списке
# Список образцов : (8, 2, 3, 0, 7)

def func_sum(l):
    sum_ = 0
    for elem in l:
        sum_ += elem
    return sum_


print(func_sum([int(i) for i in input().split(',')]))
