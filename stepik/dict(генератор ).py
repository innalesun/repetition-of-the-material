# Напишите скрипт Python для генерации и печати словаря, который содержит
# число(от 1 до n) в форме (x, x * x)

def func_generator(n):
    d = {x: x * x for x in range(1, n + 1)}
    return d


a = int(input(' введите число: '))
print(func_generator(a))
