import requests

url = "http://localhost:8000/paises/top10"
response = requests.get(url)
print("Status:", response.status_code)
print("Resposta:", response.json())
