Projeto VetCare+ — Sistema interativo de apoio à consulta veterinária.

# VetCare+ — Plataforma Clínica Veterinária (MVP)

Aplicação web em Python (FastAPI) com SQLite.

## Docker
```
docker compose up --build
# http://localhost:8000/docs
```
## Local
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

