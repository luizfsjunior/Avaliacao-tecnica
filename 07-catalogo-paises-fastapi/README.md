# 07-catalogo-paises-fastapi

## Objetivo
API para listar, buscar e avaliar países, consumindo REST Countries e salvando avaliações no PostgreSQL.

## Funcionalidades
- Listar os 10 países mais populosos: `GET /paises/top10`
- Buscar país por nome: `GET /paises/buscar?nome=brasil`
- Avaliar país: `POST /paises/avaliar`

## Como rodar
1. Configure o PostgreSQL no docker-compose.
2. Execute `docker-compose up`.
3. Acesse a API em `http://localhost:8000`.

## Estrutura
- `main.py` - FastAPI principal
- `models.py` - Modelos SQLAlchemy
- `Dockerfile` e `docker-compose.yml` - Setup Docker
- `requirements.txt` - Dependências
