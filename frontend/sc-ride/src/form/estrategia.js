export const est_form =
    {
            "name": "capacidade_estrategia",
            "title": "Capacidade Estratégia",
            "elements": [
                {
                    "type": "tagbox",
                    "name": "EST01",
                    "title": "EST01 - Escolha 5 opções em ordem decrescente de importância",
                    "isRequired": true,
                    "choices": [ "EST01.a", "EST01.b", "EST01.c", "EST01.d", "EST01.e", "EST01.f",
                        "EST01.g", "EST01.h", "EST01.i", "EST01.j", "EST01.k", "EST01.l",  "EST01.m"],
                    "validators": [{
                        "type": "expression",
                        "text": "A questão deve conter 5 respostas em ordem de importância",
                        "expression": "validateLength({EST01}) == 5"
                    }]
                },
                {
                    "type": "text",
                    "name": "EST01.m",
                    "title": "EST01.m - Quais outras áreas possuem importância?",
                    "visibleIf": "{EST01} contains 'EST01.m'"
                },
                {
                    "type": "tagbox",
                    "name": "EST02",
                    "title": "EST02 - Escolha 5 opções em ordem decrescente de importância",
                    "isRequired": true,
                    "choices": [ "EST02.a", "EST02.b", "EST02.c", "EST02.d", "EST02.e", "EST02.f",
                        "EST02.g", "EST02.h", "EST02.i", "EST02.j", "EST02.k", "EST02.l",  "EST02.m"],
                    "validators": [{
                        "type": "expression",
                        "text": "A questão deve conter 5 respostas em ordem de importância",
                        "expression": "validateLength({EST01}) == 5"
                    }]
                },
                {
                    "type": "text",
                    "name": "EST02.m",
                    "title": "EST02.m - Quais outras áreas possuem maior importância?",
                    "visibleIf": "{EST02} contains 'EST02.m'"
                },
                {
                    "type": "tagbox",
                    "name": "EST03",
                    "title": "EST03 - Escolha as opções",
                    "isRequired": true,
                    "choices": [ "EST03.a", "EST03.b", "EST03.c", "EST03.d", "EST03.e", "EST03.f",
                        "EST03.g", "EST03.h", "EST03.i", "EST03.j", "EST03.k"]
                },
                {
                    "type": "text",
                    "name": "EST03.j",
                    "title": "EST03.j - Qual Outro documento prevê ações de incorporação de tecnologias de informação?",
                    "visibleIf": "{EST03} contains 'EST03.j'"
                },
                {
                    "type": "tagbox",
                    "name": "EST03.1",
                    "title": "EST03.1 - Indique todos os elementos contidos no Plano Estratégico para Cidades Inteligentes de seu município",
                    "visibleIf": "{EST03} contains 'EST03.a'",
                    "choices": [ "EST03.1.a", "EST03.1.b", "EST03.1.c", "EST03.1.d", "EST03.1.e", "EST03.1.f",
                        "EST03.1.g", "EST03.1.h", "EST03.1.i", "EST03.1.j", "EST03.1.k", "EST03.1.l", "EST03.1.m"]
                },
                {
                    "type": "tagbox",
                    "name": "EST04",
                    "title": "EST04 - Quem da lista abaixo está ou esteve envolvido na elaboração de ações para uso de tecnologias de informação e comunicação na gestão municipal?",
                    "isRequired": true,
                    "choices": ["EST04.a", "EST04.b", "EST04.c", "EST04.d", "EST04.e", "EST04.f",
                        "EST04.g", "EST04.h", "EST04.i", "EST04.j", "EST04.k", "EST04.l", "EST04.m", "EST04.n", "EST04.o"]
                },
                {
                    "type": "text",
                    "name": "EST04.n",
                    "title": "EST04.n - Qual Outro está envolvido na elaboração de ações para uso de  tecnologia?",
                    "visibleIf": "{EST04} contains 'EST04.n'"
                },
                {
                    "type": "tagbox",
                    "name": "EST05",
                    "title": "EST05 - Quem é responsável pela formulação ou planejamento de ações de incorporação de tecnologias de informação e comunicação à gestão municipal?",
                    "isRequired": true,
                    "choices": [ "EST05.a", "EST05.b", "EST05.c", "EST05.d", "EST05.e", "EST05.f",
                        "EST05.g", "EST05.h", "EST05.i"]
                },
                {
                    "type": "text",
                    "name": "EST05Extra",
                    "title": "EST05Extra - Descreva os responsáveis pela formulação",
                    "visibleIf": "{EST05} notempty",
                    "description": "Para cada alternativa com opção de preenchimento acima, descreva como \"Alternativa\": \"Texto\""
                },
                {
                    "type": "tagbox",
                    "name": "EST05.1",
                    "title": "EST05.1 - Indique todos os atores envolvidos no órgão, conselho, comitê ou arranjo mencionado na questão anterior",
                    "visibleIf": "({EST05} notcontains 'EST05.g') and ({EST05} notcontains 'EST05.h')",
                    "choices": [ "EST05.1.a", "EST05.1.b", "EST05.1.c", "EST05.1.d", "EST05.1.e", "EST05.1.f",
                        "EST05.1.g", "EST05.1.h", "EST05.1.i", "EST05.1.j", "EST05.1.k", "EST05.1.l", "EST05.1.m", "EST05.1.n"]
                },
                {
                    "type": "text",
                    "name": "EST05.1Extra",
                    "title": "EST05.1Extra - Descreva os responsáveis pela formulação",
                    "visibleIf": "{EST05.1} notempty",
                    "description": "Para cada alternativa com opção de preenchimento acima, descreva como \"Alternativa\": \"Texto\""
                },
                {
                    "type": "radiogroup",
                    "name": "EST06",
                    "title": "EST06 - Em relação ao planejamento objeto da questão anterior, de incorporação de tecnologias da informação e comunicação na gestão municipal, como é feito seu acompanhamento?",
                    "isRequired": true,
                    "choices": [ "EST06.a", "EST06.b", "EST06.c", "EST06.d", "EST06.e", "EST06.f",
                        "EST06.g"],
                    "colCount": 1
                },
                {
                    "type": "tagbox",
                    "name": "EST06.1",
                    "title": "EST06.1 - Indique todos os responsáveis pelo monitoramento e/ou avaliação do processo de formulação de planos e/ou metas para incorporação de tecnologias de informação e comunicação na gestão municipal",
                    "visibleIf": "({EST06} notcontains 'EST06.g') and ({EST06} notcontains 'EST06.a')",
                    "choices": [ "EST06.1.a", "EST06.1.b", "EST06.1.c", "EST06.1.d", "EST06.1.e", "EST06.1.f",
                        "EST06.1.g", "EST06.1.h", "EST06.1.i", "EST06.1.j", "EST06.1.k", "EST06.1.l", "EST06.1.m", "EST06.1.n"]
                },
                {
                    "type": "text",
                    "name": "EST06.1Extra",
                    "title": "EST06.1Extra - Descreva os responsáveis pela formulação",
                    "visibleIf": "{EST06.1} notempty",
                    "description": "Para cada alternativa com opção de preenchimento acima, descreva como \"Alternativa\": \"Texto\""
                },
                {
                    "type": "tagbox",
                    "name": "EST07",
                    "title": "EST07 - Quem é responsável pela formulação ou planejamento de ações de incorporação de tecnologias de informação e comunicação à gestão municipal?",
                    "isRequired": true,
                    "choices": [ "EST07.a", "EST07.b", "EST07.c", "EST07.d", "EST07.e", "EST07.f",
                        "EST07.g", "EST07.h", "EST07.i"]
                },
                {
                    "type": "text",
                    "name": "EST07Extra",
                    "title": "EST07Extra - Descreva os responsáveis pela formulação",
                    "visibleIf": "{EST07} notempty",
                    "description": "Para cada alternativa com opção de preenchimento acima, descreva como \"Alternativa\": \"Texto\""
                },
                {
                    "type": "tagbox",
                    "name": "EST07.1",
                    "title": "EST07.1 - Indique todos os responsáveis pelo monitoramento e/ou avaliação do processo de formulação de planos e/ou metas para incorporação de tecnologias de informação e comunicação na gestão municipal",
                    "visibleIf": "({EST07} notcontains 'EST07.g')",
                    "choices": [ "EST07.1.a", "EST07.1.b", "EST07.1.c", "EST07.1.d", "EST07.1.e", "EST07.1.f",
                        "EST07.1.g", "EST07.1.h", "EST07.1.i", "EST07.1.j", "EST07.1.k", "EST07.1.l", "EST07.1.m", "EST07.1.n"]
                },
                {
                    "type": "text",
                    "name": "EST07.1Extra",
                    "title": "EST07.1Extra - Descreva os responsáveis pela formulação",
                    "visibleIf": "{EST07.1} notempty",
                    "description": "Para cada alternativa com opção de preenchimento acima, descreva como \"Alternativa\": \"Texto\""
                },
                {
                    "type": "radiogroup",
                    "name": "EST08",
                    "title": "EST08 - Em relação ao planejamento objeto da questão anterior, de incorporação de tecnologias da informação e comunicação na gestão municipal, como é feito seu acompanhamento?",
                    "isRequired": true,
                    "choices": [ "EST08.a", "EST08.b", "EST08.c", "EST08.d", "EST08.e", "EST08.f",
                        "EST08.g", "EST08.h", "EST08.i"],
                    "colCount": 1
                },
                {
                    "type": "text",
                    "name": "EST08Extra",
                    "title": "EST08Extra - Descreva os responsáveis pela formulação",
                    "visibleIf": "{EST08} notempty",
                    "description": "Para cada alternativa com opção de preenchimento acima, descreva como \"Alternativa\": \"Texto\""
                },
                {
                    "type": "checkbox",
                    "name": "EST09",
                    "title": "EST09 - Como são e como estão registrados visão e conceito de cidade inteligente sustentável na administração municipal?",
                    "isRequired": true,
                    "choices": [ "EST09.a", "EST09.b", "EST09.c", "EST09.d", "EST09.e"]
                }]
        }