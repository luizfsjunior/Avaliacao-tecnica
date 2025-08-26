# 01-webhook-leads-fastapi

## Objetivo
Receber dados de leads via webhook e salvar no banco PostgreSQL.

## Mapeamento dos campos
- Recebido: `{ "full_name": "Maria Oliveira", "contact": { "email": "maria@teste.com", "phone": "11999998888" } }`
- Banco (tabela `leads`):
  - `nome` ← `full_name`
  - `email` ← `contact.email`
  - `telefone` ← `contact.phone`

## Como rodar
1. Configure o PostgreSQL no docker-compose.
2. Execute `docker-compose up`.
3. Acesse a API em `http://localhost:8000`.

## Endpoints
- `POST /webhook` - Recebe e salva lead.

## Estrutura
- `main.py` - FastAPI principal
- `models.py` - Modelos SQLAlchemy
- `Dockerfile` e `docker-compose.yml` - Setup Docker
- `requirements.txt` - Dependências
- `exemplo.json` - JSON para teste
