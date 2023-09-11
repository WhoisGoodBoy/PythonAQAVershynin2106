import pytest
from lesson24.infrastructure.people_service import PeopleService

@pytest.fixture()
def people_service():
    yield  PeopleService()