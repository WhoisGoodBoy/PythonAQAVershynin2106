class Building:
    def __init__(self,name, address):
        self.name = name
        self.address = address
        self.stages = {}

    def __len__(self):
        return len(self.stages)

    def __setitem__(self, key, value):
        self.stages[key] = value

    def __getitem__(self, item):
        return self.stages[item]


class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry

    def __str__(self):
        return f'This is {self.name} from {self.industry} industry. Welcome'

building_1 = Building('Citadel', 'Nova Prospect 1')
toyota = Company('Toyota', 'Auto')
tesla = Company('Tesla', 'Auto')
building_1[1] = toyota
building_1[2] = tesla
print(len(building_1))
print(building_1[2].)