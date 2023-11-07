export const serv_form =
    {
        "name": "capacidade_servicos",
        "title": "Capacidade: Serviços",
        "elements":
            [
                {
                    "type": "checkbox",
                        "name": "SERV01",
                        "title": "SERV01 - Indique na lista todas as áreas em que a Prefeitura oferece serviços às pessoas do município, bem como as modalidades em que são oferecidos:",
                        "colCount": 8,
                        "choices": ["SERV01.aa", "SERV01.ab", "SERV01.ac", "SERV01.ad", "SERV01.ae", "SERV01.af", "SERV01.ag", "SERV01.ah",
                            "SERV01.ba", "SERV01.bb", "SERV01.bc", "SERV01.bd", "SERV01.be", "SERV01.bf", "SERV01.bg", "SERV01.bh",
                            "SERV01.ca", "SERV01.cb", "SERV01.cc", "SERV01.cd", "SERV01.ce", "SERV01.cf", "SERV01.cg", "SERV01.ch",
                            "SERV01.da", "SERV01.db", "SERV01.dc", "SERV01.dd", "SERV01.de", "SERV01.df", "SERV01.dg", "SERV01.dh",
                            "SERV01.ea", "SERV01.eb", "SERV01.ec", "SERV01.ed", "SERV01.ee", "SERV01.ef", "SERV01.eg", "SERV01.eh",
                            "SERV01.fa", "SERV01.fb", "SERV01.fc", "SERV01.fd", "SERV01.fe", "SERV01.ff", "SERV01.fg", "SERV01.fh",
                            "SERV01.ga", "SERV01.gb", "SERV01.gc", "SERV01.gd", "SERV01.ge", "SERV01.gf", "SERV01.gg", "SERV01.gh",
                            "SERV01.ha", "SERV01.hb", "SERV01.hc", "SERV01.hd", "SERV01.he", "SERV01.hf", "SERV01.hg", "SERV01.hh",
                            "SERV01.ia", "SERV01.ib", "SERV01.ic", "SERV01.id", "SERV01.ie", "SERV01.if", "SERV01.ig", "SERV01.ih",
                            "SERV01.ja", "SERV01.jb", "SERV01.jc", "SERV01.jd", "SERV01.je", "SERV01.jf", "SERV01.jg", "SERV01.jh",
                            "SERV01.ka", "SERV01.kb", "SERV01.kc", "SERV01.kd", "SERV01.ke", "SERV01.kf", "SERV01.kg", "SERV01.kh",
                            "SERV01.la", "SERV01.lb", "SERV01.lc", "SERV01.ld", "SERV01.le", "SERV01.lf", "SERV01.lg", "SERV01.lh",
                            "SERV01.ma", "SERV01.mb", "SERV01.mc", "SERV01.md", "SERV01.me", "SERV01.mf", "SERV01.mg", "SERV01.mh"]
                },
                {
                        "type": "text",
                        "name": "SERV01.m",
                        "title": "SERV01.m - Outros",
                        "visibleIf": "{SERV01} contains 'SERV01.ma' || {SERV01} contains 'SERV01.mb' || {SERV01} contains 'SERV01.mc' || {SERV01} contains 'SERV01.md' || {SERV01} contains 'SERV01.me' || {SERV01} contains 'SERV01.mf' || {SERV01} contains 'SERV01.mg' || {SERV01} contains 'SERV01.mh'"
                },
                {
                    "type": "tagbox",
                        "name": "SERV02",
                        "title": "SERV02 - A Prefeitura oferece em seu website algum tipo de serviço que permita ao usuário:",
                        "choices": ["SERV02.a", "SERV02.b", "SERV02.c", "SERV02.d", "SERV02.e", "SERV02.f",
                            "SERV02.g", "SERV02.h", "SERV02.i", "SERV02.j", "SERV02.k", "SERV02.l", "SERV02.m",
                            "SERV02.n", "SERV02.o", "SERV02.p"]
                },
                {
                        "type": "text",
                        "name": "SERV02.n",
                        "title": "SERV02.n - Outros",
                    "visibleIf": "{SERV02} contains 'SERV02.n'"
                },
                {
                    "type": "tagbox",
                        "name": "SERV03",
                        "title": "SERV03 - Indique quais recursos foram oferecidos às pessoas do município, por meio de dispositivos móveis nos últimos 12 meses:",
                        "choices": ["SERV03.a", "SERV03.b", "SERV03.c", "SERV03.d", "SERV03.e", "SERV03.f",
                            "SERV03.g", "SERV03.h", "SERV03.i", "SERV03.j", "SERV03.k", "SERV03.l", "SERV03.m", "SERV03.n", "SERV03.o"]
                },
                {
                        "type": "text",
                        "name": "SERV03.m",
                        "title": "SERV03.m - Outros",
                    "visibleIf": "{SERV03} contains 'SERV03.m'"
                },
                {
                    "type": "tagbox",
                        "name": "SERV04",
                        "title": "SERV04 - Neste município, as pessoas podem solicitar serviços públicos por meio de:",
                        "choices": ["SERV04.a", "SERV04.b", "SERV04.c", "SERV04.d", "SERV04.e", "SERV04.f"]
                },
                {
                    "type": "radiogroup",
                    "name": "SERV05",
                    "title": "SERV05 - A prefeitura oferece formas integradas de atendimento para os moradores do município?",
                    "choices": ["SERV05.a", "SERV05.b", "SERV05.c"],
                },
                {
                    "type": "tagbox",
                    "name": "SERV05.1",
                    "title": "SERV05.1 - Se sim, por quais canais de atendimento?",
                    "choices": ["SERV05.1.a", "SERV05.1.b", "SERV05.1.c", "SERV05.1.d", "SERV05.1.e"],
                    "visibleIf": "{SERV05} == 'SERV05.a'"
                },
                {
                    "type": "text",
                        "name": "SERV05.1.e",
                        "title": "SERV05.1.e - Outros",
                    "visibleIf": "{SERV05.1} == 'SERV05.1.e'"
                },
                {
                    "type": "radiogroup",
                    "name": "SERV06",
                    "title": "SERV06 - Existem ações de gestão para oferta de serviços integrados para os moradores do município?",
                    "choices": ["SERV06.a", "SERV06.b", "SERV06.c"],
                },
                {
                    "type": "tagbox",
                    "name": "SERV06.1",
                    "title": "SERV06.1 - Se sim, quais iniciativas de gestão integrada de informações a prefeitura possui?",
                    "choices": ["SERV06.1.a", "SERV06.1.b", "SERV06.1.c", "SERV06.1.d", "SERV06.1.e", "SERV06.1.f", "SERV06.1.g"],
                    "visibleIf": "{SERV06} == 'SERV06.a'"
                },
                {
                    "type": "text",
                        "name": "SERV06.1.g",
                        "title": "SERV06.g - Outros",
                    "visibleIf": "{SERV06.1} == 'SERV06.1.g'"
                },
                {
                    "type": "radiogroup",
                    "name": "SERV07",
                    "title": "SERV07 - A gestão municipal possui planos de ampliação da oferta de serviços para os moradores do município?",
                    "choices": ["SERV07.a", "SERV07.b", "SERV07.c"],
                },
                {
                    "type": "tagbox",
                    "name": "SERV07.1",
                    "title": "SERV07.1 - Se sim:",
                    "choices": ["SERV07.1.a", "SERV07.1.b", "SERV07.1.c", "SERV07.1.d", "SERV07.1.e", "SERV07.1.f", "SERV07.1.g", "SERV07.1.h"],
                    "visibleIf": "{SERV07} == 'SERV07.a'"
                },

            ]
    }