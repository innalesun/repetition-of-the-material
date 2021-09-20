# Напишите программу на Python для удаления ключа из словаря

d = {'n': 250, 'b': 100, 'a': 500, 'c': 400, 'm': 50}


def func_del(key):
    if key in d:
        val = d[key]
        del d[key]
        return val
    else:
        return 'в словаре отсутствует заданный ключ '


a = input('введите ключ ')
print(func_del(a))
