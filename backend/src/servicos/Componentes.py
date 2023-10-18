
class Componente:
    def __init__(self, fixadores, universo, qualificadores) -> None:
        self.fixadores = fixadores
        self.universo = universo
        self.qualificadores = qualificadores

    def soma(self, respostas: dict):
        soma = 0
        for alternativa, peso in self.universo.items():
            prefix = alternativa.split('.')[0] 
            if alternativa in respostas[prefix]:
                soma = soma + peso
        return soma

    def get_nivel_soma(self, respostas):
        soma = self.soma(respostas)
        for nivel, limites in self.limite.items():
            if soma in limites:
                nivel_soma = nivel
        return nivel_soma

    def get_nivel_fixador(self, respostas):
        # print("RESP", respostas)
        for nivel, fixador in self.fixadores.items():  # Desempacotar lista de fixadores por nivel
            for _, nota in respostas.items():  # Desempacotar lista de notas por questão
                print("FIX", fixador)
                print("NOTA", nota)
                if fixador in list(nota):  # Se um fixador for encontrados na nota, definir o nível  
                    return nivel
        # nenhum fixador encontrado
        return False

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
        if not self.qualificadores and self.limite:  # Se nao tiver qualificadores e tiver regra baseado no somatório
            nivel = self.get_nivel_soma(respostas)[-1]
            return int(nivel[-1])
        # Se nao tiver regra baseada no somatório e nem baseada em qualificadores
        elif not self.limite and not self.qualificadores:
            nivel = self.get_nivel_fixador(respostas)
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

    def verificador_interno(self, respostas: dict, nivel: int):
        # Verificar qual qualificadores estão presentes no nível mais alto
        match nivel:
            case 1:
                if super().soma(respostas=respostas) == 0 or \
                        all([v in respostas["EST03"] for v in self.fixadores["Eplan1"]]): 
                    return True
                return False
            case 2:
                if super().soma(respostas=respostas) == 1:
                    return True
                return False
            case 3:
                if super().get_nivel_soma(respostas=respostas) == "Eplan3":
                    return True
                return False
            case 4:
                print("QUALI", respostas["EST04"])
                if super().soma(respostas=respostas) == 4 or \
                        all([v in respostas["EST03"] for v in self.qualificadores["Eplan4"]]):  # Verifica se todos qualificadores estão presentes
                    return True
                return False
            case 5:
                if super().get_nivel_soma(respostas=respostas) == "Eplan5" or \
                        all([v in respostas["EST03"] for v in self.qualificadores["Eplan5"]]):  # Verifica se todos qualificadores estão presentes
                    return True
                return False
            case 6:
                if super().get_nivel_soma(respostas=respostas) == "Eplan6" and \
                        any([v in respostas['EST03'] for v in self.qualificadores["Eplan6"]]):  # Verifica se um dos qualificadores está presente
                    return True
                # Verifica se todos qualificadores estão presentes
                elif all([v in respostas['EST03'] for v in self.qualificadores["Eplan6"]]):
                    return True
                else:
                    return False
            case 7:
                if super().soma(respostas=respostas) >= 9 and \
                        all([v in respostas['EST03'] for v in self.qualificadores["Eplan7"]]):  # Verifica se todos qualificadores estão presentes
                    return True
                return False

    def maturidade(self, respostas: dict):
        print(super().soma(respostas=respostas))
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"Eplan{nivel}"
        return resultado


