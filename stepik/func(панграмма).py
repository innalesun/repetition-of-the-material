# Напишите функцию Python, чтобы проверить, является ли строка панграммой или нет
# Панограммы - это слова или предложения, содержащие каждую букву алфавита хотя бы один раз.
# Например: «Быстрая коричневая лиса перепрыгивает через ленивую собаку»

# import string
#
# print(string.ascii_letters) # для вывода латинского алфавита
print(ord('а'))
print(ord('ё'))
print(ord('А'))
print(ord('Ё'))
a = ord('а')


# русский алфавит во всех регистрах
# z = ''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)] + \
#             [chr(i) for i in range(a - 32, a - 26)] + [chr(a - 47)] + [chr(i) for i in range(a - 26, a)])

def foo(st):
    abc = ''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)])

    for el in abc:
        if el in st:
            pass
        elif el not in st:
            print('this is not a pangram')
            break
    else:
        print('this is a pangram')


foo(input('введите строку для проверки '))

# решение задачи через множество
# import string, sys
#
#
# def ispangram(str1, alphabet=string.ascii_lowercase):
#     alphaset = set(alphabet)
#     return alphaset <= set(str1.lower())
#
#
# print(ispangram('The quick brown fox jumps over the lazy dog'))