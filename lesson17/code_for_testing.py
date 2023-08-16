class Human:
    def __init__(self,name,age,hair_color):
        self.__name = name
        self.__age = age
        self.__hair_color = hair_color


    def grow(self):
        self.__age+=1

    def change_color(self, new_color):
        if new_color not in ['black', 'white']:
            raise Exception('Ginger is not allowed here')
        self.__hair_color = new_color

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__hair_color
