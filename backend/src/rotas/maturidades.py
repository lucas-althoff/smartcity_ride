from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from backend.src.servicos.Componentes import *
from backend.src.servicos.Repostas import Resposta
from backend.src.servicos.Maturidade import Nivel
from backend.src.servicos.FormUploader import FormUploader
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
    total_items = len(pontuadores)
    for comp in comps:
        lista_reposta_municipios = extrator.get_capacidade(comp)
        for resposta_municipio in lista_reposta_municipios:
            for index, (tag_comp, pontuador) in enumerate(pontuadores.items()):                
                nivel["Estrategia"][tag_comp] = pontuador.maturidade(resposta_municipio)
                nivel["municipio"] = resposta_municipio["municipio"]
                if index == total_items - 1:  # Atualizar lista apenas na ultima iteração
                    lista_nivel_mncps.append(nivel)
            # Reiniciando variável para próximo mncp
            nivel = {"Estrategia": {},
                     "municipio": ""}
    print(f"[{datetime.now()}] [RIDE] Extraído com sucesso \n", nivel)
    del extrator
    del pontuador

    fazer_upload = False
    if fazer_upload:
        df_nivel_municipio = pd.DataFrame(lista_nivel_mncps)
        df_nivel_municipio = df_nivel_municipio.join(pd.json_normalize(df_nivel_municipio.Estrategia)).drop('Estrategia', axis=1)
        df_nivel_municipio.to_csv('./backend/temp/nivel_componente_municipio.csv', index=False)
        form = FormUploader()
        form.upload_file('nivel_componente_municipio.csv', './backend/temp')
        print(f"[{datetime.now()}] [RIDE] Diagnóstico atualizado com sucesso \n", lista_nivel_mncps)

    calcular_capacidade = True
    if calcular_capacidade:
        # Calculo de maturidade capacidades
        for nivel_mncp in lista_nivel_mncps:
            maturidade_mncp = Nivel(nivel_mncp)
            nivel_capacidade = maturidade_mncp.definir_nivel()
        del maturidade_mncp
        print("MUNICIPIO ", nivel_capacidade)
    return lista_nivel_mncps


@rota_maturidade.get(path="/maturidades/tabela",
              responses={200: {"message": "Ok", "content": ""},
                         400: {"description": "not found"}},
              tags=["Maturidades"],
              name="Visualização das maturidades",
              description="Renderizar tabela com níveis de maturidade calculado",
              response_class=HTMLResponse)
async def render_maturidades():
    """
    Função que chama calculo da maturidade e prepara página para visualização.
    :returns: HTML contendo tabela com resultado
    :rtype:
    """
    json_data = await get_maturidades()
    ultima_atualizacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    html_content = """
    <!DOCTYPE html>
    <html>
     <style>
        body {
        margin:0;
        }

        h1 {
        font-family: 'Lato', sans-serif;
        font-weight:300;
        letter-spacing: 2px;
        font-size:48px;
        }
        p {
        font-family: 'Lato', sans-serif;
        letter-spacing: 1px;
        font-size:14px;
        color: #333333;
        }

        .header {
        position:relative;
        text-align:center;
        background: linear-gradient(60deg, rgba(84,58,183,1) 0%, rgba(0,172,193,1) 100%);
        color:white;
        }
        .logo {
        width:50px;
        fill:white;
        padding-right:15px;
        display:inline-block;
        vertical-align: middle;
        }

        .inner-header {
        height:65vh;
        width:100%;
        margin: 0;
        padding: 0;
        }

        .flex { /*Flexbox for containers*/
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        }

        .waves {
        position:relative;
        width: 100%;
        height:15vh;
        margin-bottom:-7px; /*Fix for safari gap*/
        min-height:100px;
        max-height:150px;
        }

        .content {
        position:relative;
        height:20vh;
        text-align:center;
        background-color: white;
        }

        /* Animation */

        .parallax > use {
        animation: move-forever 25s cubic-bezier(.55,.5,.45,.5)     infinite;
        }
        .parallax > use:nth-child(1) {
        animation-delay: -2s;
        animation-duration: 7s;
        }
        .parallax > use:nth-child(2) {
        animation-delay: -3s;
        animation-duration: 10s;
        }
        .parallax > use:nth-child(3) {
        animation-delay: -4s;
        animation-duration: 13s;
        }
        .parallax > use:nth-child(4) {
        animation-delay: -5s;
        animation-duration: 20s;
        }
        @keyframes move-forever {
        0% {
        transform: translate3d(-90px,0,0);
        }
        100% { 
            transform: translate3d(85px,0,0);
        }
        }
        /*Shrinking for mobile*/
        @media (max-width: 768px) {
        .waves {
            height:40px;
            min-height:40px;
        }
        .content {
            height:30vh;
        }
        h1 {
            font-size:24px;
        }
        }
            .table {
        background-color: white; /* Background color of the table */
    }

    /* Style the text within the table to make it more readable */
    .table td, .table th {
        color: black; /* Text color inside the table cells */
    }
    </style>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">

    <body>
        <div class="header"> 
                <div>
                    <svg class="waves" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                    viewBox="0 24 150 28" preserveAspectRatio="none" shape-rendering="auto">
                    <defs>
                    <path id="gentle-wave" d="M-160 44c30 0 58-18 88-18s 58 18 88 18 58-18 88-18 58 18 88 18 v44h-352z" />
                    </defs>
                    <g class="parallax">
                    <use xlink:href="#gentle-wave" x="48" y="0" fill="rgba(255,255,255,0.7" />
                    <use xlink:href="#gentle-wave" x="48" y="3" fill="rgba(255,255,255,0.5)" />
                    <use xlink:href="#gentle-wave" x="48" y="5" fill="rgba(255,255,255,0.3)" />
                    <use xlink:href="#gentle-wave" x="48" y="7" fill="#fff" />
                    </g>
                    </svg>
                    </div>
                </div>
        </div>
        <div class="container mt-5">
            <h1>Maturidade dos componentes por município</h1>
        </div>
        <div class="container mt-5">
            <table class="table table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th>Municipio</th>
                        <th>Eplan</th>
                        <th>GovCol</th>
                        <th>GovTec</th>
                        <th>SegPol</th>
                        <th>Vis</th>
                    </tr>
                </thead>
                <tbody>
    """

    for item in json_data:
        html_content += f"""
            <tr>
                <td>{item['municipio']}</td>
                <td>{item['Estrategia']['Eplan']}</td>
                <td>{item['Estrategia']['GovCol']}</td>
                <td>{item['Estrategia']['GovTec']}</td>
                <td>{item['Estrategia']['SegPol']}</td>
                <td>{item['Estrategia']['Vis']}</td>
            </tr>
        """

    html_content += f"""
                </tbody>
                </table>
                <p>Ultima atualização: {ultima_atualizacao}</p>
            </div>
                <div class="content flex">
                    <p>®Expo-RIDE 2023 - Ação 1.</p>
                </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)