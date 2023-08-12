from .factories import BeerFactory


class StoutFactory(BeerFactory):
    _beer_type = 'stout'

    def __init__(self):
        self.name = 'Guiness'
        self.__positions = ['classic', 'milk']

    @property
    def positions(self):
        return self.__positions

    def get_beer(self, name):
        if name == 'classic':
            return 'here`s your classic'
        elif name == 'milk':
            return 'here`s your milk stout'