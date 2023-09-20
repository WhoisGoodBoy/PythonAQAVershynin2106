import lesson25.infrastructure as infra
import json
import requests


def test_get_object():
    print(infra.get_an_object(4).json())
    assert infra.get_an_object(4).status_code == 200

def test_create_an_object():
    response, obj_id = infra.create_an_object()
    get_response = infra.get_an_object(obj_id)
    assert response.status_code==200
    assert get_response.status_code==200
    print(get_response.json())
    print(bool(''))

def test_update_object():
    response, obj_id = infra.create_an_object()
    changed_obj = infra.update_an_object(obj_id, {"name": "name is no more Apple", "data": {"color": "white", "generation": "3rd", "price": 135}})
    assert response.status_code == 200
    assert changed_obj.status_code == 200
    print(changed_obj.json())


def test_delete_object():
    response, obj_id = infra.create_an_object()
    deleted_obj = infra.delete_an_object(obj_id)
    assert deleted_obj.status_code == 200
    print(deleted_obj.json())

def test_try_to_authenticate():
    auth_request = infra.go_to_saucedemo_auth()
    print()

def test_try_to_login_reqres():
    auth_request =infra.go_to_reqres_auth()
    print(auth_request.json()['token'])

def test_login_and_create():
    auth_request = infra.go_to_reqres_auth()
    create_user = infra.create_user(auth_request.json()['token'])
    print()


def test_negative():
    try:
        r = requests.get('https://google.com/nothere')
        assert r.status_code == 404
        r.raise_for_status()
    except requests.exceptions.InvalidURL as err:
        print(err)