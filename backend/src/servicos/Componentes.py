
class Componente:
    def __init__(self, fixadores, universo, qualificadores) -> None:
        self.fixadores = fixadores
        self.universo = universo
        self.qualificadores = qualificadores

    def soma(self, respostas: dict):
        peso = list(self.universo.values())
        soma = 0
        for alternativa in self.universo:
            if alternativa in respostas[alternativa.split('.')[0]]:
                soma = soma + respostas.get(alternativa) * peso
            else:
                return soma

    def get_nivel_soma(self, respostas):
        soma = self.soma(respostas)
        for nivel, limites in self.limite.items():
            if soma in limites:
                nivel_soma = nivel
        return nivel_soma

    def get_nivel_fixador(self, respostas, nome_comp):
        for nivel, fixador in self.fixadores.items():
            for val in fixador:  # Cria lista com fixadores encontrados
                encontrados = [any(v in n for n in respostas.values())
                               for v in val]
                if any(encontrados):  # Se todos qualificadores do nível foram encontrados, definir o nível
                    nivel_quali = nivel
                else:
                    nivel_quali = nome_comp+"1"
                return nivel_quali

    def get_nivel_quali(self, respostas, nome_comp):
        for nivel, qualificador in self.qualificadores.items():
            for val in qualificador:
                # Cria lista com qualificadores encontrados
                encontrados = [any(v in n for n in respostas.values())
                               for v in val]
                if any(encontrados):  # Se todos qualificadores do nível foram encontrados, definir o nível
                    nivel_quali = nivel
                else:
                    nivel_quali = nome_comp+"1"
                return nivel_quali

    def verificador(self, respostas: dict, nome_comp: str):
        # Verificar qual qualificadores estão presentes no nível mais alto
        if not self.qualificadores and self.limite:  # Se nao tiver qualificadores
            nivel = self.get_nivel_soma(respostas)[-1]
            return int(nivel[-1])
        elif not self.limite and not self.qualificadores:  # Se nao tiver limites para soma
            nivel = self.get_nivel_fixador(respostas, nome_comp)
            return int(nivel[-1])
        else:
            nivel_soma = self.get_nivel_soma(respostas)
            nivel_quali = self.get_nivel_quali(respostas, nome_comp)        
            # Selecionar o nível de acordo com a melhor classificação
            if int(nivel_soma[-1]) > int(nivel_quali[-1]):
                return int(nivel_soma[-1])
            return int(nivel_quali[-1])


class Eplan(Componente):
    def __init__(self):
        self.fixadores = {"Eplan1": ["EST03.a", "EST03.k"],
                          "Eplan2": [],
                          "Eplan3": [],
                          "Eplan4": [],
                          "Eplan5": [],
                          "Eplan6": [],
                          "Eplan7": []}
        self.qualificadores = {"Eplan1": [],
                               "Eplan2": [],
                               "Eplan3": [],
                               "Eplan4": ["EST03.c", "EST03.h"],
                               "Eplan5": ["EST03.i"],
                               "Eplan6": ["EST03.1.g", "EST03.1.j"],
                               "Eplan7": ["EST03.1.g", "EST03.1.j", "EST03.1.k", "EST03.1.l"]}
        self.universo = {"EST03.a": 0,
                         "EST03.b": 1,
                         "EST03.c": 1,
                         "EST03.d": 1,
                         "EST03.e": 1,
                         "EST03.f": 1,
                         "EST03.g": 1,
                         "EST03.h": 1,
                         "EST03.i": 1,
                         "EST03.k": 0,
                         "EST03.1.c": 1,
                         "EST03.1.d": 1,
                         "EST03.1.e": 1,
                         "EST03.1.f": 1,
                         "EST03.1.g": 1,
                         "EST03.1.h": 1,
                         "EST03.1.i": 1,
                         "EST03.1.j": 1,
                         "EST03.1.k": 1,
                         "EST03.1.l": 1,
                         "EST03.1.m": 0}
        self.limite = {"Eplan1": [0],
                       "Eplan2": [1],
                       "Eplan3": [2, 3],
                       "Eplan4": [4],
                       "Eplan5": [5, 6],
                       "Eplan6": [7, 8],
                       "Eplan7": [9]}
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)


class GovCol(Componente):
    def __init__(self):
        self.fixadores = {"GovCol2": [],
                          "GovCol3": [],
                          "GovCol4": [],
                          "GovCol5": [],
                          "GovCol6": [],
                          "GovCol7": []}
        self.qualificadores = {}
        self.universo = {"EST04.a": 0,
                         "EST04.b": 1,
                         "EST04.c": 1,
                         "EST04.d": 2,
                         "EST04.e": 2,
                         "EST04.f": 2,
                         "EST04.g": 2,
                         "EST04.h": 1,
                         "EST04.i": 2,
                         "EST04.j": 2,
                         "EST04.k": 2,
                         "EST04.l": 2,
                         "EST04.m": 1,
                         "EST04.o": -1,
                         "EST06.1.a": 0,
                         "EST06.1.b": 1,
                         "EST06.1.c": 1,
                         "EST06.1.d": 2,
                         "EST06.1.e": 2,
                         "EST06.1.f": 2,
                         "EST06.1.g": 2,
                         "EST06.1.h": 1,
                         "EST06.1.i": 2,
                         "EST06.1.j": 2,
                         "EST06.1.k": 2,
                         "EST06.1.l": 1,
                         "EST06.1.n": 0}
        self.limite = {"GovCol1": [0],
                       "GovCol2": [1, 2, 3, 4, 5],
                       "GovCol3": [6, 7, 8, 9, 10, 11],
                       "GovCol4": [12, 13, 14, 15, 16, 17],
                       "GovCol5": [18, 19, 20, 21, 22, 23],
                       "GovCol6": [24, 25, 26, 27, 28, 29],
                       "GovCol7": [list(range(30, 80))]}
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)


