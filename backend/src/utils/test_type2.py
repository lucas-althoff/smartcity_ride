
property_name_mapping = {
    'EST01': 'EST01',
    'EST02': 'EST02',
    'EST03': 'EST03',
    'EST04': 'EST04',
    'EST05': 'EST05',
    'EST05.1': 'EST051',
    'EST06': 'EST06',
    'EST06.1': 'EST061',
    'EST07': 'EST07',
    'EST07.1': 'EST071',
    'EST08': 'EST08',
    'EST09': 'EST09',
    'INF4005': 'INF4005',
    'INF4031': 'INF4031',
    'INF4041': 'INF4041',
    'INF4046': 'INF4046',
    'INF3122': 'INF3122',
    'INF3027': 'INF3027',
    'INF3077': 'INF3077',
    'INF3110': 'INF3110',
    'INF3117': 'INF3117',
    'INF3124': 'INF3124',
    'INF3127': 'INF3127',
    'INF01': 'INF01',
    'INF011': 'INF011',
    'INF012': 'INF012',
    'INF013': 'INF013',
    'INF014': 'INF014',
    'INF02': 'INF02',
    'INF03': 'INF03',
    'INF031': 'INF031',
    'INF04': 'INF04',
    'INF041': 'INF041',
    'INF05': 'INF05',
    'INF051': 'INF051',
    'INF052': 'INF052',
    'INF053': 'INF053',
    'INF054': 'INF054',
    'DAD01': 'DAD01',
    'DAD02': 'DAD02',
    'DAD03': 'DAD03',
    'DAD04': 'DAD04',
    'DAD05': 'DAD05',
    'DAD05.1': 'DAD05',
    'DAD06': 'DAD06',
    'DAD07': 'DAD07',
    'DAD08': 'DAD08',
    'DAD09': 'DAD09',
    'SERV01': 'SERV01',
    'SERV03': 'SERV03',
    'SERV04': 'SERV04',
    'SERV05': 'SERV05',
    'SERV051': 'SERV051',
    'SERV06': 'SERV06',
    'SERV061': 'SERV061',
    'SERV07': 'SERV07',
    'SERV071': 'SERV071',
    'MON01': 'MON01',
    'MON02': 'MON02',
    'MON03': 'MON03',
    'MON04': 'MON04',
    'MON05': 'MON05'
}


from pydantic import BaseModel
from typing import List, Dict, Optional


class Resposta(BaseModel):
    message: str
    content: Optional[dict]


class Indicador(BaseModel):
    id: int
    nome: str
    dimensao: str
    topico: str


class Indicadores(BaseModel):
    indicadores: str


class Variavel(BaseModel):
    id_variavel: str
    municipio: str
    nome: str


class PlatformData(BaseModel):
    platform: str
    values: List[str]


class SurveyData(BaseModel):
    municipio: Optional[str]
    EST01: Optional[List[str]] = None
    EST02: Optional[List[str]] = None
    EST03: Optional[List[str]] = None
    EST04: Optional[List[str]] = None
    EST05: Optional[List[str]] = None
    EST051: Optional[List[str]] = None
    EST06: Optional[str] = None
    EST061: Optional[List[str]] = None
    EST07: Optional[List[str]] = None
    EST071: Optional[List[str]] = None
    EST08: Optional[str] = None
    EST09: Optional[List[str]] = None
    INF4005: Optional[str] = None
    INF4031: Optional[str] = None
    INF4041: Optional[str] = None
    INF4046: Optional[str] = None
    INF3122: Optional[str] = None
    INF3027: Optional[str] = None
    INF3077: Optional[str] = None
    INF3110: Optional[str] = None
    INF3117: Optional[str] = None
    INF3124: Optional[str] = None
    INF3127: Optional[str] = None
    INF01: Optional[str] = None
    INF011: Optional[str] = None
    INF012: Optional[str] = None
    INF013: Optional[List[str]] = None
    INF014: Optional[str] = None
    INF02: Optional[Dict[str, str]] = None
    INF03: Optional[List[str]] = None
    INF031: Optional[str] = None
    INF04: Optional[List[str]] = None
    INF041: Optional[List[str]] = None
    INF05: Optional[str] = None
    INF051: Optional[str] = None
    INF052: Optional[str] = None
    INF053: Optional[str] = None
    INF054: Optional[str] = None
    DAD01: Optional[Dict[str, str]] = None
    DAD02: Optional[str] = None
    DAD03: Optional[str] = None
    DAD04: Optional[List[str]] = None
    DAD05: Optional[str] = None
    DAD051: Optional[str] = None
    DAD06: Optional[str] = None
    DAD07: Optional[str] = None
    DAD08: Optional[str] = None
    DAD09: Optional[List[str]] = None
    # SERV01: Optional[Dict[str, PlatformData]] = None
    SERV01: Optional[Dict[str, Dict[str, List[str]]]] = None
    SERV03: Optional[List[str]] = None
    SERV04: Optional[List[str]] = None
    SERV05: Optional[str] = None
    SERV051: Optional[List[str]] = None
    SERV06: Optional[str] = None
    SERV061: Optional[str] = None
    SERV07: Optional[str] = None
    SERV071: Optional[str] = None
    MON01: Optional[str] = None
    MON02: Optional[List[str]] = None
    MON03: Optional[str] = None
    MON04: Optional[str] = None
    MON05: Optional[str] = None

