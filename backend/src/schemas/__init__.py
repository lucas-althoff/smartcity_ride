from typing import Optional
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
    "EST03.1": "EST031",
    "EST05.1": "EST051",
    "EST05.1Extra": "EST051Extra",
    "EST06.1": "EST061",
    "EST06.1Extra": "EST061Extra",
    "EST07.1": "EST071",
    "EST07.1Extra": "EST071Extra",
    "EST08.1": "EST081",
    "EST08.1Extra": "EST081Extra",
    "INF01.1": "INF011",
    "INF04.1": "INF041",
    "INF05.1": "INF051",
    "SERV05.1": "SERV051",
    "SERV06.1": "SERV061",
    "SERV07.1": "SERV071",
}


class SurveyData(BaseModel):
    municipio: Optional[str]
    EST01: Optional[List[str]]
    EST02: Optional[List[str]]
    EST03: Optional[List[str]]
    EST04: Optional[List[str]]
    EST051: Optional[List[str]]
    EST05: Optional[List[str]]
    EST05Extra: Optional[str]
    EST051Extra: Optional[str]
    EST06: Optional[str]
    EST061: Optional[List[str]]
    EST061Extra: Optional[str]
    EST07: Optional[List[str]]
    EST07Extra: Optional[str]
    EST071: Optional[List[str]]
    EST071Extra: Optional[str]
    EST08: Optional[str]
    EST09: Optional[List[str]]
    INF4005: Optional[str]
    INF4031: Optional[str]
    INF4041: Optional[str]
    INF4046: Optional[str]
    INF3122: Optional[str]
    INF3027: Optional[str]
    INF3077: Optional[str]
    INF3110: Optional[str]
    INF3117: Optional[str]
    INF3124: Optional[str]
    INF3127: Optional[str]
    INF01: Optional[str]
    INF011: Optional[str]
    INF012: Optional[str]
    INF013: Optional[List[str]]
    INF014: Optional[str]
    INF02: Optional[List[str]]
    INF03: Optional[List[str]]
    INF031: Optional[str]
    INF04: Optional[List[str]]
    INF041: Optional[List[str]]
    INF05: Optional[str]
    INF051: Optional[str]
    INF052: Optional[str]
    INF053: Optional[str]
    INF054: Optional[str]
    DAD01: Optional[List[str]]
    DAD02: Optional[str]
    DAD03: Optional[str]
    DAD04: Optional[List[str]]
    DAD05: Optional[str]
    DAD06: Optional[str]
    DAD07: Optional[str]
    DAD08: Optional[str]
    DAD09: Optional[List[str]]
    SERV01: Optional[List[str]]
    SERV03: Optional[List[str]]
    SERV04: Optional[List[str]]
    SERV05: Optional[str]
    SERV051: Optional[List[str]]
    SERV06: Optional[str]
    SERV061: Optional[str]
    SERV07: Optional[str]
    SERV071: Optional[str]
    MON01: Optional[str]
    MON02: Optional[List[str]]
    MON03: Optional[str]
    MON04: Optional[str]
    MON05: Optional[str]
