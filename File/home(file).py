'''
A = 'abcdefgh'
i = 1
I = ''
K = []
V = []
f = {}


while i <= 8:
    for j in A:
        I = str(i)+ str(j)
        print('i = {}, I = {}'.format(i,I))
        #if i == 1:
        V.append(str(i) + str(j))
        if j == 'a':
            V.append(str(i) + str (j))
        i += 1
        print(V)
'''
'''
A = 'abcdefgh'

I = ''
K = []
V = []
f = {}


for i in range(0,10):
    for j in A:
        I = str(i)+ str(j)
        print('i = {}, I = {}'.format(i,I))
        if i == 1:
            V.append(str(i) + str(j))
            if j == 'a':
                V.append(str(i) + str (j))


        print(V)
'''
'''
st = 'abcdefgh'
y = 0
num = '12345678'
x = 0


K = []
V = []



for i in range(1,9):
    for j in st:
        K = str(num[(x)])+ str(st[(y)])
        print(j, K)
        if i == int(num[x]):
            print(num[x])
            print(j)
            V.append(str(num[x]) + str(j))
            if j == st[y]:
                V.append(str(i) + str(st[y]))
        print(V)



        print(V)

'''
'''

# f = open('D:\Теория\Файлы.pptx','r' )
# print(f)
#print(*f)
# f.close()

# fd = open('Строки.pptx', 'r')
# print(fd)
# print(*fd)
# fd.close()

# ff = open('str.txt', 'r')
# print(ff)
# print(*ff)
# ff.close()
#
# g = open('стр.txt', 'r')
# print(g)
# print(*g)
# g.close()
#
# b = open('str.txt','r')
# try:
#     b.close()
# except:
#     print(b)

# ff = open('str.txt', 'r')
#
# ff.close()
# print(*ff)
'''
'''
try:

    with open('str.txt') as a:

        print(*a)
        print(a)
        print(a)

    print(*a)
except:
    print('yjyj')
'''
'''
import os
'''
'''
a = open('str.txt','r')
print(a.read(3))
print(a.read(3))
#print(a.read(3))
print(a.read())
a.close()
'''
'''
a = open('str.txt','r')
# print(a.readline())
#
# print(a.readline())
print(a.readlines())
a.close()
'''
'''
a = open('ddd.txt','w')
a.write('hello World. My name is Inna')
a.close()
# a = open('ddd.txt', 'r')
# print(*a)
# a.close()
import os
os.rename('ddd.txt','DDD.txt')
b = open('DDD.txt','r')
b.close()
print(*b)
'''
'''
import os
b = open('DDD.txt','r')
print(os.getcwd())
#os.mkdir('kkk')
b.close()

'''
'''
import os
print(os.getcwd())
#os.mkdir('new kanalog')
os.chdir('kkk')
print(os.getcwd())
s = open('KKK.txt','w')
print(s.write('my name is Inna. Hello, Inna'))
s.close()
s = open('KKK.txt', 'r')
print(*s)
s.close()

print(os.getcwd())
#os.mkdir('vk')
print(os.getcwd())
# os.chdir('vk')
# print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
os.chdir('List')
print(os.getcwd())
# z = open('control_home.py','r')
# print(*z)
# z.close()
print(os.getcwd())
os.chdir('..')
os.chdir('..')
os.chdir('..')
print(os.getcwd())
os.chdir('PycharmProjects/Яна/File/kkk')
print(os.getcwd())
os.chdir('..')
print(os.getcwd())

os.chdir('kkk')
print(os.getcwd())
os.remove('KKK.txt')
os.chdir('..')
print(os.getcwd())
os.rmdir('kkk')
os.remove('str.txt')
'''
'''
import os

os.remove('Строки.pptx')
'''
'''
import os
print(os.getcwd())
os.remove('8 ферзей.py')
'''
'''         # taks1

with open('task1.txt') as f:
    s = f.readline()
    print(*s)

s = s.replace('_',' ')
print(s)
l = s.split(' ')
print(l)

sum = 0
for i in l:
    if i.isdigit():
        print(i)
        i = int(i)
        sum += i
print(sum)

print(*f)

'''
'''
f = open('task2.txt')
b = []
n = []
s = f.readlines()
print(s)
#f.close() когда нужно и можно закрывать файл???
# a = 'python'
# print(a[:-1])
for i in s:
    i = i[:-1]
    if i.isalpha():
        i = str(i)
        b.append(i)
    elif i.isdigit():
        i = int(i)
        n.append(i)
print(b)
print(n)
b.sort()
n.sort()
mas = n + b
print(mas)
'''
'''
file_name = input('file_name: ')
f = open(file_name,'w')
# import os
# os.remove('task3.txt')
while True:
    s = input('s: ')
    if s == '':
        break
    f.write(s + '\n')
f.close()

# import os
# os.remove('task3.txt')
'''
'''
f = open('task4.txt')
s = f.readlines()
print(s)

print(len(s))
n = 0
for i in s:
    i = str(i)
    i = i[:-1]
    n += 1
    print(n, ':', len(i))
f.close() 
'''
'''
f = open('task4.txt')
n = 0
for i in f:
    n += 1
    print(i, ':', len(i))
print(n)
f.close()
'''
arr = ['Hello', '1', 'It', '25', 'began', '100%', 'lo56ng', '3', 'ago' 'in' 'Britain', '585']
f = open('task5.txt','w')
word = []
number = []

for i in arr:
    if i.isdigit():
        i = int(i)
        number.append(i)
    else:
        word.append(i)
word.sort()
number.sort()
s = word + number
print(s)

for i in s:
    f.write(str(i)+ '\n')

f.close()
