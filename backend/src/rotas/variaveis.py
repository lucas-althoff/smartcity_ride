import os
import json
from ast import literal_eval
from fastapi import APIRouter
from backend.src.database import ObjetoSQL
from backend.src.schemas import Variavel
from backend.src.utils import criar_saida

rota_var = APIRouter()


@rota_var.get(path="/variaveis",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Variaveis"],
              name="Consultar dados na tabela variaveis",
              description="Consulta tabela 'variaveis' na base de dados")
async def get_variaveis():
    """
    Função que consulta uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    supa_cliente = ObjetoSQL()
    dados = supa_cliente.processar_query_select(tabela='variaveis')
    print(dados)
    return criar_saida(dados)


@rota_var.post(path="/variaveis",
               responses={201: {"description": "Created", "content": ""},
                          400: {"description": "not found"}},
               tags=["Variaveis"],
               name="Inserir dados na tabela variaveis",
               description="Atualizar linha da tabela 'variaveis' da base de dados")
async def post_variaveis(request: Variavel):
    """
    Função que renderiza a página estática home.
    :returns: Página inicial
    :rtype: fastapi.Request
    """
    supa_cliente = ObjetoSQL()
    print("Request payload: ", request)
    input = json.loads(request.model_dump_json())
    vars = literal_eval(input['id_variaveis'])
    print("INPUT: ", vars, type(vars))
    nomes = []
    for i, var in enumerate(vars):
        print(i, var)
        supa_cliente.processar_query_insert(tabela='variaveis',
                                            dados=var)
        nomes.append(var['nome'])
    return criar_saida(message="Todas variaveis criadas", content=nomes)


@rota_var.put(path="/variaveis",
              responses={201: {"description": "Created", "content": ""},
                         400: {"description": "not found"}},
              tags=["Variaveis"],
              name="Atualizar dados da tabela variaveis",
              description="Atualizar linha da tabela 'variaveis' da base de dados.")
async def put_variaveis(request: Variavel):
    """
    Função que atualiza uma tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    supa_cliente = ObjetoSQL()
    print("Request payload: ", request)
    input = json.loads(request.model_dump_json())
    vars = literal_eval(input['id_variaveis'])
    print("INPUT: ", vars, type(vars))
    nomes = []
    for i, var in enumerate(vars):
        print(i, var)
        supa_cliente.processar_query_insert(tabela='variaveis',
                                            dados=var)
        nomes.append(var['nome'])
    return criar_saida(message="Todas variaveis atualizadas", content=nomes)


@rota_var.delete(path="/variaveis",
                 responses={201: {"description": "Created", "content": ""},
                            400: {"description": "not found"}},
                 tags=["Variaveis"],
                 name="Deletar dados na tabela variaveis",
                 description="Atualizar linha da tabela 'variaveis' da base de dados")
async def delete_indicadores(request: Variavel):
    """
    Função que deleta uma linha em tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    ...
