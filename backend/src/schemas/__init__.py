from pydantic import BaseModel
from typing import List, Optional


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

property_name_mapping = {
    'EST01': 'EST01',
    'EST02': 'EST02',
    'EST03': 'EST03',
    'EST04': 'EST04',
    'EST05': 'EST05',
    'EST05Extra': 'EST05Extra',
    'EST05.1': 'EST051',
    'EST05.1Extra': 'EST051Extra',
    'EST06': 'EST06',
    'EST06.1': 'EST061',
    'EST06.1Extra': 'EST061Extra',
    'EST07': 'EST07',
    'EST07Extra': 'EST07Extra',
    'EST07.1': 'EST071',
    'EST07.1Extra': 'EST071Extra',
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
    EST05Extra: Optional[str] = None
    EST051Extra: Optional[str] = None
    EST061Extra: Optional[str] = None
    EST07Extra: Optional[str] = None
    EST071Extra: Optional[str] = None
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
    INF02: Optional[List[str]] = None
    INF03: Optional[List[str]] = None
    INF031: Optional[str] = None
    INF04: Optional[List[str]] = None
    INF041: Optional[List[str]] = None
    INF05: Optional[str] = None
    INF051: Optional[str] = None
    INF052: Optional[str] = None
    INF053: Optional[str] = None
    INF054: Optional[str] = None
    DAD01: Optional[List[str]] = None
    DAD02: Optional[str] = None
    DAD03: Optional[str] = None
    DAD04: Optional[List[str]] = None
    DAD05: Optional[str] = None
    DAD06: Optional[str] = None
    DAD07: Optional[str] = None
    DAD08: Optional[str] = None
    DAD09: Optional[List[str]] = None
    SERV01: Optional[List[str]] = None
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

# class SurveyData(BaseModel):
#     municipio: Optional[str]
#     EST01: Optional[List[str]]
#     EST02: Optional[List[str]]
#     EST03: Optional[List[str]]
#     EST04: Optional[List[str]]
#     EST051: Optional[List[str]]
#     EST05: Optional[List[str]]
#     EST05Extra: Optional[str]
#     EST051Extra: Optional[str]
#     EST06: Optional[str]
#     EST061: Optional[List[str]]
#     EST061Extra: Optional[str]
#     EST07: Optional[List[str]]
#     EST07Extra: Optional[str]
#     EST071: Optional[List[str]]
#     EST071Extra: Optional[str]
#     EST08: Optional[str]
#     EST09: Optional[List[str]]
#     INF4005: Optional[str]
#     INF4031: Optional[str]
#     INF4041: Optional[str]
#     INF4046: Optional[str]
#     INF3122: Optional[str]
#     INF3027: Optional[str]
#     INF3077: Optional[str]
#     INF3110: Optional[str]
#     INF3117: Optional[str]
#     INF3124: Optional[str]
#     INF3127: Optional[str]
#     INF01: Optional[str]
#     INF011: Optional[str]
#     INF012: Optional[str]
#     INF013: Optional[List[str]]
#     INF014: Optional[str]
#     INF02: Optional[List[str]]
#     INF03: Optional[List[str]]
#     INF031: Optional[str]
#     INF04: Optional[List[str]]
#     INF041: Optional[List[str]]
#     INF05: Optional[str]
#     INF051: Optional[str]
#     INF052: Optional[str]
#     INF053: Optional[str]
#     INF054: Optional[str]
#     DAD01: Optional[List[str]]
#     DAD02: Optional[str]
#     DAD03: Optional[str]
#     DAD04: Optional[List[str]]
#     DAD05: Optional[str]
#     DAD06: Optional[str]
#     DAD07: Optional[str]
#     DAD08: Optional[str]
#     DAD09: Optional[List[str]]
#     SERV01: Optional[List[str]]
#     SERV02: Optional[List[str]]
#     SERV03: Optional[List[str]]
#     SERV04: Optional[List[str]]
#     SERV05: Optional[str]
#     SERV051: Optional[List[str]]
#     SERV06: Optional[str]
#     SERV061: Optional[str]
#     SERV07: Optional[str]
#     SERV071: Optional[str]
#     MON01: Optional[str]
#     MON02: Optional[List[str]]
#     MON03: Optional[str]
#     MON04: Optional[str]
#     MON05: Optional[str]
