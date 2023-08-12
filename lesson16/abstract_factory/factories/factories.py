from abc import ABC, abstractmethod


class BeerFactory(ABC):
    _beer_type = ''

    @abstractmethod
    def get_beer(self, name):
        pass