import json
from ast import literal_eval
from fastapi import APIRouter
from backend.src.database import ObjetoSQL
from backend.src.schemas import Indicadores
from backend.src.utils import criar_saida

rota_ind = APIRouter()


@rota_ind.get(path="/indicadores",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Indicadores"],
              name="Consultar Indicadores",
              description="Consulta Indicadores", include_in_schema=False)
async def get_indicadores():
    """
    Função que consulta uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    supa_cliente = ObjetoSQL()
    dados = supa_cliente.processar_query_select(tabela='indicadores')
    print(dados)
    return criar_saida(dados)


@rota_ind.post(path="/indicadores",
               responses={201: {"description": "Created", "content": ""},
                          400: {"description": "not found"}},
               tags=["Indicadores"],
               name="Inserir Indicadores",
               description="Alimentar Tabela Indicadores", include_in_schema=False)
async def post_indicadores(request: Indicadores):
    """
    Função que insere dados em uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    supa_cliente = ObjetoSQL()
    print("Request payload: ", request)
    input = json.loads(request.model_dump_json())
    indicadores = literal_eval(input['indicadores'])
    print("INPUT: ", indicadores, type(indicadores))
    nomes = []
    for i, indicador in enumerate(indicadores):
        print(i, indicador)
        supa_cliente.processar_query_insert(tabela='indicadores',
                                            dados=indicador)
        nomes.append(indicador['nome'])
    return criar_saida(message="Todos indicadores criados", content=nomes)


@rota_ind.put(path="/indicadores",
              responses={201: {"description": "Created", "content": ""},
                         400: {"description": "not found"}},
              tags=["Indicadores"],
              name="Atualizar Indicadores",
              description="Alimentar Tabela Indicadores", include_in_schema=False)
async def put_indicadores(request: Indicadores):
    """
    Função que atualiza uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    supa_cliente = ObjetoSQL()
    print("Request payload: ", request)
    input = json.loads(request.model_dump_json())
    indicadores = literal_eval(input['indicadores'])
    print("INPUT: ", indicadores, type(indicadores))
    nomes = []
    for i, indicador in enumerate(indicadores):
        print(i, indicador)
        supa_cliente.processar_query_insert(tabela='indicadores',
                                            dados=indicador)
        nomes.append(indicador['nome'])
    return criar_saida(message="Todos indicadores criados", content=nomes)


@rota_ind.delete(path="/indicadores",
                 responses={201: {"description": "Created", "content": ""},
                            400: {"description": "not found"}},
                 tags=["Indicadores"],
                 name="Deletar Indicadores",
                 description="Alimentar Tabela Indicadores", include_in_schema=False)
async def delete_indicadores(request: Indicadores):
    """
    Função que deleta uma linha em tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype:
    """
    ...