input_data = {
   "municipio": "Água Fria de Goiás (GO)",
   "EST06": "EST06.f",
   "EST08": "EST08.g",
   "EST09": [
      "EST09.c"
   ],
   "EST01": [
      "EST01.b",
      "EST01.e",
      "EST01.g",
      "EST01.j",
      "EST01.i"
   ],
   "INF4031": "Sim",
   "INF05.4": "INF05.4.a",
   "INF05": "INF05.a",
   "INF05.5": "INF05.5.a",
   "INF02": {
      "INF02.a": "a",
      "INF02.b": "a",
      "INF02.c": "a",
      "INF02.d": "a",
      "INF02.e": "a",
      "INF02.f": "a"
   },
   "DAD01": {
      "DAD01.a": "a",
      "DAD01.b": "a",
      "DAD01.c": "a",
      "DAD01.d": "a",
      "DAD01.e": "b",
      "DAD01.f": "b",
      "DAD01.g": "b",
      "DAD01.h": "b",
      "DAD01.i": "b",
      "DAD01.j": "b",
      "DAD01.k": "a",
      "DAD01.l": "a"
   },
   "SERV07": "SERV07.d",
   "MON05": "MON05.c",
   "SERV01": {
      "SERV01.l": {
         "Plataforma integrada": [
            "b"
         ]
      },
      "SERV01.a": {
         "Multicanais": [
            "c"
         ]
      },
      "SERV01.b": {
         "Plataforma integrada": [
            "b"
         ]
      },
      "SERV01.c": {
         "Transacional": [
            "d"
         ]
      },
      "SERV01.d": {
         "Multicanais": [
            "c"
         ]
      },
      "SERV01.e": {
         "Transacional": [
            "d"
         ]
      },
      "SERV01.f": {
         "Informacional": [
            "e"
         ]
      },
      "SERV01.g": {
         "Não Digitalizado - digitalização planejada": [
            "f"
         ]
      },
      "SERV01.h": {
         "Informacional": [
            "e"
         ]
      },
      "SERV01.i": {
         "Não Digitalizado - digitalização planejada": [
            "f"
         ]
      },
      "SERV01.j": {
         "Informacional": [
            "e"
         ]
      },
      "SERV01.k": {
         "Não Digitalizado - digitalização planejada": [
            "f"
         ]
      }
   }
}

test_planaltina = {"municipio":"Planaltina (GO)","EST01":["EST01.d","EST01.c","EST01.e","EST01.i","EST01.a"],"EST02":["EST02.i","EST02.d","EST02.e","EST02.a","EST02.j"],"EST03":["EST03.a"],"EST04":["EST04.a","EST04.m"],"EST05":["EST05.a","EST05.e"],"EST051":["EST05.1.a","EST05.1.l"],"EST06":"EST06.a","EST07":["EST07.g"],"EST08":"EST08.g","EST09":["EST09.d"],"INF4005":"24,55 km² IBGE","INF4031":"Nao","INF4041":"Nao","INF4046":"Nao","INF3122":"Sim","INF3027":"98,53% aguasesaneamento.org.br","INF3077":"2","INF3110":"38,71% aguasesaneamento.org.br","INF3117":"95,71% aguasesaneamento.org.br","INF3124":"0","INF3127":"94,39% aguasesaneamento.org.br","INF01":"INF01.b","INF02":{"INF02.a":"a","INF02.b":"a","INF02.c":"c","INF02.d":"c","INF02.e":"c","INF02.f":"c"},"INF03":["INF03.a","INF03.c","INF03.d","INF03.e","INF03.f","INF03.g","INF03.h"],"INF04":["INF04.b","INF04.g"],"INF05":"INF05.b","DAD01":{"DAD01.a":"b","DAD01.b":"c","DAD01.c":"c","DAD01.d":"a","DAD01.e":"b","DAD01.f":"c","DAD01.g":"c","DAD01.h":"c","DAD01.i":"b","DAD01.j":"b","DAD01.k":"c","DAD01.l":"a"},"DAD02":"DAD02.e","DAD03":"DAD03.g","DAD04":["DAD04.e"],"DAD05":"DAD05.b","DAD06":"DAD06.a","DAD07":"DAD07.a","DAD08":"DAD08.b","SERV01":{"SERV01.a":{"Multicanais":["c"]},"SERV01.b":{"Informacional":["e"]},"SERV01.c":{"Não sabe":["h"]},"SERV01.d":{"Informacional":["e"]},"SERV01.e":{"Não sabe":["h"]},"SERV01.f":{"Informacional":["e"]},"SERV01.g":{"Não sabe":["h"]},"SERV01.h":{"Não sabe":["h"]},"SERV01.i":{"Transacional":["d"]},"SERV01.j":{"Multicanais":["c"]},"SERV01.k":{"Não sabe":["h"]},"SERV01.l":{"Não sabe":["h"]}},"SERV03":["SERV03.i","SERV03.j"],"SERV04":["SERV04.a","SERV04.b","SERV04.c","SERV04.e"],"SERV05":"SERV05.b","SERV06":"SERV06.b","SERV07":"SERV07.c","MON01":"MON01.a","MON02":["MON02.m"],"MON03":"MON03.b","MON04":"MON04.e","MON05":"MON05.a"}


