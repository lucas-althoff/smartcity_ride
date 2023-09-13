import os
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from backend.src.database import ObjetoSQL
import json

rotas = APIRouter()
templates_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'utils')
templates = Jinja2Templates(directory=templates_path)


def criar_saida(content, message=''):
    return {"message": message,
            "content": content}


@rotas.get(path="/",
           responses={200: {"description": "Ok", "content": {"image/jpeg": {"example": "pagina"}}},
                      400: {"description": "not found"}},
           tags=["Home"],
           name="Página inicial",
           description="Apresenta página inicial do projeto")
async def home(request: Request):
    """
    Função que renderiza a página estática home.
    :returns: Página inicial
    :rtype: fastapi.Request
    """
    return templates.TemplateResponse("index.html", {"request": request})


@rotas.get(path="/indicadores",
           responses={200: {"message": "Ok", "content": ""},
                      400: {"description": "not found"}},
           tags=["indicadores"],
           name="Indicadores",
           description="Consulta Indicadores")
async def indicadores():
    """
    Função que consulta uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    supa_cliente = ObjetoSQL()
    dados = supa_cliente.processar_query_select(tabela='indicadores')
    print(dados)
    return criar_saida(dados)


@rotas.post(path="/indicadores",
            responses={201: {"description": "Created", "content": ""},
                       400: {"description": "not found"}},
            tags=["indicadores"],
            name="Insert Indicadores",
            description="Alimentar Tabela Indicadores")
async def post_indicadores(request: dict):
    """
    Função que renderiza a página estática home.
    :returns: Página inicial
    :rtype: fastapi.Request
    """
    supa_cliente = ObjetoSQL()
    print(request, type(request))
    dados = supa_cliente.processar_query_insert(tabela='indicadores', dados=request)
    return criar_saida(dados)