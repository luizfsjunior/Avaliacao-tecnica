import requests
import json

# Caminho do arquivo JSON de exemplo
json_path = "exemplo.json"

# URL do endpoint FastAPI
url = "http://localhost:8000/webhook"

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Resposta:", response.json())
