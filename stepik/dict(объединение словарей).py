# Напишите скрипт Python для объединения следующих словарей для создания нового
# Пример словаря:
# dic1 = {1:10, 2:20}
# dic2 = {3:30, 4:40}
# dic3 = {5: 50,6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

print(id(dic1))
dic1.update(dic2)
dic1.update(dic3)

d = dic1.copy()
print((d, id(d)))

dic4 = {} # еще одно решение
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)
