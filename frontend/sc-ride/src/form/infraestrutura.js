export const inf_form =
    {
        "name": "capacidade_infraestrutura",
        "title": "Capacidade: Infraestrutura",
        "elements":
        [
            {
                "type": "text",
                "name": "INF4005",
                "description": "INF4005 - Índice para cálculo de IUPlan: Percentual de pavimentação das vias públicas"
             },
            {
                "type": "radiogroup",
                "name": "INF4031",
                "description": "INF4031 - Índice para cálculo de IUPlan: Existem Ações de acessibilidade no transporte público do município",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "radiogroup",
                "name": "INF4041",
                "description": "INF4041 - Índice para cálculo de IUPlan: Existem ações para políticas habitacionais do município",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "radiogroup",
                "name": "INF4046",
                "description": "INF4046 - Índice para cálculo de IUPlan: Presença de ações de fomento a ciclo-mobilidade na cidade",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "radiogroup",
                "name": "INF3122",
                "description": "INF3122 - Índice para cálculo de IUPlan: Presença de coleta seletiva de resíduos nos municípios",
                "choices": ["Sim", "Nao"]
            },
            {
                "type": "text",
                "name": "INF3027",
                "description": "INF3027 - Indice para calculo do AQua: Percentual da população coberta com coleta de resíduos (lixo orgânico e reciclável sem separação ou com separação)"
            },
            {
                "type": "text",
                "name": "INF3077",
                "description": "INF3077 - Índíce para cálculo do AQua: Número de equipamentos culturais disponíveis no município"
            },
            {
                "type": "text",
                "name": "INF3110",
                "description": "INF3110 - Índíce para cálculo do AQua: Índice de perdas de água na distribuição"
            },
            {
                "type": "text",
                "name": "INF3117",
                "description": "INF3117 - Índice para cálculo do AQua: População do muncípio atendida com abastecimento de água tratada"
            },
            {
                "type": "text",
                "name": "INF3124",
                "description": "INF3124 - Índice para cálculo do AQua: População do muncípio atendida com abastecimento de água tratada"
            },
            {
                "type": "text",
                "name": "INF3127",
                "description": "INF3127 - Índice para cálculo do AQua: Percentual da população residente em domicílios permanentes com esgotamento sanitário por rede geral e fossa séptica"
            },
            {
                "type": "radiogroup",
                "name": "INF01",
                "description": "INF01 - A prefeitura possui departamento, setor ou área responsável pela infraestrutura de TI no município?",
                "choices": ["INF01.a", "INF01.b", "INF01.c"]
            },
            {
                "type": "radiogroup",
                "name": "INF01.1",
                "description": "INF01.1 - A prefeitura possui departamento, setor ou área responsável pela infraestrutura de TI no município?",
                "visibleIf": "{INF01} != 'INF01.a'",
                "choices": ["INF01.1.a", "INF01.1.b", "INF01.1.c"]
            },
            {
                "type": "radiogroup",
                "name": "INF01.2",
                "description": "INF01.2 - A prefeitura possui departamento, setor ou área responsável pela infraestrutura de TI no município?",
                "visibleIf": "{INF01} == 'INF01.a'",
                "choices": ["INF01.1.a", "INF01.1.b", "INF01.1.c"]
            },
            {
                "type": "tagbox",
                "name": "INF01.3",
                "description": "INF01.3 - Informe o vínculo empregatício dos funcionários",
                "choices": ["INF01.3.a", "INF01.3.b", "INF01.3.c", "INF01.3.c"]
            },
            {
                "type": "radiogroup",
                "name": "INF01.4",
                "description": "INF01.4 - Indique quais práticas de governança de TI são adotadas na prefeitura. Escolha apenas uma alternativa.",
                "choices": ["INF01.4.a" ,"INF01.4.b" ,"INF01.4.c" ,"INF01.4.d" ,"INF01.4.e"]
            },
            {
                "type": "checkbox",
                "name": "INF02",
                "title": "INF02 - Considerando as seis funções de TI da administração municipal listadas abaixo, assinale quem é o responsável principal por desempenhar cada uma delas.",
                "colCount": 3,
                "choices": ["INF02.aa", "INF02.ab", "INF02.ac", "INF02.ba", "INF02.bb", "INF02.bc",
                "INF02.ca", "INF02.cb", "INF02.cc", "INF02.da", "INF02.db", "INF02.dc", "INF02.ea",
                "INF02.eb", "INF02.ec", "INF02.fa", "INF02.fb", "INF02.fc"]
            },
            {
                "type": "tagbox",
                "name": "INF03",
                "description": "INF03 - Quais são os sistemas de informação disponíveis na prefeitura?",
                "choices": ["INF03.a" ,"INF03.b" ,"INF03.c" ,"INF03.d" ,"INF03.e" ,"INF03.f"
                    ,"INF03.g" ,"INF03.h" ,"INF03.i" ,"INF03.j" ,"INF03.k" ,"INF03.l" ,"INF03.m"]
            },
            {
                "type": "text",
                "name": "INF03.l",
                "description": "INF03.l - Qual outro sistema de informação disponível na prefeitura?"
            },
            {
                "type": "tagbox",
                "name": "INF04",
                "description": "INF04 - Onde ficam armazenados os dados e sistemas da prefeitura?",
                "choices": ["INF04.a" ,"INF04.b" ,"INF04.c" ,
                    "INF04.d" ,"INF04.e" ,"INF04.f" ,"INF04.g" ,"INF04.h"]
            },
            {
                "type": "tagbox",
                "name": "INF04.1",
                "description": "INF04.1 - Se existe armazenamento de dados em nuvem, indique:",
                "choices": ["INF04.a" ,"INF04.b" ,"INF04.c" , "INF04.d"],
                "visibleIf": "{INF04} contains 'INF04.b'"
            },
            {
                "type": "radiogroup",
                "name": "INF05",
                "description": "INF05 - A prefeitura possui um Plano Diretor de tecnologia da Informação (PDTI) ou Plano estratégico de TI já implementado?",
                "choices": ["INF05.a", "INF05.b"]
            },
            {
                "type": "radiogroup",
                "name": "INF05.1",
                "description": "INF05.1 - A prefeitura ainda não elaborou um plano, mas indique se realizou alguma das atividades:",
                "choices": ["INF05.1.a", "INF05.1.b"],
                "visibleIf": "{INF05} == 'INF05.b'"
            },
            {
                "type": "radiogroup",
                "name": "INF05.2",
                "description": "INF05.2 - A prefeitura já realizou pelo menos uma das ações previstas no documento formalmente constituído de planejamento de TI?",
                "choices": ["INF05.2.a", "INF05.2.b"]
            },
            {
                "type": "radiogroup",
                "name": "INF05.3",
                "description": "INF05.3 - A prefeitura monitora periodicamente o documento formalmente instituído de planejamento de Tecnologia da Informação?",
                "choices": ["INF05.3.a", "INF05.3.b"]
            },
            {
                "type": "radiogroup",
                "name": "INF05.4",
                "description": "INF05.4 - A prefeitura faz planejamento para o uso de tecnologias avançadas? Dos tipos: IOT, IA, Machine learning, Big Data?",
                "choices": ["INF05.4.a", "INF05.4.b"]
            },
            {
                "type": "radiogroup",
                "name": "INF05.5",
                "description": "INF05.5 - O planejamento contempla a participação de outros atores no mercado de oferta de soluções tecnológicas?",
                "choices": ["INF05.5.a", "INF05.5.b"],
                "visibleIf": "{INF05} == 'INF05.a'"
            },
        ]
    }