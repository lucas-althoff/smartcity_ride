
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




a = {property_name_mapping.get(key, key): value for key, value in input_data.items()}

transformed_data = SurveyData(**a)

print(transformed_data.dict())