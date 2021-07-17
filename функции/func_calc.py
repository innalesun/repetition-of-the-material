x = float(input('введите число 1: '))
y = float(input('введите число 2: '))


def plus_function(x, y):
    return x + y


def subtract_function(x, y):
    return x - y


def multi_function(x, y):
    return x * y


def div_function(x, y):
    if y == 0:
        return 'делить на 0 нельзя'
    else:
        return x / y


while True:

    c = input('введите операцию(если введен 0, то выход из программы): ')

    if c == '+':
        print(plus_function(x, y))
    elif c == '-':
        print(subtract_function(x, y))
    elif c == '*':
        print('%.4f' % multi_function(x, y))
    elif c == '/':
        print(div_function(x, y))
    else:
        if c != '0':
            print('некорректная операция')
        else:
            break
