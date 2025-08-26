from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import List

class Lead(BaseModel):
    nome: str
    email: str
    telefone: str

app = FastAPI()

DEST_API_URL = "https://httpbin.org/post"

@app.post("/send-leads")
def send_leads(leads: List[Lead]):
    if len(leads) > 1000:
        raise HTTPException(status_code=400, detail="Máximo de 1000 leads por vez.")
    results = []
    for i in range(0, len(leads), 100):
        batch = leads[i:i+100]
        try:
            resp = requests.post(DEST_API_URL, json=[lead.dict() for lead in batch], timeout=10)
            success = resp.status_code == 200 or resp.status_code == 201
            results.append({"batch": i//100+1, "success": success, "status": resp.status_code})
        except Exception as e:
            results.append({"batch": i//100+1, "success": False, "error": str(e)})
    return {"results": results}
