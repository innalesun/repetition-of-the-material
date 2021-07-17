'''
f = open('example.txt', 'r')
print(*f)
print(f)
f.close()
'''
'''
f = open('example.txt', 'r')
try:
    print(*f)
finally:
    f.close()
'''
'''
with open ('example.txt') as f:
    print(*f)
'''
'''
f = open('example.txt', 'r')
print(f.read(5))
print(f.read(5))
f.close()
'''
'''
x = open('txt.txt', 'r')

#print(x.readline())
print(x.readlines())
'''
'''
f = open('xyz.txt', 'w')
f.write('hello \n World')
f.close()
f = open('xyz.txt', 'r')
print(*f)
f.close()
'''
'''
import os

#os.rename('xyz.txt', 'abc.txt')

print(os.getcwd())

#os.mkdir('file')
#os.chdir('file')
print(os.getcwd())

os.chdir('..')

#os.makedirs('nested1/nested2/nested3')
'''

import os
#os.remove('abc.txt')

#os.rmdir('file')

os.removedirs('nested1/nested2/nested3')

