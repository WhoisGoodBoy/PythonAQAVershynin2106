class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name


class Cat:
    def make_noise(self):
        pass


class Lion(Cat):
    def __init__(self):
        self.color = 'yellow'
        self.age = 12
        self.speed = 60
        self.character = 'Pride'

    def make_noise(self):
        print('Roar')


class Cheetah(Cat):
    def __init__(self):
        self.color = 'black'
        self.age = 10
        self.speed = 120
        self.character = 'Friendly'

    def make_noise(self):
        print('meow')


king = Lion()
sweet_cheetah = Cheetah()
print(king.color)
king.make_noise()
sweet_cheetah.make_noise()
