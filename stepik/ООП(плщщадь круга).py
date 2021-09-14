# Программа получает на вход радиус и вычисляет площадь круга и длину окружности, используя классы.
import math


class Circle():
    def __init__(self, r):
        self.r = r

    def leng(self):
        return 2 * self.r * math.pi

    def square(self):
        return (self.r ** 2 * math.pi) / 4


r = int(input('r '))
ob = Circle(r)
print(ob.leng())
print(ob.square())

#print("Площадь круга:", round(ob.square(), 2)) # округление результата до 2 знаков после запятой
