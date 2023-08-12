from .factories import BeerFactory
from .hardened_beer import HardenedBeer


class LagerFactory(BeerFactory):
    _beer_type = 'lager'

    def __init__(self):
        self.name = 'Rogan'
        self.__positions = ['lager', 'hardened']

    @property
    def positions(self):
        return self.__positions

    def get_beer(self, name):
        if name == 'lager':
            return 'here`s your lager'
        elif name == 'hardened':
            return HardenedBeer()