import pytest
from lesson24.infrastructure.people_service import PeopleService
from lesson24.infrastructure.people import People
from lesson24.infrastructure.test_data_sample_first_person import first_person_dict

@pytest.fixture()
def people_service():
    yield  PeopleService()


@pytest.fixture()
def first_people():
    yield People(
        name="Luke Skywalker",
        height="172",
        mass="77",
        hair_color="blond",
        skin_color="fair",
        eye_color="blue",
        birth_year="19BBY",
        gender="male",
        homeworld="https://swapi.dev/api/planets/1/",
        films=[
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/6/",
        "https://swapi.dev/api/films/3/",
        "https://swapi.dev/api/films/1/"
        ],
        species=[
        ],
        vehicles=[
        "https://swapi.dev/api/vehicles/14/",
        "https://swapi.dev/api/vehicles/30/"
        ],
        starships=[
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/22/"
        ],
        created="2014-12-09T13:50:51.644000Z",
        edited="2014-12-20T21:17:56.891000Z",
        url="https://swapi.dev/api/people/1/"
    )


@pytest.fixture()
def first_people1():
    yield People(**first_person_dict
    )