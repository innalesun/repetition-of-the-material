# Программа принимает на вход длину и ширину прямоугольника и вычисляет его площадь с использованием классов

class Square():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def func_square(self):
        return self.a * self.b


a = int(input('длина: '))
b = int(input('ширина: '))
qw = Square(a, b)
print(qw.func_square())

# Решение задачи
# Принимаются значения длины и ширины прямоугольника.
# Создаем класс и при помощи конструктора инициализируем его значения.
# Создаем метод под названием func_square, который будет вычислять площадь прямоугольника.
# Создаем объект данного класса.
# Используя этот объект, вызываем метод func_square с параметрами длины и ширины, полученными от пользователя.
# Выводим значение площади прямоугольника на экран.
