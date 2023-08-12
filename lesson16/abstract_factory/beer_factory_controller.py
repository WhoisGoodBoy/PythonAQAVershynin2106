from factories.lager_factory import LagerFactory
from factories.stout_factory import StoutFactory

class AbstractBeerFactory:
    @staticmethod
    def get_factory(beer_type):
        if beer_type == 'lager':
            return LagerFactory()
        elif beer_type == 'stout':
            return StoutFactory()

lager_factory_1 = AbstractBeerFactory.get_factory('lager')
bottle_of_hardened_beer = lager_factory_1.get_beer('hardened')
print(bottle_of_hardened_beer)