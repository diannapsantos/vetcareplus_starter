from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()
class Sintomas(BaseModel):
    febre: float | None = None
    letargia: bool = False
    vomitos: bool = False

def prioridade_regras(s: Sintomas) -> str:
    score = 0
    if s.febre and s.febre >= 40: score += 2
    if s.letargia: score += 1
    if s.vomitos: score += 1
    return ['Baixa','Média','Alta','Crítica'][min(score,3)]

@router.post('/', summary='Calcula prioridade por regras simples')
def triage(s: Sintomas):
    return {'priority': prioridade_regras(s)}
