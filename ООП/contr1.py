'''
def palindrom(a):
    if a == a[::-1]:
        print('это палиндром')
    else:
        print('это не палиндром')

palindrom("кукла")
#palindrom("мадам")
'''




'''

class Tomato:
    states = {0: 'green', 1: 'yellow', 2: 'red'}

    def __init__(self, _index):
        self._index = _index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
            print(self._state)

    def is_ripe(self):
        if self._state == 2:
            print('томат созрел')
        else:
            print("еще не созрел")

    def print_states(self):
        print(f'Tomat {self._index} is {Tomato.states[self._state]}')


object1 = Tomato(5)
print(type(Tomato.states))
object1.is_ripe()
object1.print_states()
object1.grow()

object1.grow()
object1.print_states()
'''
'''

class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()


# object_ = TomatoBush(4)
# object_.grow_all()

    def all_are_ripe(self):
        for tomato in self.tomatoes:
'''




