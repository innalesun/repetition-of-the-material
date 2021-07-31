class Tomato:
    states = {0: 'green', 1: 'yellow', 2: 'orange', 3: 'red'}

    def __init__(self, _index):
        self._index = _index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
            print(Tomato.states[self._state])
        else:
            print(
                f'к томату {self._index} на стадии созревания {Tomato.states[self._state]} применить метод не возможно. томат созрел ')

    def is_ripe(self):
        if self._state == 3:
            print('томат созрел')
            return True
        else:
            print("еще не созрел")
            return False

    def print_states(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(1, num)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.is_ripe() == True:

                print(True)
                break

            elif i.is_ripe() == False:

                print(False)
                break

    def give_away_all(self):
        for i in self.tomatoes:
            if i.is_ripe() == True:
                self.tomatoes.clear()


class Gardener:
    def __init__(self, name, _plant):
        self.name = name
        self._plant = _plant

    # def work(self):
    #     if self._plant == Tomato(self):
    #         print(self._plant.grow())
    #     elif self._plant == TomatoBush():
    #         print(self._plant.grow_all())

    def work(self):
        print(self._plant.grow())

    def harvest(self):
        if self._plant.is_ripe() == True:
            print(f'садовник {self.name} собрал урожай {self._plant}')
        else:
            print(f"собирать урожай садовнику {self.name} еще рано")

    @staticmethod
    def knowledge_base():
        print('справка по садоводству,,,,')


if __name__ == '__main__':
    Gardener.knowledge_base()

    tom1 = Tomato(1)
    Sacha = Gardener('Alex', tom1)
    tom1.grow()
    gard.work()
    gard.harvest()
    gard.work()
    gard.harvest()

    # tomb1 = TomatoBush(4)
    # tomb1.grow_all()
    # tomb1.all_are_ripe()
    # tomb1.give_away_all()
    # Maxim = Gardener('Max', tomb1)
    # Maxim.work()




