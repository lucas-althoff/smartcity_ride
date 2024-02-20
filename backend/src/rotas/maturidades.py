from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from backend.src.servicos.Componentes import SegPol, Vis, GovCol, GovTec, EPlan
from backend.src.servicos.Componentes import IUPlan, AQua, ITPlan, Inst, HwSw, GovTI
from backend.src.servicos.Componentes import DPlan, Digi, DTransp, DInteg
from backend.src.servicos.Componentes import SPlan, SUrb, SOn, SInteg
from backend.src.servicos.Componentes import MPlan, Coord, Perc, MTransp
from backend.src.servicos.Repostas import Resposta
from backend.src.servicos.Maturidade import Nivel
from datetime import datetime, timedelta

rota_maturidade = APIRouter()


@rota_maturidade.get(path="/maturidades",
                     responses={200: {"message": "Ok", "content": ""},
                                400: {"description": "not found"}},
                     tags=["Maturidades"],
                     name="Gerar Maturidades",
                     description="Gera Maturidades",
                     include_in_schema=True)
async def get_maturidades():
    """
        Função que executa o tratamento dos formulários e calcula a maturidade.
        :returns: Lista de conteúdo devolvida pela query
        :rtype:
        """

    est = [EPlan(), GovCol(), GovTec(), SegPol(), Vis()]
    inf = [IUPlan(), AQua(), ITPlan(), Inst(), HwSw(), GovTI()]  # Completo com indices
    dad = [DPlan(), Digi(), DTransp(), DInteg()]
    serv = [SPlan(), SUrb(), SOn(), SInteg()]  # Completo com indices
    mon = [MPlan(), Coord(), Perc(), MTransp()]

    pontuadores_comps = {"EST": est,
                         "INF": inf,
                         "DAD": dad,
                         "SERV": serv,
                         "MON": mon}

    extrator = Resposta()
    resultado_mncp = {}
    for nome_cap, pontuadores in pontuadores_comps.items():  # Coletando o pontuador
        respostas_municipios = extrator.get_capacidade(nome_cap)
        pontuador_cap = Nivel(caps=[nome_cap])
        nivel = {nome_cap: {}}
        for resposta_municipio in respostas_municipios:  # Resposta por municipio por capacidade
            nivel["municipio"] = resposta_municipio["municipio"]
            print(f"[{datetime.now()}] [SC-RIDE] Cálculo Município - {resposta_municipio['municipio']}")
            print(f"###### Município - {resposta_municipio['municipio']} #######")
            for pontuador in pontuadores:
                nivel[nome_cap][pontuador.componente] = pontuador.maturidade(resposta_municipio)
            nivel_cap = pontuador_cap.definir_nivel(niveis=nivel)
            if nivel["municipio"] in resultado_mncp:
                resultado_mncp[resposta_municipio["municipio"]].append({"capacidade": nome_cap,
                                                                        "maturidade": nivel_cap,
                                                                        "componentes": nivel[nome_cap]})
            else:  # Inicializa o resultado
                resultado_mncp.update({resposta_municipio["municipio"]: [{"capacidade": nome_cap,
                                                                          "maturidade": nivel_cap,
                                                                          "componentes": nivel[nome_cap]}]})
            print(f"[{datetime.now()}] [SC-RIDE] Maturidade calculada com sucesso \n Componentes:", nivel, f"Capacidade {nome_cap}: ", nivel_cap)
            nivel = {nome_cap: {}}  # Zera o dicionario temporário a cada calculo de componente por mncps
    return resultado_mncp


@rota_maturidade.get(path="/maturidades/tabela",
                     responses={200: {"message": "Ok", "content": ""},
                                400: {"description": "not found"}},
                     tags=["Maturidades"],
                     name="Visualização das maturidades",
                     description="Renderizar tabela com níveis de maturidade calculado",
                     response_class=HTMLResponse,
                     include_in_schema=True)
async def render_maturidades2():
    json_data = await get_maturidades()
    ultima_atualizacao = datetime.now() - timedelta(hours=3)
    ultima_atualizacao = ultima_atualizacao.strftime('%Y-%m-%d %H:%M:%S')

    # Define the "capacidades" to create separate tables
    caps = ["EST", "INF", "DAD", "SERV", "MON"]

    # Extract component names dynamically from the JSON data
    componentes_by_capacidade = {cap: set() for cap in caps}
    for data in json_data.values():
        for item in data:
            cap = item["capacidade"]
            for componente in item["componentes"]:
                componentes_by_capacidade[cap].add(componente)

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
        </div>"""
    html_content += f"""
        <div class="container mt-5">
            <h1>Maturidade da Capacidade Institucional por Município</h1>
            <p>Ultima atualização: {ultima_atualizacao}</p>
        </div>
    """
    mapa_cap = {"EST": "Estratégia", "INF": "Infraestrutura", "DAD": "Dados", "SERV": "Serviços e Aplicações", "MON": "Monitoramento"}
    # Create tables for each "capacidade"
    for cap in caps:
        # Create a table header for the current "capacidade" with dynamic component names
        componentes = list(componentes_by_capacidade[cap])
        header_row = "".join([f"<th>{componente}</th>" for componente in componentes])

        html_content += f"""
        <div class="container mt-5">
            <h2>Capacidade: {mapa_cap[cap]}</h2>
            <table class="table table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th>Municipio</th>
                        {header_row}
                        <th>Maturidade</th>
                    </tr>
                </thead>
                <tbody>
        """

        for municipio, data in json_data.items():
            for item in data:
                if item["capacidade"] == cap:
                    html_content += f"<tr><td>{municipio}</td>"

                    # Add component values to the table based on available components
                    for componente in componentes:
                        html_content += f"<td>{item['componentes'].get(componente, '')}</td>"

                    # Add "maturidade" value
                    html_content += f"<td>{item['maturidade']}</td>"

                    html_content += "</tr>"
        html_content += f"""
                    </tbody>
                    </table>
                </div>"""
    html_content += f"""                
        <div class="content flex">
            <p>®Expo-RIDE 2024 - Ação 1.</p>
        </div>
    </body>
    </html>
    """

    return html_content


@rota_maturidade.get(path="/municipios/luziania",
                     responses={200: {"message": "Ok", "content": ""},
                                400: {"description": "not found"}},
                     tags=["Maturidades"],
                     name="Visualização das maturidades por municipio",
                     description="Renderizar tabela com níveis de maturidade calculado e recomendações",
                     response_class=HTMLResponse,
                     include_in_schema=True)
async def render_maturidades2():
    json_data = await get_maturidades()

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
        </div>"""
    html_content += f"""
        <div class="container mt-5">
            <h1>Luziânia (GO) Diagnóstico de Capacidade Institucional</h1>
        </div>
    """

    html_content += f"""                
        <div class="content flex">
            <p>®Expo-RIDE 2024 - Ação 1.</p>
        </div>
    </body>
    </html>
    """

    return html_content
