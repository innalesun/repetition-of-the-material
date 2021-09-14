import math

class Circle():

    def leng(self, r):
        return 2 * r * math.pi

    def square(self, r):
        return (r ** 2 * math.pi) / 4


r = int(input(' input r '))
ob = Circle()
print(ob.leng(r))
print(ob.square(r))

