'''
class Human:
    name = 'Andy'
    age = 30
    address = []

andy:Human = Human()
samantha:Human = Human()
print(andy)
print(samantha)
print(andy.name)
print(samantha.name)
samantha.address = [1,2]
andy.address = [2,1]
andy.address.append(5)
print(andy.address)
print(samantha.address)
'''

class Human:
    def __init__(self, name, age, address='1 st', hair_color='black'):
        self.__name = name
        self.__age = age
        self.address = address
        self.hair_color = hair_color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name



    def modify_age(self, new_age):
        self.__age = new_age

    @classmethod
    def from_age_and_name(cls, name, age):
        return cls(name, age, '2 st', 'white')

    @staticmethod
    def get_me_something():
        print('hello')

francenstein = Human.from_age_and_name('Francenstein', 5)
print(francenstein.hair_color)
andy = Human('Andy', 30,'1 street', 'black')
samantha = Human('Samantha', 20, None, None)

print(samantha.name)
samantha.name = 'Samanta 2000 pro Turbo'
print(samantha.name)
samantha.get_me_something()
samantha.modify_age(21)
