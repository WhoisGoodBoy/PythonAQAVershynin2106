from lesson24.infrastructure.people import People

def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'


def test_luke_with_fixture(people_service, first_people1):
    response = people_service.get_people("1")
    actual_people = People(
        **response.json()
    )
    assert actual_people == first_people1
