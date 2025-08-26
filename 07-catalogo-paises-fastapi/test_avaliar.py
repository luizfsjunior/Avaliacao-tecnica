import requests
import json

url = "http://localhost:8000/paises/avaliar"
data = {"country": "Brazil", "vote": "like"}
response = requests.post(url, json=data)
print("Status:", response.status_code)
print("Resposta:", response.json())
