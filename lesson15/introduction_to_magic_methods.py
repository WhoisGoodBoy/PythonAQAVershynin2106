'''import  datetime
class Traffic_light:
    numbers_someone_called_height = []
    def __init__(self):
        self.__color = 'Green'
        self.height = 3
    def __str__(self):
        return f'Hi I`m traffic_light instance, and my current color_status is {self.__color}'

    def __repr__(self):
        return 'Traffic_light()'

    def __getattr__(self, item):
        return f'this is not {item} you are looking for'

    def __getattribute__(self, item):
        if item.startswith('height'):
            Traffic_light.numbers_someone_called_height.append(datetime.datetime.now())
        return super().__getattribute__(item)




traffic_light_1 = Traffic_light()
print(traffic_light_1)
#traffic_light_2 = eval(repr(traffic_light_1))
#print(traffic_light_2)
print(traffic_light_1.height)
'''

class Horse:
    def __init__(self):
        self.speed = 5
        self.age = 4

    def __add__(self, other):
        print(type(other))
        #if other.__class__.__name__.startswith('Horse'):
        if type(other) == Horse:
            return Horse()
        else:
            return Mul(other.strenght, self.speed)

    def __iadd__(self, other):
        self.age += other.age
        return self

    def __eq__(self, other):
        return self.age == other.age

class Donkey:
    def __init__(self):
        self.strenght = 10
        self.age = 5

    def __add__(self, other):

        return Mul(other.speed, self.strenght)

    def __radd__(self, other):
        return Mul(other.speed, self.strenght)

    def __del__(self):
        print('his gone, my friend, don`t cry')

class Mul:
    def __init__(self, strenght, speed):
        self.strenght = strenght
        self.speed = speed

    def __str__(self):
        return f'{self.__class__.__name__}\nspeed:{self.speed}\nstrenght:{self.strenght}'

horse = Horse()
donkey = Donkey()
mul = horse + donkey
mul2 = Mul(1,2)
horse2 = Horse()
horse3 = horse + horse2
print(horse3)
print(mul)
print(mul2)
del horse
print(horse3 == horse2)
horse2 += donkey
print(horse2.age)
print(horse2 == horse2)

