# Напишите программу на Python для суммирования всех элементов в словаре

def func_sum():
    S = 0
    d = {1: 10, 2: 20, 3: 'oo', 4: 'ppp', 5: 100, 'U': 125}
    for i in d.values():
        if type(i) is int:
            S += i

    return S


print(func_sum())


# вывод значений словаря
d_new = {1: 10, 2: 20, 3: 333, 4: 444, 5: 100, 'U': 125}
print(d_new.values())
