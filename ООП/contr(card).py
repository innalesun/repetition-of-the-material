def card(a):
    print('*' * (len(a) - 4) + a[-4::])


card(input('введите номер карты '))