class GovCol(Componente):
    def __init__(self):
        self.fixadores = {}
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
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 2:
                if super().soma(respostas=respostas) in list(range(1, 6)):
                    return True
                return False
            case 3:
                if super().soma(respostas=respostas) in list(range(6, 12)):
                    return True
                return False
            case 4:
                if super().soma(respostas=respostas) in list(range(12, 18)):
                    return True
                return False
            case 5:
                if super().soma(respostas=respostas) in list(range(18, 24)):
                    return True
                return False
            case 6:
                if super().soma(respostas=respostas) in list(range(24, 30)):
                    return True
                return False
            case 7:
                if super().soma(respostas=respostas) >= 30:
                    return True
                return False

    def maturidade(self, respostas: dict):
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"GovCol{nivel}"
        return resultado


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

    def verificador_interno(self, respostas: dict, nivel: int):
        # Verificar qual qualificadores estão presentes no nível mais alto
        match nivel:
            case 1:
                if super().soma(respostas=respostas) >= 0 or \
                        (all([v in respostas['EST05'] for v in self.fixadores["GovTec1"]]) and \
                            all([v in respostas['EST07'] for v in self.fixadores["GovTec1"]])):
                    return True
                return False
            case 2:
                if super().soma(respostas=respostas) in self.limite['GovTec2']:
                    return True
                return False
            case 3:
                if super().soma(respostas=respostas) in self.limite['GovTec3'] or \
                        (all([v in respostas['EST05'] for v in self.fixadores["GovTec3"]]) and \
                            all([v in respostas['EST07'] for v in self.fixadores["GovTec3"]])):
                    return True
                return False
            case 4:
                if super().soma(respostas=respostas) in self.limite['GovTec4'] or \
                        any([v in respostas['EST05'] for v in self.qualificadores["GovTec4"][:3]]) and \
                        any([v in respostas['EST07'] for v in self.qualificadores["GovTec4"][3:]]):
                    return True
                return False
            case 5:
                if super().soma(respostas=respostas) in self.limite['GovTec5'] and \
                        any([v in respostas['EST05'] for v in self.qualificadores["GovTec5"][:3]]) and \
                        any([v in respostas['EST07'] for v in self.qualificadores["GovTec5"][3:]]):
                    return True
                return False
            case 6:
                c1 = super().get_nivel_soma(respostas=respostas) == "Eplan6"
                c2 = (any([v in respostas['EST05'] for v in self.qualificadores["GovTec6"][:3]]) and \
                      any([v in respostas['EST07'] for v in self.qualificadores["GovTec6"][3:6]]))
                c3 = (all([v in respostas['EST05'] for v in self.qualificadores["GovTec6"][6:8]]) and \
                      any([v in respostas['EST05'] for v in self.qualificadores["GovTec6"][8:13]]))
                c4 = (all([v in respostas['EST07'] for v in self.qualificadores["GovTec6"][13:15]]) and \
                      any([v in respostas['EST07'] for v in self.qualificadores["GovTec6"][15:]]))
                if c1 and c2 and c3 and c4:
                    return True
                return False
            case 7:
                c1 = super().get_nivel_soma(respostas=respostas) == "Eplan7"
                c2 = (any([v in respostas['EST05'] for v in self.qualificadores["GovTec7"][:3]]) and \
                      any([v in respostas['EST07'] for v in self.qualificadores["GovTec7"][3:6]]))
                c3 = all([v in respostas['EST05'] for v in self.qualificadores["GovTec7"][6:13]])
                c4 = all([v in respostas['EST07'] for v in self.qualificadores["GovTec7"][13:]])
                if c1 and c2 and c3 and c4:
                    return True
                return False

    def maturidade(self, respostas: dict):
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"GovTec{nivel}"
        return resultado


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

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol1"]]): 
                    return True
                return False
            case 2:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol2"]]): 
                    return True
                return False
            case 3:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol3"]]): 
                    return True
                return False
            case 4:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol4"]]): 
                    return True
                return False
            case 5:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol5"]]): 
                    return True
                return False
            case 6:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol6"]]): 
                    return True
                return False

    def maturidade(self, respostas: dict):
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"SegPol{nivel}"
        return resultado


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

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 2:
                if all([v in respostas["EST09"] for v in self.fixadores["Vis2"]]): 
                    return True
                return False
            case 3:
                if all([v in respostas["EST09"] for v in self.fixadores["Vis3"]]): 
                    return True
                return False
            case 4:
                if all([v in respostas["EST09"] for v in self.fixadores["Vis4"]]): 
                    return True
                return False

    def maturidade(self, respostas: dict):
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"Vis{nivel}"
        return resultado


# Infraestrutura
class ITPlan(Componente):
    def __init__(self):
        self.fixadores = {"ITPlan1": ["INF05.b"],
                          "ITPlan3": ["INF05.1.b"],
                          "ITPlan4": ["INF05.a", "INF05.2.b"],
                          "ITPlan5": ["INF05.2.a", "INF05.3.b", "INF05.4.b"],
                          "ITPlan6": ["INF05.3.a", "INF05.4.a", "INF05.5.b"],
                          "ITPlan7": ["INF05.5.a"]}
        self.qualificadores = {"ITPlan2": ["INF05.1.a","INF05.b"]}
        self.universo = {}
        self.limite = {}
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if any([v in respostas["INF05"] for v in self.fixadores["ITPlan1"]]): 
                    return True
                return False
            case 2:
                if any([v in respostas["INF05.1"] for v in self.qualificadores["ITPlan2"][0]]): 
                    return True
                return False
            case 3:
                if all([v in respostas["INF05.1"] for v in self.fixadores["ITPlan3"]]): 
                    return True
                return False
            case 4:
                if any([v in respostas["INF05"] for v in self.fixadores["ITPlan4"]]) and \
                    any([v in respostas["INF05.2"] for v in self.fixadores["ITPlan4"]]):
                    return True
                return False
            case 5:
                if any([v in respostas["INF05.2"] for v in self.fixadores["ITPlan5"]]) and \
                    any([v in respostas["INF05.3"] for v in self.fixadores["ITPlan5"]]) and \
                    any([v in respostas["INF05.4"] for v in self.fixadores["ITPlan5"]]):
                    return True
                return False
            case 6:
                if any([v in respostas["INF05.3"] for v in self.fixadores["ITPlan6"]]) and \
                    any([v in respostas["INF05.4"] for v in self.fixadores["ITPlan6"]]) and \
                    any([v in respostas["INF05.5"] for v in self.fixadores["ITPlan6"]]):
                    return True
                return False
            case 7:
                if all([v in respostas["INF05.6"] for v in self.fixadores["ITPlan3"]]): 
                    return True
                return False

    def maturidade(self, respostas: dict):
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"SegPol{nivel}"
        return resultado

