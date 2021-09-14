# Напишите скрипт Python для сортировки (возрастания и убывания) словаря по ключу

d = {'n': 250, 'b': 100, 'a': 500, 'c': 400, 'm': 50}

print(d)
K = []

for i in d.keys():
    K.append(i)

print(K, type(K))

K_1 = sorted(K)
d_1 = {el: d[el] for el in K_1}
print(d_1)

K_2 = sorted(K, reverse=True)
d_2 = {el: d[el] for el in K_2}
print(d_2)

# import operator
#
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# print('Original dictionary : ', d)
# sorted_d = sorted(d.items(), key=operator.itemgetter(0))
# print('Dictionary in ascending order by value : ', sorted_d)
# sorted_d = dict(sorted(d.items(), key=operator.itemgetter(0), reverse=True))
# print('Dictionary in descending order by value : ', sorted_d)
