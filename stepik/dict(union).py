# Напишите программу на Python, чтобы объединить два словаря, добавляя значения для общих ключей.
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# Пример вывода: Счетчик ({'a': 400, 'b': 400, 'd': 400, 'c': 300})


def func_union(a, b):
    for k, v in b.items():
        if k not in a.keys():
            a[k] = v
        elif k in a.keys():
            a[k] += v

    return a

c = {'a': 100, 'b': 200, 'c': 300}
d = {'a': 300, 'b': 200, 'd': 400}

print(func_union(c, d))

# решение с модулем collections
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)