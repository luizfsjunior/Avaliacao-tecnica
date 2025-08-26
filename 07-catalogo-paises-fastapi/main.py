from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests, os
from models import Base, Country, Vote

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/countries_db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

REST_COUNTRIES_URL = "https://restcountries.com/v3.1/all?fields=name,population,continents"

class CountryOut(BaseModel):
    name: str
    population: int
    continent: str
    votes_like: int
    votes_dislike: int

class VoteIn(BaseModel):
    country: str
    vote: str 

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


def get_or_create_country(db, name, population, continent):
    country = db.query(Country).filter(Country.name == name).first()
    if not country:
        country = Country(name=name, population=population, continent=continent)
        db.add(country)
        db.commit()
        db.refresh(country)
    return country

@app.get("/paises/top10", response_model=list[CountryOut])
def top10():
    db = SessionLocal()

    resp = requests.get(REST_COUNTRIES_URL, timeout=10)
    if resp.status_code != 200:
        db.close()
        raise HTTPException(status_code=502, detail="Erro ao consultar API de países.")
    countries = resp.json()

    sorted_countries = sorted(countries, key=lambda c: c.get("population", 0), reverse=True)[:10]
    result = []
    for c in sorted_countries:
        name = c.get("name", {}).get("common", "")
        population = c.get("population", 0)
        continent = c.get("continents", [""])[0]
        country = get_or_create_country(db, name, population, continent)
        result.append(CountryOut(
            name=country.name,
            population=country.population,
            continent=country.continent,
            votes_like=country.votes_like,
            votes_dislike=country.votes_dislike
        ))
    db.close()
    return result

@app.get("/paises/buscar", response_model=CountryOut)
def buscar(nome: str = Query(..., description="Nome do país")):
    db = SessionLocal()
    resp = requests.get(f"https://restcountries.com/v3.1/name/{nome}", timeout=10)
    if resp.status_code != 200:
        db.close()
        raise HTTPException(status_code=404, detail="País não encontrado na API.")
    c = resp.json()[0]
    name = c.get("name", {}).get("common", "")
    population = c.get("population", 0)
    continent = c.get("continents", [""])[0]
    country = get_or_create_country(db, name, population, continent)
    result = CountryOut(
        name=country.name,
        population=country.population,
        continent=country.continent,
        votes_like=country.votes_like,
        votes_dislike=country.votes_dislike
    )
    db.close()
    return result

@app.post("/paises/avaliar")
def avaliar(vote_in: VoteIn):
    db = SessionLocal()
    country = db.query(Country).filter(Country.name == vote_in.country).first()
    if not country:
        db.close()
        raise HTTPException(status_code=404, detail="País não encontrado.")
    if vote_in.vote not in ["like", "dislike"]:
        db.close()
        raise HTTPException(status_code=400, detail="Voto deve ser 'like' ou 'dislike'.")

    vote = Vote(country_id=country.id, vote=vote_in.vote)
    db.add(vote)
    if vote_in.vote == "like":
        country.votes_like += 1
    else:
        country.votes_dislike += 1
    db.commit()
    db.refresh(country)
    db.close()
    return {
        "country": country.name,
        "status": "sucesso",
        "votes_like": country.votes_like,
        "votes_dislike": country.votes_dislike
    }
