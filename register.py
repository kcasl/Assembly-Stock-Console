import requests

url = "http://3.36.171.50:8000/register"

while True:
    std_id = input("고유학번 입력 :")
    username = input("이름 입력 :")
    password = input("비번 입력 :")
    capital = float(input("시작 돈 :"))

    data = {
        "std_id": std_id,
        "username": username,
        "password": password,
        "capital": capital
    }

    response = requests.post(url, json=data)

    print(response.status_code)
    print(response.json())
