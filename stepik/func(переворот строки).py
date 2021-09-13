# Напишите программу на Python для обращения строки
# Пример строки : «1234abcd»
# Ожидаемый результат : "dcba4321"

def func_str(st):
    return st[::-1]


print(func_str(input()))
