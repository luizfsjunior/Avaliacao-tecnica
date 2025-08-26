from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests, os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/fanout_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class FanoutLog(Base):
    __tablename__ = "fanout_logs"
    id = Column(Integer, primary_key=True, index=True)
    api_url = Column(String, nullable=False)
    success = Column(Boolean, default=False)
    error_message = Column(String, nullable=True)

class DataIn(BaseModel):
    nome: str
    email: str
    telefone: str

app = FastAPI()

API_URLS = [
    "https://httpbin.org/post",
    "https://postman-echo.com/post",
    "https://reqres.in/api/users"
]

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/fanout")
def fanout(data: DataIn):
    db = SessionLocal()
    results = []
    payload = data.dict()
    for url in API_URLS:
        try:
            resp = requests.post(url, json=payload, timeout=5)
            success = resp.status_code == 200 or resp.status_code == 201
            error_message = None if success else f"Status: {resp.status_code}"
        except Exception as e:
            success = False
            error_message = str(e)
        log = FanoutLog(api_url=url, success=success, error_message=error_message)
        db.add(log)
        results.append({"api_url": url, "success": success, "error": error_message})
    db.commit()
    db.close()
    return {"results": results}
