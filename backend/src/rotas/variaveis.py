import json
from ast import literal_eval
from fastapi import APIRouter
from backend.src.database import ObjetoSQL
from backend.src.schemas import Variavel, SurveyData, property_name_mapping
from backend.src.utils import criar_saida
from datetime import datetime

rota_var = APIRouter()

@rota_var.post(path="/survey/validator",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Questionário"],
              name="Receber Questionário Completo",
              description="Receber questionário e valida sua estrutura")
async def survey_validator(input: dict):
    """
    Função que posta resultados do questionario na base de dados supabase
    :returns: 
    :rtype:
    """
    try:
        input = input["surveyData"]
        print(f'[SC-RIDE] [{datetime.now()}] Request payload: ', input)
        transformed_data = {property_name_mapping.get(key, key): value for key, value in input.items()}
        survey_data = SurveyData(**transformed_data)
    except Exception as e:
        print(f'[SC-RIDE] [{datetime.now()}] ERRO: ', e)
        return criar_saida(message="Erro", content=str(e))
    return criar_saida(message="Notas recebidas no servidor", content=survey_data.model_dump())

@rota_var.post(path="/survey/complete",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Questionário"],
              name="Receber Questionário Completo",
              description="Receber questionário e registra na base de dados")
async def survey_supabase(input: dict):
    res = await survey_validator(input)
    print(f'[SC-RIDE] [{datetime.now()}] Resultado validacao: ', res, type(res))
    if res['message'] == 'Erro':
        return criar_saida(message="Erro", content=str(res['content']))
    try:
        notas = res['content']
        mun = notas['municipio']
        del notas['municipio']
        dados = {
            'municipio': mun,
            'atualizacao': datetime.now().isoformat(),
            'notas': notas
        }
        print(f'[SC-RIDE] [{datetime.now()}] Dados preparados para inserção na base: ', dados)
        supa_cliente = ObjetoSQL()
        supa_cliente.processar_query_insert(tabela='survey', dados=dados)
        print(f'[SC-RIDE] [{datetime.now()}] Notas inseridas na tabela survey da base de dados')
    except Exception as e:
        print(f'[SC-RIDE] [{datetime.now()}] ERRO: ', e)
        return criar_saida(message="Erro", content=str(e))
    return criar_saida(message="Notas inseridas na tabela survey da base de dados", content=notas)

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
