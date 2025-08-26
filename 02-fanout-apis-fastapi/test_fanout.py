import requests
import json

json_path = "exemplo.json"
url = "http://localhost:8000/fanout"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Resposta:", response.json())
