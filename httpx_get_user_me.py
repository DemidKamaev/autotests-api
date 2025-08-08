import httpx


url = 'http://localhost:8000/api/v1/authentication/login'

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {
  "email": "Demid@example.com",
  "password": "Pes90-nya70"
}

response = httpx.post(url, headers=headers, json=data)
print(f"Код ответа {response.status_code}")
res = response.json()['token']['accessToken']
print(res)


url1 = 'http://localhost:8000/api/v1/users/me'

headers1 = {
    "accept": "application/json",
    "Authorization": f"Bearer {res}"
}

response = httpx.get(url1, headers=headers1)
print(f"Код ответа {response.status_code}")
print(response.json())



