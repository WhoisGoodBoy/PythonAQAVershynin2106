

class People:
    def __init__(self,
    name,
    height,
    mass,
    hair_color,
    skin_color,
    eye_color,
    birth_year,
    gender,
    homeworld,
    films,
    species,
    vehicles,
    starships,
    created,
    edited,
    url):
        self.name=name
        self.height=height
        self.mass=mass
        self.hair_color=hair_color
        self.skin_color=skin_color
        self.eye_color=eye_color
        self.birth_year=birth_year
        self.gender=gender
        self.homeworld=homeworld
        self.films=films
        self.species=species
        self.vehicles=vehicles
        self.starships=starships
        self.created=created
        self.edited=edited
        self.url=url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
