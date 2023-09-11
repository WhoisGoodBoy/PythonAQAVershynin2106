

def test_test_luke(people_service):
    response = people_service.get_people("1")
    assert response.json()['name'] == 'Luke Skywalker'
