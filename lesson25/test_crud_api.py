import lesson25.infrastructure as infra
import json


def test_get_object():
    print(infra.get_an_object(4).json())
    assert infra.get_an_object(4).status_code == 200

def test_create_an_object():
    response, obj_id = infra.create_an_object()
    get_response = infra.get_an_object(obj_id)
    assert response.status_code==200
    assert get_response.status_code==200
    print(get_response.json())

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
