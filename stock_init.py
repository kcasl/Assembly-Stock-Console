import requests

url = "http://3.36.171.50:8000/stock_init"

response = requests.get(url)

print(response.status_code)
print(response.json())
