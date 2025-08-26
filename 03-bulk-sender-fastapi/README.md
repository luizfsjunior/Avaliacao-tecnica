# 03-bulk-sender-fastapi

## Objetivo
Receber uma lista de 1.000 leads e enviar em lotes de 100 para uma API destino, sem perda ou repetição.

## Lógica
- Divide a lista em lotes de 100.
- Envia cada lote sequencialmente.
- Garante envio completo.

## Como rodar
1. Execute `docker build -t bulk-sender .` e `docker run -p 8000:8000 bulk-sender`.
2. Acesse a API em `http://localhost:8000`.

## Endpoints
- `POST /send-leads` - Envia lista de leads em lotes.

## Estrutura
- `main.py` - FastAPI principal
- `Dockerfile` - Setup Docker
- `requirements.txt` - Dependências
- `exemplo.json` - lista de 1000 leads teste
