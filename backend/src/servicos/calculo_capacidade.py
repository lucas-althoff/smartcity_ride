from Componentes import *
from Repostas import Resposta
from datetime import datetime
from Maturidade import Nivel
from FormUploader import FormUploader
import pandas as pd

if __name__ == "__main__":
    nivel_capacidade = {"Estrategia": 1,
                        "Infraestrutura": 1,
                        "Dados": 1,
                        "ServicosApp": 1,
                        "Monitoramento": 1,
                        "municipio": ""}

    nivel_componente = {"Estrategia": {"Eplan": 1,
                                       "GovCol": 0,
                                       "GovTec": 1,
                                       "SegPol": 1,
                                       "Vis": 0},
                        "Infraestrutura": {"IUPlan": 0,
                                           "AQua": 1,
                                           "ITPlan": 0,
                                           "Inst": 0,
                                           "HwSw": 1,
                                           "GovTI": 0},
                        "Dados": {"DPlan": 1,
                                  "Digi": 1,
                                  "DTransp": 1,
                                  "DInteg": 0},
                        "ServicosApp": {"SPlan": 1,
                                        "SUrb": 1,
                                        "SOn": 1,
                                        "SInteg": 0},
                        "Monitoramento": {"MPlan": 1,
                                          "Coord": 0,
                                          "Perc": 0,
                                          "MTransp": 0, },
                        "municipio": ""}

    # respostas_estrategia = {
    #     "municipio": "Cacaozinho", ## INCLUIDO
    #     # Lista tamanho max 5 com campo aberto
    #     "EST01": ["EST01.b", "EST01.d", "EST01.a", "EST01.l", "EST01.m:Idosos"],
    #     # Lista tamanho max 5 com campo aberto
    #     "EST02": ["EST02.c", "EST02.e", "EST02.b", "EST02.l", "EST02.m:Idosos"],
    #     # Lista aberta com campo aberto
    #     "EST03": ["EST03.c", "EST03.a", "EST03.d"],
    #     # Lista aberta
    #     "EST03.1": ["EST03.1.c", "EST03.1.j", "EST03.1.k"],
    #     # Lista aberta com campo aberto
    #     "EST04": ["EST04.b", "EST04.c", "EST04.f"],
    #     # Lista aberta com campo aberto
    #     "EST05": ["EST05.a", "EST05.e", "EST05.g"],
    #     # Lista aberta com campo aberto
    #     "EST05.1": ["EST05.1.a:Elisa", "EST05.1.e:Maria", "EST05.1.g:Marcia"],
    #     "EST06": ["EST06.d"],  # Múltipla escolha ## MODIFICADO
    #     # Lista aberta com campo aberto
    #     "EST06.1": ["EST06.1.a:Elisa", "EST06.1.b:Jesus", "EST06.1.c:Edison"],
    #     # Lista aberta com campo aberto
    #     "EST07": ["EST07.a:Roney", "EST07.c:Erica", "EST07.h:Marcia"],
    #     # Lista aberta com campo aberto
    #     "EST07.1": ["EST07.1.a:Luiz", "EST07.1.b:Waleska", "EST07.1.h:Daniela"],
    #     # Múltipla escolha com campo aberto
    #     "EST08": ["EST08.f:Ana Luisa"],  ## MODIFICADO
    #     # Múltipla escolha
    #     "EST09": ["EST09.a"]} ## MODIFICADO

    # respostas_infraestrutura = None
    # respostas_dados = None
    # respostas_servicosApp = None
    # respostas_monitoramento = None

    # respostas = {"nota_global": {"Estrategia": respostas_estrategia,
    #                              "Infraestrutura": respostas_infraestrutura,
    #                              "Dados": respostas_dados,
    #                              "ServicosApp": respostas_servicosApp,
    #                              "Monitoramento": respostas_monitoramento}}


    pontuadores = {"Eplan": Eplan(), "GovCol": GovCol(),
                   "GovTec": GovTec(), "SegPol": SegPol(),
                   "Vis": Vis()}

    #TODO: Filtrar pelo último dado do municipio, atualmente ele puxa todas linhas
    extrator = Resposta()

    # Calculo de maturidade componentes
    # comps = ["EST", "INF", "DAD", "SERV", "MON"]
    comps = ["EST"]
    nivel = {"Estrategia": {},
             "municipio": ""}
    lista_nivel_mncps = []
    for comp in comps:
        lista_reposta_municipios = extrator.get_capacidade(comp)
        for resposta_municipio in lista_reposta_municipios:
            for tag_comp, pontuador in pontuadores.items():
                nivel["Estrategia"][tag_comp] = pontuador.verificador(resposta_municipio, nome_comp=tag_comp)
                nivel["municipio"] = resposta_municipio["municipio"]
                lista_nivel_mncps.append(nivel)

    print(f"[{datetime.now()}] [RIDE] Extraído com sucesso \n", lista_nivel_mncps)
    #TODO: Fazer insert na tabela indicador_municipio
    #TODO: Fazer o select do nivel de maturidade do municipio
    #TODO: Converter JSON e jogar dados na tabela
    del extrator
    del pontuador

    df_nivel_municipio = pd.DataFrame(lista_nivel_mncps)
    df_nivel_municipio = df_nivel_municipio.join(pd.json_normalize(df_nivel_municipio.Estrategia)).drop('Estrategia', axis=1)
    df_nivel_municipio.to_csv('./backend/temp/nivel_componente_municipio.csv', index=False)
    form = FormUploader()
    form.upload_file('nivel_componente_municipio.csv', './backend/temp')
    calcular_capacidade = False

    if calcular_capacidade:
        # Calculo de maturidade capacidades
        for nivel_mncp in lista_nivel_mncps:
            maturidade_mncp = Nivel(nivel_mncp)
            nivel_capacidade = maturidade_mncp.definir_nivel()

        del maturidade_mncp