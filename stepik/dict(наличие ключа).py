# Напишите скрипт Python, чтобы проверить, существует ли данный ключ в словаре

def key_in_dict(k):
    d = {1: 10, 2: 20, 3: 'oo', 4: 'ppp', 5: 100, 'U': 125}
    if k in d.keys():
        return d[k]
    else:
        return False

a = input('введите предполагаемый ключ: ')
if a.isdigit():
    print(key_in_dict(int(a)))
else:
    print(key_in_dict(a))
