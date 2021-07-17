'''
p = lambda x=1,y=2:x**y
s = p
print(s(5))
'''

def f_func():
    print('test func1')

def sec_func():
    print('test func2')

def sim_func(fn):

    print('start')
    fn()
    print('stop')
    
a = sim_func(f_func())
b = sec_func(sec_func())
    


'''
def simple_decore(fn):

    print('start function')

    fn()
    print('stop function')
    #return wrapper()

@simple_decore
def firs_test():
    print('test function1')
'''


'''
def season(a):
    if a == 1 or a == 2 or a == 12:
        print('зима')
    elif a == 3 or a == 4 or a == 5:
        print('весна')
    elif a == 6 or a == 7 or a == 8:
        print('лето')
    elif a == 9 or a == 10 or a == 11:
        print('осень')

season(int(input('введите номер месяца')))

'''
'''
import random
a = [random.randint(0,100) for i in range(10)]
def sr(a):
    return sum(a)/10

print(sr(a))
'''