#TODO: Implementar as regras para qualificadores
class GovTec(Componente):
    def __init__(self):
        self.fixadores = {"GovTec1": ["EST05.d", "EST07.d"],
                          "GovTec2": [],
                          "GovTec3": ["EST05.d", "EST07.d"],
                          "GovTec4": [],
                          "GovTec5": [],
                          "GovTec6": [],
                          "GovTec7": []}
        self.qualificadores = {"GovTec1": [],
                               "GovTec2": [],
                               "GovTec3": [],
                               "GovTec4": ["EST05.a", "EST05.b", "EST05.c",
                                           "EST07.a", "EST07.b", "EST07.c"],
                               "GovTec5": ["EST05.a", "EST05.b", "EST05.c",
                                           "EST07.a", "EST07.b", "EST07.c"],
                               "GovTec6": ["EST05.a", "EST05.b", "EST05.c",
                                           "EST07.a", "EST07.b", "EST07.c",
                                           "EST05.1.d", "EST05.1.e", "EST05.1.f",
                                           "EST05.1.g", "EST05.1.h", "EST05.1.i",
                                           "EST05.1.j", "EST05.1.k",
                                           "EST07.1.d", "EST07.1.e", "EST07.1.f",
                                           "EST07.1.g", "EST07.1.h", "EST07.1.i",
                                           "EST07.1.j", "EST07.1.k"],
                               "GovTec7": ["EST05.a", "EST05.b", "EST05.c",
                                           "EST07.a", "EST07.b", "EST07.c",
                                           "EST05.1.d", "EST05.1.e", "EST05.1.f",
                                           "EST05.1.g", "EST05.1.h", "EST05.1.i",
                                           "EST05.1.j", "EST05.1.k",
                                           "EST07.1.d", "EST07.1.e", "EST07.1.f",
                                           "EST07.1.g", "EST07.1.h", "EST07.1.i",
                                           "EST07.1.j", "EST07.1.k"]}
        self.universo = {"EST05.a": 3,
                         "EST05.b": 3,
                         "EST05.c": 3,
                         "EST05.d": 2,
                         "EST05.e": 1,
                         "EST05.f": 1,
                         "EST05.g": -1,
                         "EST05.h": 0,
                         "EST07.a": 3,
                         "EST07.b": 3,
                         "EST07.c": 3,
                         "EST07.d": 2,
                         "EST07.e": 1,
                         "EST07.f": 1,
                         "EST07.g": -1,
                         "EST07.h": 0,
                         "EST05.1.a": 0,
                         "EST05.1.b": 1,
                         "EST05.1.c": 1,
                         "EST05.1.d": 2,
                         "EST05.1.e": 2,
                         "EST05.1.f": 2,
                         "EST05.1.g": 2,
                         "EST05.1.h": 1,
                         "EST05.1.i": 2,
                         "EST05.1.j": 2,
                         "EST05.1.k": 2,
                         "EST05.1.l": 1,
                         "EST05.1.n": 0,
                         "EST07.1.a": 0,
                         "EST07.1.b": 1,
                         "EST07.1.c": 1,
                         "EST07.1.d": 2,
                         "EST07.1.e": 2,
                         "EST07.1.f": 2,
                         "EST07.1.g": 2,
                         "EST07.1.h": 1,
                         "EST07.1.i": 2,
                         "EST07.1.j": 2,
                         "EST07.1.k": 2,
                         "EST07.1.l": 1,
                         "EST07.1.n": 0}
        self.limite = {"GovTec1": [0],
                       "GovTec2": [1, 2, 3],
                       "GovTec3": [4, 5],
                       "GovTec4": [6, 7, 8, 9],
                       "GovTec5": [list(range(10, 18))],
                       "GovTec6": [list(range(18, 26))],
                       "GovTec7": [list(range(26, 80))]}
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)


class SegPol(Componente):
    def __init__(self):
        self.fixadores = {"SegPol1": ["EST06.a"],
                          "SegPol2": ["EST06.b"],
                          "SegPol3": ["EST06.c"],
                          "SegPol4": ["EST06.d"],
                          "SegPol5": ["EST06.e"],
                          "SegPol6": ["EST06.f"]}
        self.qualificadores = {}
        self.universo = {}
        self.limite = {}
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)


class Vis(Componente):
    def __init__(self):
        self.fixadores = {"Vis2": ["EST09.a", "EST09.e"],
                          "Vis3": ["EST09.c"],
                          "Vis4": ["EST09.b"]}
        self.qualificadores = {}
        self.universo = {}
        self.limite = {}
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)
