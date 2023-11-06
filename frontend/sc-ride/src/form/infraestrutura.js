export const inf_form =
    {
        "name": "capacidade_infraestrutura",
        "title": "Capacidade: Infraestrutura",
        "elements":
        [
            {
                "type": "text",
                "name": "INF4005",
                "description": "Índice para cálculo de IUPlan: Percentual de pavimentação das vias públicas"
             },
            {
                "type": "radiogroup",
                "name": "INF4031",
                "description": "Índice para cálculo de IUPlan: Existem Ações de acessibilidade no transporte público do município",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "radiogroup",
                "name": "INF4041",
                "description": "Índice para cálculo de IUPlan: Existem ações para políticas habitacionais do município",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "radiogroup",
                "name": "INF4046",
                "description": "Índice para cálculo de IUPlan: Presença de ações de fomento a ciclo-mobilidade na cidade",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "radiogroup",
                "name": "INF3122",
                "description": "Índice para cálculo de IUPlan: Presença de coleta seletiva de resíduos nos municípios",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "text",
                "name": "INF3027",
                "description": "Indice para calculo do AQua: Percentual da população coberta com coleta de resíduos (lixo orgânico e reciclável sem separação ou com separação)"
            },
            {
                "type": "text",
                "name": "INF3077",
                "description": "Índíce para cálculo do AQua: Número de equipamentos culturais disponíveis no município"
            },
            {
                "type": "text",
                "name": "INF3110",
                "description": "Índíce para cálculo do AQua: Índice de perdas de água na distribuição"
            },
            {
                "type": "text",
                "name": "INF3117",
                "description": "Índice para cálculo do AQua: População do muncípio atendida com abastecimento de água tratada"
            },
            {
                "type": "text",
                "name": "INF3124",
                "description": "Índice para cálculo do AQua: População do muncípio atendida com abastecimento de água tratada"
            },
            {
                "type": "text",
                "name": "INF3127",
                "description": "Índice para cálculo do AQua: Percentual da população residente em domicílios permanentes com esgotamento sanitário por rede geral e fossa séptica"
            },
            {
                "type": "radiogroup",
                "name": "INF01",
                "description": "A prefeitura possui departamento, setor ou área responsável pela infraestrutura de TI no município?",
                "choices": ["INF01.a", "INF01.b", "INF01.c"]
            },
            {
                "type": "radiogroup",
                "name": "INF01.1",
                "description": "A prefeitura possui departamento, setor ou área responsável pela infraestrutura de TI no município?",
                "visibleIf": "{INF01} != 'INF01.a'",
                "choices": ["INF01.1.a", "INF01.1.b", "INF01.1.c"]
            },
            {
                "type": "radiogroup",
                "name": "INF01.2",
                "description": "A prefeitura possui departamento, setor ou área responsável pela infraestrutura de TI no município?",
                "visibleIf": "{INF01} == 'INF01.a'",
                "choices": ["INF01.1.a", "INF01.1.b", "INF01.1.c"]
            },
            {
                "type": "tagbox",
                "name": "INF01.3",
                "description": "Informe o vínculo empregatício dos funcionários",
                "choices": ["INF01.3.a", "INF01.3.b", "INF01.3.c", "INF01.3.c"]
            },
            {
                "type": "radiogroup",
                "name": "INF01.4",
                "description": "Indique quais práticas de governança de TI são adotadas na prefeitura. Escolha apenas uma alternativa.",
                "choices": ["INF01.4.a" ,"INF01.4.b" ,"INF01.4.c" ,"INF01.4.d" ,"INF01.4.e"]
            },

        ]
    }