class Inst(Componente):
    def __init__(self):
        self.fixadores = {"Inst1": ["INF05.b"],
                          "Inst3": ["INF05.1.b"],
                          "Inst4": ["INF05.a", "INF05.2.b"],
                          "Inst5": ["INF05.2.a", "INF05.3.b", "INF05.4.b"],
                          "Inst6": ["INF05.3.a", "INF05.4.a", "INF05.5.b"],
                          "Inst7": ["INF05.5.a"]}
        self.qualificadores = {"Inst1": ["INF01.b","INF01.c"]}
        self.universo = {
            "INF02.aa": 0,
            "INF02.ab": 0,
            "INF02.ac": 0,
            "INF02.ba": 1,
            "INF02.bb": 1,
            "INF02.bc": 1,
            "INF02.ca": 1,
            "INF02.cb": 1,
            "INF02.cc": 1,
            "INF02.da": 2,
            "INF02.db": 2,
            "INF02.dc": 2,
            "INF02.ea": 4,
            "INF02.eb": 2,
            "INF02.ec": 2,
            "INF02.fa": 4,
            "INF02.fb": 2,
            "INF02.fc": 2,
            "INF02.ga": 0,
            "INF02.gb": 0,
            "INF02.gc": 0
        }
        self.limite = {
            "ITPlan1": [0, 1],
            "ITPlan3": [],
            "ITPlan4": [],
            "ITPlan5": [],
            "ITPlan6": [],
            "ITPlan7": []
        }
        super().__init__(fixadores=self.fixadores,
                         qualificadores=self.qualificadores,
                         universo=self.universo)

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if super().soma in [0, 1] and \
                    any([v in respostas["INF01"] for v in self.qualificadores["Inst1"]]): 
                    return True
                return False
            case 2:
                if super().soma(respostas=respostas) in [2, 3] and \
                    any([v in respostas["INF01.1"] for v in self.qualificadores["Inst2"]]): 
                    return True
                return False
            case 3:
                if super().soma(respostas=respostas) in [4, 5] and \
                    any([v in respostas["INF01.1"] for v in self.fixadores["Inst3"]]):
                    return True
                return False
            case 4:
                if super().soma(respostas=respostas) in [6, 7] and \
                    any([v in respostas["INF01"] for v in self.fixadores["Inst4"]]):
                    return True
                return False
            case 5:
                if super().soma(respostas=respostas) in [8, 9] and \
                    any([v in respostas["INF01"] for v in self.fixadores["Inst5"]]):
                    return True
                return False
            case 6:
                if super().soma(respostas=respostas) in [10, 11] and \
                    any([v in respostas["INF01"] for v in self.fixadores["Inst6"]]):
                    return True
                return False
            case 7:
                if super().soma(respostas=respostas) in [10, 11] and \
                    all([v in respostas["INF01"] for v in self.fixadores["Inst7"]]): 
                    return True
                return False

    def maturidade(self, respostas: dict):
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"SegPol{nivel}"
        return resultado

class IUPlan(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado
    
class AQua(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

class HwSw(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

class GovTI(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

# DADOS
class DPlan(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado
    
class Digi(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado


class DTransp(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado


class DInteg(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

# Serviços e Aplicações
class SPlan(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

class SUrb(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

class SOn(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

class SInteg(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado

# Monitoramento
class MPlan(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado
    

class Coord(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado


class Perc(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado


class MTransp(Componente):
    def __init__(self):
       self.nivel = 1
    def maturidade(self, respostas: dict):
        resultado = f"SegPol{self.nivel}"
        return resultado


if "__main__" == __name__:
    notas = {'EST03': ['EST03.g'], 'EST03.1': ['EST03.1.b'], 'EST04': ['EST04.f'], 'EST05': ['EST05.a', 'EST05.b', 'EST05.h', 'EST05.g'], 'EST05.1': ['EST05.1.b'], 'EST06': ['EST06.a'], 'EST06.1': ['EST06.1.h'], 'EST07': ['EST07.g'], 'EST07.1': [
        'EST07.1.e'], 'EST08': ['EST08.b'], 'EST09': ['EST09.c'], 'EST01': ['EST01.a', 'EST01.b', 'EST01.c', 'EST01.d', 'EST01.e'], 'EST02': ['EST02.a', 'EST02.b', 'EST02.c', 'EST02.d', 'EST02.e'], 'municipio': 'Cabeceira Grande (MG)'}
    obj = SegPol()
    print(obj.maturidade(respostas=notas))
