# Напишите программу на Python, чтобы получить словарь из полей объекта

class Phone:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def check_sim(self, mobile_operator):
        if self.model == '1785' and mobile_operator == 'MTS':
            print('Your mobile operator is MTS')
        else:
            print('невозможно определить принадлежность с моб.оператору')


my_phone = Phone('blue', '1785')
print(my_phone.__dict__)

'''


class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'

    def do_nothing(self):
        pass


test = dictObj()
print(test.__dict__)
'''