test_planaltina2 = {
    "municipio": "Planaltina (GO)",
    "EST01": [
      "EST01.d",
      "EST01.c",
      "EST01.e",
      "EST01.i",
      "EST01.a"
    ],
    "EST02": [
      "EST02.i",
      "EST02.d",
      "EST02.e",
      "EST02.a",
      "EST02.j"
    ],
    "EST03": [
      "EST03.a"
    ],
    "EST04": [
      "EST04.a",
      "EST04.m"
    ],
    "EST05": [
      "EST05.a",
      "EST05.e"
    ],
    "EST051": [
      "EST05.1.a",
      "EST05.1.l"
    ],
    "EST06": "EST06.a",
    "EST061": None,
    "EST07": [
      "EST07.g"
    ],
    "EST071": None,
    "EST08": "EST08.g",
    "EST09": [
      "EST09.d"
    ],
    "INF4005": "24,55 km² IBGE",
    "INF4031": "Nao",
    "INF4041": "Nao",
    "INF4046": "Nao",
    "INF3122": "Sim",
    "INF3027": "98,53% aguasesaneamento.org.br",
    "INF3077": "2",
    "INF3110": "38,71% aguasesaneamento.org.br",
    "INF3117": "95,71% aguasesaneamento.org.br",
    "INF3124": "0",
    "INF3127": "94,39% aguasesaneamento.org.br",
    "INF01": "INF01.b",
    "INF011": None,
    "INF012": None,
    "INF013": None,
    "INF014": None,
    "INF02": {
      "INF02.a": "a",
      "INF02.b": "a",
      "INF02.c": "c",
      "INF02.d": "c",
      "INF02.e": "c",
      "INF02.f": "c"
    },
    "INF03": [
      "INF03.a",
      "INF03.c",
      "INF03.d",
      "INF03.e",
      "INF03.f",
      "INF03.g",
      "INF03.h"
    ],
    "INF031": None,
    "INF04": [
      "INF04.b",
      "INF04.g"
    ],
    "INF041": None,
    "INF05": "INF05.b",
    "INF051": None,
    "INF052": None,
    "INF053": None,
    "INF054": None,
    "DAD01": {
      "DAD01.a": "b",
      "DAD01.b": "c",
      "DAD01.c": "c",
      "DAD01.d": "a",
      "DAD01.e": "b",
      "DAD01.f": "c",
      "DAD01.g": "c",
      "DAD01.h": "c",
      "DAD01.i": "b",
      "DAD01.j": "b",
      "DAD01.k": "c",
      "DAD01.l": "a"
    },
    "DAD02": "DAD02.e",
    "DAD03": "DAD03.g",
    "DAD04": [
      "DAD04.e"
    ],
    "DAD05": None,
    "DAD051": None,
    "DAD06": "DAD06.a",
    "DAD07": "DAD07.a",
    "DAD08": "DAD08.b",
    "DAD09": None,
    "SERV01": {
      "SERV01.a": {
        "Multicanais": [
          "c"
        ]
      },
      "SERV01.b": {
        "Informacional": [
          "e"
        ]
      },
      "SERV01.c": {
        "Não sabe": [
          "h"
        ]
      },
      "SERV01.d": {
        "Informacional": [
          "e"
        ]
      },
      "SERV01.e": {
        "Não sabe": [
          "h"
        ]
      },
      "SERV01.f": {
        "Informacional": [
          "e"
        ]
      },
      "SERV01.g": {
        "Não sabe": [
          "h"
        ]
      },
      "SERV01.h": {
        "Não sabe": [
          "h"
        ]
      },
      "SERV01.i": {
        "Transacional": [
          "d"
        ]
      },
      "SERV01.j": {
        "Multicanais": [
          "c"
        ]
      },
      "SERV01.k": {
        "Não sabe": [
          "h"
        ]
      },
      "SERV01.l": {
        "Não sabe": [
          "h"
        ]
      }
    },
    "SERV03": [
      "SERV03.i",
      "SERV03.j"
    ],
    "SERV04": [
      "SERV04.a",
      "SERV04.b",
      "SERV04.c",
      "SERV04.e"
    ],
    "SERV05": "SERV05.b",
    "SERV051": None,
    "SERV06": "SERV06.b",
    "SERV061": None,
    "SERV07": "SERV07.c",
    "SERV071": None,
    "MON01": "MON01.a",
    "MON02": [
      "MON02.m"
    ],
    "MON03": "MON03.b",
    "MON04": "MON04.e",
    "MON05": "MON05.a"
  }

a = {property_name_mapping.get(key, key): value for key, value in test_planaltina2.items()}

transformed_data = SurveyData(**a)

print(transformed_data.dict())