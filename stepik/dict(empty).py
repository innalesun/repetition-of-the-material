# Напишите программу на Python, чтобы проверить, является ли словарь пустым или нет


def func_empty(d):
    if len(d) == 0:
        print('empty')
    elif len(d) != 0:
        print('not empty!')


a = {1: 'kkk'}
func_empty(a)

# another interesting solution

my_dict = {1: 'kkk'}
if not bool(my_dict):
    print("Dictionary is empty")
else:
    print('Dictionary is not empty!')
