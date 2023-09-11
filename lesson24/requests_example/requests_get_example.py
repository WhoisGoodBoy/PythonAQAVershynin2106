from requests import get
url = 'https://reqres.in/'
headers = {
    "ContentType":"application/json"
}
response = get(url + "api/users?page=2", headers=headers)
print(response.json())
