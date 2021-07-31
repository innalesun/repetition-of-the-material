'''
class Car:

    def start(self):
        print('двигатель заведен')


car_a = Car()

print(Car)
print(car_a)

print(dir(Car))
print(dir(car_a))
'''
'''
class Car:

    def __str__(self):
        return "car class object"

    def start(self):
        print('двигатель заведен')


car_a = Car()
print(car_a)
print(dir(Car))
print(dir(car_a))
car_a.start()
'''

class Human:

    # Статические поля
    default_name = 'No name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    # Статический метод
    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')

    def earn_money(self, amount):
        self.__money += amount
        print(f'Earned {amount} money! Current value: {self.__money}')


if __name__ == '__main__':

    Human.default_info()

    alexander = Human('Sasha', 27)
    alexander.info()

    alexander.earn_money(5000)
    alexander.earn_money(20000)
    alexander.info()
 #   print(alexander.__money) #AttributeError: 'Human' object has no attribute '__money'
    print(alexander._Human__money)# обратиться к принту приватного поля через класс

#    human_object.make_deal(object_house1)# может из другого кода пока не удаляю

