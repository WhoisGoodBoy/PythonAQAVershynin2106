class Donkey:
    strength = 10

    @classmethod
    def print_strength(cls):
        print(cls, cls.strength)

class Horse:
    speed = 20
    strength = 15

    @classmethod
    def print_strength(cls):
        print(cls, cls.strength)


class Mul(Horse, Donkey):
    pass

mul1 = Mul()
print(mul1.strength)
print(mul1.speed)
mul1.print_strength()


class Human:
    def m(self):
        print('A')

class Child1(Human):
    def m(self):
        print('B')

class Child2(Human):
    def m(self):
        print('C')


class GrandChild(Child1,Child2):
    def m(self):
        print('D')

    def m_from_second_parent(self):
        Child2.m(self)

grandchild = GrandChild()
grandchild.m()
grandchild.m_from_second_parent()
