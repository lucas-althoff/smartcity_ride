export const mon_form =
    {
            "name": "capacidade_monitoramento",
            "title": "Capacidade: Monitoramento",
            "elements":
                [
                        {
                                "type": "radiogroup",
                                "name": "MON01",
                                "description": "MON01 - Assinale qual alternativa representa a situação da prefeitura em relação aos seus planos de monitoramento",
                                "choices": ["MON01.a" ,"MON01.b" ,"MON01.c" ,"MON01.d" ,"MON01.e", "MON01.g"]
                        },
                        {
                                "type": "tagbox",
                                "name": "MON02",
                                "description": "MON02 - Assinale quais destas áreas de atuação da prefeitura possuem planos de monitoramento das suas metas e serviços prestados:",
                                "choices": ["MON02.a", "MON02.b", "MON02.c", "MON02.d", "MON02.e", "MON02.f", "MON02.g",
                                        "MON02.h", "MON02.i", "MON02.j", "MON02.k", "MON02.l", "MON02.m", "MON02.n"]
                        },
                        {
                                "type": "text",
                                "name": "MON02.n",
                                "title": "MON02.n - Outros",
                                "visibleIf": "{MON02} == 'MON02.n'"
                        },
                        {
                                "type": "radiogroup",
                                "name": "MON03",
                                "description": "MON03 - Assinale qual alternativa representa a situação da prefeitura em relação aos seus planos de monitoramento",
                                "choices": ["MON03.a" ,"MON03.b" ,"MON03.c" ,"MON03.d" ,"MON03.e", "MON03.g"]
                        },
                        {
                                "type": "radiogroup",
                                "name": "MON04",
                                "description": "MON04 - De que forma as informações não sigilosas contidas no monitoramento são disponibilizadas?",
                                "choices": ["MON04.a" ,"MON04.b" ,"MON04.c" ,"MON04.d"]
                        },
                        {
                                "type": "radiogroup",
                                "name": "MON05",
                                "description": "MON05 - De que forma as informações não sigilosas contidas no monitoramento são disponibilizadas?",
                                "choices": ["MON05.a" ,"MON05.b" ,"MON05.c" ,"MON05.d", "MON05.e"]
                        }
                ],
    }