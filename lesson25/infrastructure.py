import requests
import json
from requests.auth import HTTPBasicAuth
from requests.exceptions import HTTPError

url = "https://api.restful-api.dev/objects"
class Mac:
    def __init__(self, object_id, name, data=''):
        self.object_id = object_id
        self.name=name
        self.data = data



def get_an_object(object_id):
    response = requests.get(f"{url}/{object_id}")
    return response

def create_an_object():
    headers = {"content-type": "application/json"}
    payload = json.dumps({"name": "Apple AirPods", "data": {"color": "white", "generation": "3rd", "price": 135}})
    response = requests.post(url, data=payload, headers=headers)
    return response, response.json()['id']

def update_an_object(obj_id, changed_dict):
    headers = {"content-type": "application/json"}
    payload = json.dumps(changed_dict)
    response = requests.put(f'{url}/{obj_id}', data=payload, headers=headers)
    return response

def delete_an_object(obj_id):
    response = requests.delete(f'{url}/{obj_id}')
    return response

def go_to_saucedemo_auth():
    response = requests.get('https://www.saucedemo.com/', auth=HTTPBasicAuth('stand!ard_user', 'secret_sauce'))
    return response

def go_to_reqres_auth():
    data = {"email": "eve.holt@reqres.in","password": "cityslicka"}
    return requests.post('https://reqres.in/api/login', json=data)

def create_user(token):
    headers = {"content-type": "application/json",
               'token':token}
    return requests.post('https://reqres.in/api/users', json={
    "name": "morpheus",
    "job": "leader"
},headers=headers)



