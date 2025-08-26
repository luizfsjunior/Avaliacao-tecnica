from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/leads_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Lead(Base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

class Contact(BaseModel):
    email: str
    phone: str

class LeadIn(BaseModel):
    full_name: str
    contact: Contact

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.post("/webhook")
def receive_lead(lead: LeadIn):
    db = SessionLocal()
    db_lead = Lead(
        nome=lead.full_name,
        email=lead.contact.email,
        telefone=lead.contact.phone
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    db.close()
    return {"id": db_lead.id, "nome": db_lead.nome, "email": db_lead.email, "telefone": db_lead.telefone}
