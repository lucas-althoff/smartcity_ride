from typing import Optional
from pydantic import BaseModel


class Resposta(BaseModel):
    message: str
    content: Optional[dict]


class Indicador(BaseModel):
    id: int
    nome: str
    dimensao: str
    topico: str


class Indicadores(BaseModel):
    indicadores: str


class Variavel(BaseModel):
    id_variavel: str
    municipio: str
    nome: str
