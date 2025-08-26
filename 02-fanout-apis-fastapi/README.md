# 02-fanout-apis-fastapi

## Objetivo
Receber dados e enviar para 3 APIs diferentes, registrando erros sem interromper o fluxo.

## Lógica
- Para cada API, tenta enviar os dados.
- Se falhar, registra o erro e continua para as próximas.
- Salva status no banco.

## Como rodar
1. Configure o PostgreSQL no docker-compose.
2. Execute `docker-compose up`.
3. Acesse a API em `http://localhost:8000`.

## Endpoints
- `POST /fanout` - Envia dados para múltiplas APIs.

## Estrutura
- `main.py` - FastAPI principal
- `models.py` - Modelos SQLAlchemy
- `Dockerfile` e `docker-compose.yml` - Setup Docker
- `requirements.txt` - Dependências
- `exemplo.json` - JSON para teste
