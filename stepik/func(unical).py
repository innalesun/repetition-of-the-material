# Напишите функцию Python, которая берет список и возвращает новый список с уникальными элементами
# первого списка.
# на ввод подается например 1,5,9,9,9,5


def unical(ls):
    ls_new = []

    for i in ls:
        if i not in ls_new:
            ls_new.append(i)

    return ls_new


a = [int(i) for i in input().split(',')]
print(unical(a))

print(unical.__doc__)
print(unical.__name__)

# ls = [int(i) for i in input().split(',')]
# print(ls)
