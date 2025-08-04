import requests

url = "https://aptekiplus.ru/api/v2/cart/preorders"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

data = {
    "retailId": ""
    "regionId": 33,
    "cityId": "3300000100000000000000000",
    "paymentType": "online"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)


