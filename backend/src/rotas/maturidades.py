from fastapi import APIRouter
from backend.src.servicos.Componentes import *
from backend.src.servicos.Repostas import Resposta
from backend.src.servicos.Maturidade import Nivel
# from backend.src.servicos.FormUploader import FormUploader
from datetime import datetime
import pandas as pd

rota_maturidade = APIRouter()

@rota_maturidade.get(path="/maturidades",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Maturidades"],
              name="Gerar Maturidades",
              description="Gera Maturidades")
async def get_maturidades():
    """
        Função que executa o tratamento dos formulários e calcula a maturidade.
        :returns: Lista de conteúdo devolvida pela query
        :rtype:
        """

    pontuadores = {"Eplan": Eplan(), "GovCol": GovCol(),
                   "GovTec": GovTec(), "SegPol": SegPol(),
                   "Vis": Vis()}

    extrator = Resposta()
    comps = ["EST"]
    nivel = {"Estrategia": {},
             "municipio": ""}
    lista_nivel_mncps = []
    for comp in comps:
        lista_reposta_municipios = extrator.get_capacidade(comp)
        print("List municip", lista_reposta_municipios)
        for resposta_municipio in lista_reposta_municipios:
            for tag_comp, pontuador in pontuadores.items():
                nivel["Estrategia"][tag_comp] = pontuador.maturidade(resposta_municipio)
                nivel["municipio"] = resposta_municipio["municipio"]
                # lista_nivel_mncps.append(nivel)
    
    print(f"[{datetime.now()}] [RIDE] Extraído com sucesso \n", nivel)
    del extrator
    del pontuador

    # fazer_upload = False
    # if fazer_upload:
    #     df_nivel_municipio = pd.DataFrame(lista_nivel_mncps)
    #     df_nivel_municipio = df_nivel_municipio.join(pd.json_normalize(df_nivel_municipio.Estrategia)).drop('Estrategia', axis=1)
    #     df_nivel_municipio.to_csv('./backend/temp/nivel_componente_municipio.csv', index=False)
    #     form = FormUploader()
    #     form.upload_file('nivel_componente_municipio.csv', './backend/temp')
    #     print(f"[{datetime.now()}] [RIDE] Diagnóstico atualizado com sucesso \n", lista_nivel_mncps)

    calcular_capacidade = False
    if calcular_capacidade:
        # Calculo de maturidade capacidades
        for nivel_mncp in lista_nivel_mncps:
            maturidade_mncp = Nivel(nivel_mncp)
            nivel_capacidade = maturidade_mncp.definir_nivel()

        del maturidade_mncp
    return nivel