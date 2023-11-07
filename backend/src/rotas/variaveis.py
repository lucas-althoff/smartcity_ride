import json
from ast import literal_eval
from fastapi import APIRouter
from backend.src.database import ObjetoSQL
from backend.src.schemas import Variavel
from backend.src.utils import criar_saida

rota_var = APIRouter()

@rota_var.post(path="/survey/complete",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Questionário"],
              name="Receber Questionário Completo",
              description="Receber questionário e registra na base de dados")
async def survey_complete(input):
    """
    Função que posta resultados do questionario na base de dados supabase
    :returns: 
    :rtype:
    """
    print("Request payload: ", input)
    input_json = json.loads(input.model_dump_json())
    print("LODADED INPUT: ", input_json, type(input_json))
    notas = literal_eval(input_json)
    print("INPUT: ", notas, type(notas))
    # supa_cliente = ObjetoSQL()
    # nomes = []
    # for i, var in enumerate(notas):
    #     print(i, var)
    #     supa_cliente.processar_query_insert(tabela='variaveis',
    #                                         dados=var)
    #     nomes.append(var['nome'])
    return criar_saida(message="Notas recebidas no servidor", content=notas)


@rota_var.get(path="/variaveis",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Variaveis"],
              name="Consultar dados na tabela variaveis",
              description="Consulta tabela 'variaveis' na base de dados", include_in_schema=False)
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
               description="Atualizar linha da tabela 'variaveis' da base de dados", include_in_schema=False)
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
              description="Atualizar linha da tabela 'variaveis' da base de dados.", include_in_schema=False)
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
                 description="Atualizar linha da tabela 'variaveis' da base de dados", include_in_schema=False)
async def delete_indicadores(request: Variavel):
    """
    Função que deleta uma linha em tabela no Supabase.
    :returns: Lista de conteúdo devolvida pela query
    :rtype: 
    """
    ...
