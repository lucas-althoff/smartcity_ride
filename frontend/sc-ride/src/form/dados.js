export const inf_form =
    {
        "name": "capacidade_dados",
        "title": "Capacidade: Dados",
        "elements":
            [
                {
                        "type": "checkbox",
                        "name": "DAD01",
                        "title": "DAD01 - Em relação as seguintes áreas de atuação da prefeitura, assinale qual a forma de coleta e armazenamento de dados utilizada:",
                        "colCount": 3,
                        "choices": ["DAD01.aa", "DAD01.ab", "DAD01.ac", "DAD01.ba", "DAD01.bb", "DAD01.bc",
                        "DAD01.ca", "DAD01.cb", "DAD01.cc", "DAD01.da", "DAD01.db", "DAD01.dc", "DAD01.ea",
                        "DAD01.eb", "DAD01.ec", "DAD01.fa", "DAD01.fb", "DAD01.fc", "DAD01.ga", "DAD01.gb",
                        "DAD01.gc", "DAD01.ha", "DAD01.hb", "DAD01.hc", "DAD01.ia", "DAD01.ib", "DAD01.ic",
                        "DAD01.ja", "DAD01.jb", "DAD01.jc", "DAD01.ka", "DAD01.kb", "DAD01.kc", "DAD01.la",
                        "DAD01.lb", "DAD01.lc", "DAD01.ma", "DAD01.mb", "DAD01.mc"]
                },
                {
                        "type": "text",
                        "name": "DAD01.m",
                        "title": "DAD01.m - Outros"
                },
                {
                        "type": "radiogroup",
                        "name": "DAD02",
                        "title": "DAD02 - Assinale a alternativa que mais representa o estágio atual do município em relação à integração e interoperabilidade das bases de dados.",
                        "choices": ["DAD02.a", "DAD02.b", "DAD02.c", "DAD02.d", "DAD02.e"]
                },
                {
                        "type": "radiogroup",
                        "name": "DAD03",
                        "title": "DAD03 - Assinale a alternativa que mais representa o estágio do município em termos de planejamento do uso de dados:",
                        "choices": ["DAD03.a", "DAD03.b", "DAD03.c", "DAD03.d", "DAD03.e", "DAD03.f", "DAD03.g"]
                },
                {
                        "type": "tagbox",
                        "name": "DAD04",
                        "title": "DAD04 - Quais das seguintes práticas de segurança da informação são utilizadas na prefeitura atualmente?",
                        "choices": ["DAD04.a", "DAD04.b", "DAD04.c", "DAD04.d", "DAD04.e", "DAD04.f", "DAD04.g", "DAD04.h", "DAD04.i"]
                },
                {
                        "type": "radiogroup",
                        "name": "DAD05",
                        "title": "DAD05 - No que tange a Lei de Acesso à Informação, em qual situação o município se encontra?",
                        "choices": ["DAD05.a", "DAD05.b", "DAD05.c", "DAD05.d"]
                },
                {
                        "type": "radiogroup",
                        "name": "DAD06",
                        "title": "DAD06 - O município disponibiliza em uma página na internet informações sobre execução orçamentária e financeira?",
                        "choices": ["DAD06.a", "DAD06.b", "DAD06.c", "DAD06.d"]
                },
                {
                        "type": "radiogroup",
                        "name": "DAD07",
                        "title": "DAD07 - As informações disponibilizadas em uma página na internet são publicadas em dados abertos?",
                        "choices": ["DAD07.a", "DAD07.b", "DAD07.c", "DAD07.d", "DAD07.e"]
                },
                {
                        "type": "radiogroup",
                        "name": "DAD08",
                        "title": "DAD08 - Houve análises de Big Data nos últimos 12 meses?",
                        "choices": ["DAD08.a", "DAD08.b", "DAD08.c"]
                },
                {
                        "type": "tagbox",
                        "name": "DAD09",
                        "title": "DAD09 - Quais as fontes utilizadas para essas análises? Assinalar múltiplas opções, se for o caso.",
                        "choices": ["DAD09.a", "DAD09.b", "DAD09.c", "DAD09.d", "DAD09.e"],
                        "visibleIf": "{DAD08} == 'DAD08.a'"
                },
            ]
    }