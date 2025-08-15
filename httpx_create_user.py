import httpx
from tools.fakers import get_random_email


url = 'http://localhost:8000/api/v1/users'

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {
  "email": get_random_email(),
  "password": "rem4mom-7",
  "lastName": "Bet",
  "firstName": "User",
  "middleName": "BU"
}

response = httpx.post(url, headers=headers, json=data)
print(response.status_code)
print(response.json())


url_2 = 'http://localhost:8000/api/v1/authentication/login'

data_2 = {
  "email": "Bet4User@example.com",
  "password": "rem4mom-7"
}


response = httpx.post(url_2, headers=headers, json=data_2)
print(response.status_code)
data_res = response.json()
print(data_res)


url_3 = f"http://localhost:8000/api/v1/users/{data_res['user']['id']}"

data_3 = {
  "email": "Bet4User@example.com",
  "lastName": "Bet4",
  "firstName": "User4",
  "middleName": "BU_4"
}

response = httpx.patch(url_3, headers=headers, json=data_3)
print(response.status_code)
print(response.json())
