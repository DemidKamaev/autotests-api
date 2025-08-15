import httpx
from tools.fakers import get_random_email


# Создаем пользователя
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
create_user_response_data = response.json()
print('Create user:', create_user_response_data)


# Проходим аутентификацию
url_2 = 'http://localhost:8000/api/v1/authentication/login'
login_data = {
  "email": data['email'],
  "password": data['password']
}

response = httpx.post(url_2, headers=headers, json=login_data)
print(response.status_code)
login_response_data = response.json()
print('Login data:', login_response_data)


# Изменение данных
update_user_headers = {
  "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

update_data = {
  "email": get_random_email(),
  "lastName": "Bet4",
  "firstName": "User4",
  "middleName": "BU_4"
}

user_id = create_user_response_data['user']['id']
update_user_response = httpx.patch(f"http://localhost:8000/api/v1/users/{user_id}",
                                   headers=update_user_headers, json=update_data)
print(update_user_response.status_code)
update_user_response_data = update_user_response.json()
print('Update user:', update_user_response_data)
