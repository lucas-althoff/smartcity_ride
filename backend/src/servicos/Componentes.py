
def soma(respostas: dict, universo: dict):
    soma = 0
    for alternativa, peso in universo.items():
        prefix = alternativa.split('.')[0]
        # print("ALTERNATIVA", alternativa)
        # print("PREFIX", prefix)
        if alternativa in respostas[prefix]:
            soma = soma + peso
    return soma


class EPlan():
    def __init__(self):
        self.componente = "EPlan"
        self.nivel_inicial = "1"
        self.fixadores = {"EPlan1": ["EST03.a", "EST03.k"]}
        self.qualificadores = {"EPlan4": ["EST03.c", "EST03.h"],
                               "EPlan5": ["EST03.i"],
                               "EPlan6": ["EST03.1.g", "EST03.1.j"],
                               "EPlan7": ["EST03.1.g", "EST03.1.j", "EST03.1.k", "EST03.1.l"]}
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

    def verificador_interno(self, respostas: dict, nivel: int):
        # Verificar qual qualificadores estão presentes no nível mais alto
        match nivel:
            case 1:
                c1 = soma(respostas=respostas, universo=self.universo) == 0
                c2 = all([v in respostas["EST03"] for v in self.fixadores["EPlan1"]])
                if c1 or c2:  # Critério soma e fixadores
                    return True
                return False
            case 2:
                if soma(respostas=respostas, universo=self.universo) == 1:  # Critério soma inicial
                    return True
                return False
            case 3:
                if soma(respostas=respostas, universo=self.universo) in [2, 3]:  # Critério soma
                    return True
                return False
            case 4:
                if soma(respostas=respostas, universo=self.universo) == 4 or \
                        all([v in respostas["EST03"] for v in self.qualificadores["EPlan4"]]):  # Critério soma ou qualificador
                    return True
                return False
            case 5:
                if soma(respostas=respostas, universo=self.universo) in [5, 6] or \
                        all([v in respostas["EST03"] for v in self.qualificadores["EPlan5"]]):  # Critério soma ou qualificador
                    return True
                return False
            case 6:
                if soma(respostas=respostas, universo=self.universo) in [7, 8] and \
                        any([v in respostas['EST03'] for v in self.qualificadores["EPlan6"]]):  # Critério soma e qualificador
                    return True
                # Verifica se todos qualificadores estão presentes
                elif all([v in respostas['EST03'] for v in self.qualificadores["EPlan6"]]):  # Critério qualificador exclusivo
                    return True
                else:
                    return False
            case 7:
                if soma(respostas=respostas, universo=self.universo) >= 9 and \
                        all([v in respostas['EST03'] for v in self.qualificadores["EPlan7"]]):  # Critério soma e qualificador
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class GovCol():
    def __init__(self):
        self.componente = "GovCol"
        self.nivel_inicial = "2"
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

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 2:
                if soma(respostas=respostas, universo=self.universo) in list(range(1, 6)):  # Critério soma
                    return True
                return False
            case 3:
                if soma(respostas=respostas, universo=self.universo) in list(range(6, 12)):  # Critério soma
                    return True
                return False
            case 4:
                if soma(respostas=respostas, universo=self.universo) in list(range(12, 18)):  # Critério soma
                    return True
                return False
            case 5:
                if soma(respostas=respostas, universo=self.universo) in list(range(18, 24)):  # Critério soma
                    return True
                return False
            case 6:
                if soma(respostas=respostas, universo=self.universo) in list(range(24, 30)):  # Critério soma
                    return True
                return False
            case 7:
                if soma(respostas=respostas, universo=self.universo) >= 30:  # Critério soma
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class GovTec():
    def __init__(self):
        self.componente = "GovTec"
        self.nivel_inicial = "1"
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
                       "GovTec5": list(range(10, 18)),
                       "GovTec6": list(range(18, 26)),
                       "GovTec7": list(range(26, 80))}

    def verificador_interno(self, respostas: dict, nivel: int):
        # Verificar qual qualificadores estão presentes no nível mais alto
        match nivel:
            case 1:
                if soma(respostas=respostas, universo=self.universo) >= 0 or \
                        (all([v in respostas['EST05'] for v in self.fixadores["GovTec1"]]) and
                            all([v in respostas['EST07'] for v in self.fixadores["GovTec1"]])):  # Critério soma ou fixadores
                    return True
                return False
            case 2:
                if soma(respostas=respostas, universo=self.universo) in self.limite['GovTec2']:  # Critério soma
                    return True
                return False
            case 3:
                if soma(respostas=respostas, universo=self.universo) in self.limite['GovTec3'] or \
                        (all([v in respostas['EST05'] for v in self.fixadores["GovTec3"]]) and
                            all([v in respostas['EST07'] for v in self.fixadores["GovTec3"]])):  # Critério soma ou fixadores
                    return True
                return False
            case 4:
                if soma(respostas=respostas, universo=self.universo) in self.limite['GovTec4'] or \
                        any([v in respostas['EST05'] for v in self.qualificadores["GovTec4"][:3]]) and \
                        any([v in respostas['EST07'] for v in self.qualificadores["GovTec4"][3:]]):  # Critério soma ou qualificadores
                    return True
                return False
            case 5:
                if soma(respostas=respostas, universo=self.universo) in self.limite['GovTec5'] and \
                        any([v in respostas['EST05'] for v in self.qualificadores["GovTec5"][:3]]) and \
                        any([v in respostas['EST07'] for v in self.qualificadores["GovTec5"][3:]]):  # Critério soma ou qualificadores
                    return True
                return False
            case 6:
                c1 = soma(respostas=respostas, universo=self.universo) in self.limite['GovTec6']
                c2 = (any([v in respostas['EST05'] for v in self.qualificadores["GovTec6"][:3]]) and
                      any([v in respostas['EST07'] for v in self.qualificadores["GovTec6"][3:6]]))
                c3 = (all([v in respostas['EST05'] for v in self.qualificadores["GovTec6"][6:8]]) and
                      any([v in respostas['EST05'] for v in self.qualificadores["GovTec6"][8:13]]))
                c4 = (all([v in respostas['EST07'] for v in self.qualificadores["GovTec6"][13:15]]) and
                      any([v in respostas['EST07'] for v in self.qualificadores["GovTec6"][15:]]))
                if c1 and c2 and c3 and c4:  # Critério soma e grupo de qualificadores
                    return True
                return False
            case 7:
                c1 = soma(respostas=respostas, universo=self.universo) in self.limite['GovTec7']
                c2 = (any([v in respostas['EST05'] for v in self.qualificadores["GovTec7"][:3]]) and
                      any([v in respostas['EST07'] for v in self.qualificadores["GovTec7"][3:6]]))
                c3 = all([v in respostas['EST05']
                         for v in self.qualificadores["GovTec7"][6:13]])
                c4 = all([v in respostas['EST07']
                         for v in self.qualificadores["GovTec7"][13:]])
                if c1 and c2 and c3 and c4:  # Critério soma e grupo de qualificadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class SegPol():
    def __init__(self):
        self.componente = "SegPol"
        self.nivel_inicial = "1"
        self.fixadores = {"SegPol1": ["EST06.a"],
                          "SegPol2": ["EST06.b"],
                          "SegPol3": ["EST06.c"],
                          "SegPol4": ["EST06.d"],
                          "SegPol5": ["EST06.e"],
                          "SegPol6": ["EST06.f"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol1"]]):  # Critério fixadores
                    return True
                return False
            case 2:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol2"]]):  # Critério fixadores
                    return True
                return False
            case 3:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol3"]]):  # Critério fixadores
                    return True
                return False
            case 4:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                if all([v in respostas["EST06"] for v in self.fixadores["SegPol6"]]):  # Critério fixadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class Vis():
    def __init__(self):
        self.componente = "Vis"
        self.nivel_inicial = "2"
        self.fixadores = {"Vis2": ["EST09.a", "EST09.e"],
                          "Vis3": ["EST09.c"],
                          "Vis4": ["EST09.b"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 2:
                if all([v in respostas["EST09"] for v in self.fixadores["Vis2"]]):  # Critério fixadores
                    return True
                return False
            case 3:
                if all([v in respostas["EST09"] for v in self.fixadores["Vis3"]]):  # Critério fixadores
                    return True
                return False
            case 4:
                if all([v in respostas["EST09"] for v in self.fixadores["Vis4"]]):  # Critério fixadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(2, 5):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


# Infraestrutura
class ITPlan():
    def __init__(self):
        self.componente = "ITPlan"
        self.nivel_inicial = "1"
        self.fixadores = {"ITPlan1": ["INF05.b"],
                          "ITPlan3": ["INF05.1.b"],
                          "ITPlan4": ["INF05.a", "INF05.2.b"],
                          "ITPlan5": ["INF05.2.a", "INF05.3.b", "INF05.4.b"],
                          "ITPlan6": ["INF05.3.a", "INF05.4.a", "INF05.5.b"],
                          "ITPlan7": ["INF05.5.a"]}
        self.qualificadores = {"ITPlan2": ["INF05.1.a"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if any([v in respostas["INF05"] for v in self.fixadores["ITPlan1"]]):  # Critério fixadores
                    return True
                return False
            case 2:
                if any([v in respostas["INF05.1"] for v in self.qualificadores["ITPlan2"][0]]):  # Critério qualificadores
                    return True
                return False
            case 3:
                if all([v in respostas["INF05.1"] for v in self.fixadores["ITPlan3"]]):  # Critério fixador
                    return True
                return False
            case 4:
                if any([v in respostas["INF05"] for v in self.fixadores["ITPlan4"]]) and \
                        any([v in respostas["INF05.2"] for v in self.fixadores["ITPlan4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if any([v in respostas["INF05.2"] for v in self.fixadores["ITPlan5"]]) and \
                        any([v in respostas["INF05.3"] for v in self.fixadores["ITPlan5"]]) and \
                        any([v in respostas["INF05.4"] for v in self.fixadores["ITPlan5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                if any([v in respostas["INF05.3"] for v in self.fixadores["ITPlan6"]]) and \
                        any([v in respostas["INF05.4"] for v in self.fixadores["ITPlan6"]]) and \
                        any([v in respostas["INF05.5"] for v in self.fixadores["ITPlan6"]]):  # Critério fixadores
                    return True
                return False
            case 7:
                if all([v in respostas["INF05.5"] for v in self.fixadores["ITPlan7"]]):  # Critério fixador
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class Inst():
    def __init__(self):
        self.componente = "Inst"
        self.nivel_inicial = "1"
        self.fixadores = {}
        self.qualificadores = {"Inst1": ["INF01.b", "INF01.c"],
                               "Inst2": ["INF01.1.a"],
                               "Inst3": ["INF01.1.b"],
                               "Inst4": ["INF01.a"],
                               "Inst5": ["INF01.a"],
                               "Inst6": ["INF01.a"],
                               "Inst7": ["INF01.a"]}
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

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if soma(respostas=respostas, universo=self.universo) in [0, 1] and \
                        any([v in respostas["INF01"] for v in self.qualificadores["Inst1"]]):
                    return True
                return False
            case 2:
                if soma(respostas=respostas, universo=self.universo) in [2, 3] and \
                        any([v in respostas["INF01.1"] for v in self.qualificadores["Inst2"]]):
                    return True
                return False
            case 3:
                if soma(respostas=respostas, universo=self.universo) in [4, 5] and \
                        any([v in respostas["INF01.1"] for v in self.qualificadores["Inst3"]]):
                    return True
                return False
            case 4:
                if soma(respostas=respostas, universo=self.universo) in [6, 7] and \
                        any([v in respostas["INF01"] for v in self.qualificadores["Inst4"]]):
                    return True
                return False
            case 5:
                if soma(respostas=respostas, universo=self.universo) in [8, 9] and \
                        any([v in respostas["INF01"] for v in self.qualificadores["Inst5"]]):
                    return True
                return False
            case 6:
                if soma(respostas=respostas, universo=self.universo) in [10, 11] and \
                        any([v in respostas["INF01"] for v in self.qualificadores["Inst6"]]):
                    return True
                return False
            case 7:
                if soma(respostas=respostas, universo=self.universo) >= 12 and \
                        all([v in respostas["INF01"] for v in self.qualificadores["Inst7"]]):
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class IUPlan():
    def __init__(self):
        self.componente = "IUPlan"
        self.nivel_inicial = "1"
        idc_4005 = 0
        idc_4031 = 0
        idc_4041 = 0
        idc_4046 = 0
        idc_3122 = 0
        self.indices = {"4005": idc_4005,
                        "4031": idc_4031,
                        "4041": idc_4041,
                        "4046": idc_4046,
                        "3122": idc_3122}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if int(respostas["INF4005"]) <= 45:
                    return True
                return False
            case 2:
                if respostas["INF4005"] > 45 and respostas["INF4005"] <= 78:
                    return True
                return False
            case 3:
                if respostas["INF4005"] >= 79 and respostas["INF4005"] <= 81:
                    return True
                return False
            case 4:
                if respostas["INF4005"] >= 82 and respostas["INF4005"] <= 87:
                    return True
                return False
            case 5:
                c1 = respostas["INF4005"] >= 88 and respostas["INF4005"] <= 93
                c2 = respostas["INF4041"] == "Sim"
                c3 = respostas["INF4031"] == "Sim"
                c4 = respostas["INF4046"] == "Sim"
                if c1 and c2 and c3 and c4:
                    return True
                return False
            case 6:
                c1 = respostas["INF4005"] >= 94 and respostas["INF4005"] <= 99
                c2 = respostas["INF4041"] == "Sim"
                c3 = respostas["INF4031"] == "Sim"
                c4 = respostas["INF4046"] == "Sim"
                if c1 and c2 and c3 and c4:
                    return True
                return False
            case 7:
                c1 = respostas["INF4005"] > 99
                c2 = respostas["INF4041"] == "Sim"
                c3 = respostas["INF4031"] == "Sim"
                c4 = respostas["INF4046"] == "Sim"
                c5 = respostas["INF3122"] == "Sim"
                if c1 and c2 and c3 and c4 and c5:
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class AQua():
    def __init__(self):
        self.componente = "AQua"
        self.nivel_inicial = "1"

        # idc_3017 = 0
        # idc_3077 = 0
        # idc_3110 = 0
        # idc_3117 = 0
        # idc_3124 = 0
        # idc_3127 = 0

        # respostas = {"3027": idc_3017,
        #                 "3077": idc_3077,
        #                 "3110": idc_3110,
        #                 "3117": idc_3117,
        #                 "3124": idc_3124,
        #                 "3127": idc_3127}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                c1 = respostas["INF3027"] <= 35
                c2 = respostas["INF3117"] <= 35
                c3 = respostas["INF3127"] <= 35
                c4 = respostas["INF3110"] == "nan"
                c5 = respostas["INF3124"] <= 1
                c6 = respostas["INF3077"] <= 3
                if c1 and c2 and c3 and c4 and c5 and c6:
                    return True
                return False
            case 2:
                c1 = respostas["INF3027"] > 35 and respostas["INF3027"] <= 56
                c2 = respostas["INF3117"] > 35 and respostas["INF3117"] <= 56
                c3 = respostas["INF3127"] > 35 and respostas["INF3127"] <= 56
                c4 = respostas["INF3110"] == "nan"
                c5 = respostas["INF3124"] >= 2
                c6 = respostas["INF3077"] >= 3
                if c1 and c2 and c3 and c4 and c5 and c6:
                    return True
                return False
            case 3:
                c1 = respostas["INF3027"] > 56 and respostas["INF3027"] <= 78
                c2 = respostas["INF3117"] > 56 and respostas["INF3117"] <= 78
                c3 = respostas["INF3127"] > 56 and respostas["INF3127"] <= 78
                c4 = respostas["INF3110"] <= 44
                c5 = respostas["INF3124"] >= 3
                c6 = respostas["INF3077"] >= 7
                if c1 and c2 and c3 and c4 and c5 and c6:
                    return True
                return False
            case 4:
                c1 = respostas["INF3027"] > 79 and respostas["INF3027"] <= 87
                c2 = respostas["INF3117"] > 79 and respostas["INF3117"] <= 87
                c3 = respostas["INF3127"] > 79 and respostas["INF3127"] <= 87
                c4 = respostas["INF3110"] <= 38
                c5 = respostas["INF3124"] >= 4
                c6 = respostas["INF3077"] >= 9
                if c1 and c2 and c3 and c4 and c5 and c6:
                    return True
                return False
            case 5:
                c1 = respostas["INF3027"] > 88 and respostas["INF3027"] <= 100
                c2 = respostas["INF3117"] > 88 and respostas["INF3117"] <= 100
                c3 = respostas["INF3127"] > 88 and respostas["INF3127"] <= 100
                c4 = respostas["INF3110"] <= 32
                c5 = respostas["INF3124"] >= 6
                c6 = respostas["INF3077"] >= 13
                if c1 and c2 and c3 and c4 and c5 and c6:
                    return True
                return False
            case 6:
                c1 = respostas["INF3027"] == 100
                c2 = respostas["INF3117"] == 100
                c3 = respostas["INF3127"] == 100
                c4 = respostas["INF3110"] <= 21
                c5 = respostas["INF3124"] >= 7
                c6 = respostas["INF3077"] >= 16
                if c1 and c2 and c3 and c4 and c5 and c6:
                    return True
                return False
            case 7:
                c1 = respostas["INF3027"] == 100
                c2 = respostas["INF3117"] == 100
                c3 = respostas["INF3127"] == 100
                c4 = respostas["INF3110"] <= 1
                c5 = respostas["INF3124"] >= 9
                c6 = respostas["INF3077"] >= 18
                if c1 and c2 and c3 and c4 and c5 and c6:
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class HwSw():
    def __init__(self):
        self.componente = "HwSw"
        self.nivel_inicial = "1"
        self.fixadores = {}
        self.qualificadores = {"HwSw1": ["INF03.j", "INF03.k", "INF04.g"],
                               "HwSw2": ["INF03.j", "INF03.k", "INF04.f"],
                               "HwSw3": ["INF03.j", "INF03.k", "INF04.e"],
                               "HwSw4": ["INF03.j", "INF03.k", "INF04.d"],
                               "HwSw5": ["INF03.j", "INF03.k", "INF04.c"],
                               "HwSw6": ["INF03.j", "INF03.k", "INF04.b"],
                               "HwSw7": ["INF03.j", "INF03.k", "INF04.a"]}
        self.universo = {
            "INF03.a": 1,
            "INF03.b": 1,
            "INF03.c": 1,
            "INF03.d": 1,
            "INF03.e": 1,
            "INF03.f": 1,
            "INF03.g": 1,
            "INF03.h": 1,
            "INF03.i": 1
        }

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if soma(respostas=respostas, universo=self.universo) < 9 and \
                    not any([v in respostas["INF03"] for v in self.qualificadores["HwSw1"][:2]]) and \
                        self.qualificadores["HwSw1"][2] in respostas["INF04"]:
                    return True
                return False
            case 2:
                if soma(respostas=respostas, universo=self.universo) < 9 and \
                    not any([v in respostas["INF03"] for v in self.qualificadores["HwSw2"][:2]]) and \
                        self.qualificadores["HwSw2"][2] in respostas["INF04"]:
                    return True
                return False
            case 3:
                if soma(respostas=respostas, universo=self.universo) < 9 and \
                    not any([v in respostas["INF03"] for v in self.qualificadores["HwSw3"][:2]]) and \
                        self.qualificadores["HwSw3"][2] in respostas["INF04"]:
                    return True
                return False
            case 4:
                if soma(respostas=respostas, universo=self.universo) == 9 and \
                        self.qualificadores["HwSw4"][0] in respostas["INF03"] and \
                        self.qualificadores["HwSw4"][1] not in respostas["INF03"] and \
                        self.qualificadores["HwSw4"][2] in respostas["INF04"]:
                    return True
                return False
            case 5:
                if soma(respostas=respostas, universo=self.universo) == 9 and \
                        all([v in respostas["INF03"] for v in self.qualificadores["HwSw5"]]) and \
                        self.qualificadores["HwSw5"][2] in respostas["INF04"]:
                    return True
                return False
            case 6:
                if soma(respostas=respostas, universo=self.universo) == 9 and \
                        all([v in respostas["INF03"] for v in self.qualificadores["HwSw6"]]) and \
                        self.qualificadores["HwSw6"][2] in respostas["INF04"]:
                    return True
                return False
            case 7:
                if soma(respostas=respostas, universo=self.universo) == 9 and \
                        all([v in respostas["INF03"] for v in self.qualificadores["HwSw7"]]) and \
                        self.qualificadores["HwSw7"][2] in respostas["INF04"]:
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class GovTI():
    def __init__(self):
        self.componente = "GovTI"
        self.nivel_inicial = "4"
        self.fixadores = {"GovTI4": ["INF01.4.a"],
                          "GovTI5": ["INF01.4.b"],
                          "GovTI6": ["INF01.4.c"],
                          "GovTI7": ["INF01.4.d"]}
        self.qualificadores = {}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 4:
                if self.fixadores["GovTI4"][0] in respostas["INF01.4"]:  # Critério fixador
                    return True
                return False
            case 5:
                if self.fixadores["GovTI5"][0] in respostas["INF01.4"]:  # Critério fixador
                    return True
                return False
            case 6:
                if self.fixadores["GovTI6"][0] in respostas["INF01.4"]:  # Critério fixador
                    return True
                return False
            case 7:
                if self.fixadores["GovTI7"][0] in respostas["INF01.4"]:  # Critério fixador
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(4, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


# DADOS
class DPlan():
    def __init__(self):
        self.componente = "DPlan"
        self.nivel_inicial = "1"
        self.fixadores = {"DPlan1": ["DAD03.g"],
                          "DPlan2": ["DAD03.f"],
                          "DPlan3": ["DAD03.e"]}
        self.qualificadores = {"DPlan4": ["DAD03.d", "DAD03.a"],
                               "DPlan5": ["DAD03.c", "DAD03.a"],
                               "DPlan6": ["DAD03.b", "DAD08.a"],
                               "DPlan7": ["DAD03.a", "DAD08.a"]}
        self.universo1 = {
            "DAD04.a": 1,
            "DAD04.b": 1,
            "DAD04.c": 1,
            "DAD04.d": 1,
            "DAD04.e": 1,
            "DAD04.f": 1,
            "DAD04.g": 1,
            "DAD04.h": 1,
            "DAD04.i": 0
        }
        self.universo2 = {
            "DAD09.a": 1,
            "DAD09.b": 1,
            "DAD09.c": 1,
            "DAD09.d": 1,
            "DAD09.e": 1
        }

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if self.fixadores["DPlan1"][0] in respostas["DAD03"]:  # Critério fixador
                    return True
                return False
            case 2:
                if self.fixadores["DPlan2"][0] in respostas["DAD03"]:  # Critério fixador
                    return True
                return False
            case 3:
                if self.fixadores["DPlan3"][0] in respostas["DAD03"]:  # Critério fixador
                    return True
                return False
            case 4:
                if soma(respostas=respostas, universo=self.universo1) >= 3 and \
                        self.qualificadores["DPlan4"] in respostas["DAD03"]:  # Critério soma e qualificador
                    return True
                return False
            case 5:
                if soma(respostas=respostas, universo=self.universo1) >= 3 and \
                        self.qualificadores["DPlan5"] in respostas["DAD03"]:  # Critério soma e qualificador
                    return True
                return False
            case 6:
                if soma(respostas=respostas, universo=self.universo1) >= 5 and \
                        soma(respostas=respostas, universo=self.universo2) >= 1 and \
                        self.qualificadores["DPlan6"] in respostas["DAD03"] and \
                        self.qualificadores["DPlan6"] in respostas["DAD08"]:  # Critério soma e qualificadores
                    return True
                return False
            case 7:
                if soma(respostas=respostas, universo=self.universo1) >= 7 and \
                        soma(respostas=respostas, universo=self.universo2) >= 2 and \
                        self.qualificadores["DPlan7"] in respostas["DAD03"] and \
                        self.qualificadores["DPlan7"] in respostas["DAD08"]:  # Critério soma e qualificadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class Digi():
    def __init__(self):
        self.componente = "Digi"
        self.nivel_inicial = "1"
        self.fixadores = {}
        self.qualificadores = {}
        self.universo = {
            "DAD01.aa": 2,
            "DAD01.ab": 1,
            "DAD01.ac": 0,
            "DAD01.ba": 2,
            "DAD01.bb": 1,
            "DAD01.bc": 0,
            "DAD01.ca": 2,
            "DAD01.cb": 1,
            "DAD01.cc": 0,
            "DAD01.da": 2,
            "DAD01.db": 1,
            "DAD01.dc": 0,
            "DAD01.ea": 2,
            "DAD01.eb": 1,
            "DAD01.ec": 0,
            "DAD01.fa": 2,
            "DAD01.fb": 1,
            "DAD01.fc": 0,
            "DAD01.ga": 2,
            "DAD01.gb": 1,
            "DAD01.gc": 0,
            "DAD01.ha": 2,
            "DAD01.hb": 1,
            "DAD01.hc": 0,
            "DAD01.ia": 2,
            "DAD01.ib": 1,
            "DAD01.ic": 0,
            "DAD01.ja": 2,
            "DAD01.jb": 1,
            "DAD01.jc": 0,
            "DAD01.ka": 2,
            "DAD01.kb": 1,
            "DAD01.kc": 0,
            "DAD01.la": 2,
            "DAD01.lb": 1,
            "DAD01.lc": 0
        }

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if soma(respostas=respostas, universo=self.universo) <= 7:
                    return True
                return False
            case 2:
                if soma(respostas=respostas, universo=self.universo) in list(range(8, 11)):
                    return True
                return False
            case 3:
                if soma(respostas=respostas, universo=self.universo) > 10:
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 4):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class DTransp():
    def __init__(self):
        self.componente = "DTransp"
        self.nivel_inicial = "1"
        self.fixadores = {"DTransp1": ["DAD05.a"]}
        self.qualificadores = {"DTransp2": ["DAD05.b", "DAD05.a", "DAD06.b"],
                               "DTransp3": ["DAD05.c", "DAD06.a", "DAD06.b"],
                               "DTransp4": ["DAD05.d", "DAD06.a", "DAD06.b"],
                               "DTransp5": ["DAD05.d", "DAD06.a", "DAD06.b", "DAD07.a", "DAD07.b", "DAD07.c"],
                               "DTransp6": ["DAD05.d", "DAD06.a", "DAD07.b"],
                               "DTransp7": ["DAD05.d", "DAD06.a", "DAD07.a"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if self.fixadores["DTransp1"][0] in respostas["DAD05"]:  # Critério fixador
                    return True
                return False
            case 2:
                c1 = self.qualificadores["DTransp2"][0] in respostas["DAD05"]
                c2 = any([v in respostas["DAD06"] for v in self.qualificadores["DTransp2"][1:]])
                if c1 and c2:  # Critério duplo qualificadores
                    return True
                return False
            case 3:
                c1 = self.qualificadores["DTransp3"][0] in respostas["DAD05"]
                c2 = any([v in respostas["DAD06"] for v in self.qualificadores["DTransp3"][1:]])
                if c1 and c2:  # Critério duplo qualificadores
                    return True
                return False
            case 4:
                c1 = self.qualificadores["DTransp4"][0] in respostas["DAD05"]
                c2 = any([v in respostas["DAD06"] for v in self.qualificadores["DTransp4"][1:]])
                if c1 and c2:  # Critério duplo qualificadores
                    return True
                return False
            case 5:
                c1 = self.qualificadores["DTransp5"][0] in respostas["DAD05"]
                c2 = any([v in respostas["DAD06"] for v in self.qualificadores["DTransp3"][1:3]])
                c3 = any([v in respostas["DAD07"] for v in self.qualificadores["DTransp3"][3:]])
                if c1 and c2 and c3:  # Critério triplo qualificadores
                    return True
                return False
            case 6:
                c1 = self.qualificadores["DTransp6"][0] in respostas["DAD05"]
                c2 = self.qualificadores["DTransp6"][1] in respostas["DAD06"]
                c3 = self.qualificadores["DTransp6"][2] in respostas["DAD07"]
                if c1 and c2 and c3:  # Critério triplo qualificadores
                    return True
                return False
            case 7:
                c1 = self.qualificadores["DTransp7"][0] in respostas["DAD05"]
                c2 = self.qualificadores["DTransp7"][1] in respostas["DAD06"]
                c3 = self.qualificadores["DTransp7"][2] in respostas["DAD07"]
                if c1 and c2 and c3:  # Critério triplo qualificadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class DInteg():
    def __init__(self):
        self.componente = "DInteg"
        self.nivel_inicial = "4"

        self.fixadores = {f"{self.componente}4": ["DAD02.d"],
                          f"{self.componente}5": ["DAD02.c"],
                          f"{self.componente}6": ["DAD02.b"],
                          f"{self.componente}7": ["DAD02.a"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 4:
                if self.fixadores[f"{self.componente}4"][0] in respostas["DAD02"]:  # Critério fixador
                    return True
                return False
            case 5:
                if self.fixadores[f"{self.componente}5"][0] in respostas["DAD02"]:  # Critério fixador
                    return True
                return False
            case 6:
                if self.fixadores[f"{self.componente}6"][0] in respostas["DAD02"]:  # Critério fixador
                    return True
                return False
            case 7:
                if self.fixadores[f"{self.componente}7"][0] in respostas["DAD02"]:  # Critério fixador
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(4, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


# Serviços e Aplicações
class SPlan():
    def __init__(self):
        self.componente = "SPlan"
        self.nivel_inicial = "1"

        self.fixadores = {f"{self.componente}1": ["SERV07.b", "SERV07.c"]}
        self.qualificadores = {f"{self.componente}2": ["SERV07.a", "SERV07.1.a"],
                               f"{self.componente}3": ["SERV07.a", "SERV07.1.b"],
                               f"{self.componente}4": ["SERV07.a", "SERV07.1.c"],
                               f"{self.componente}5": ["SERV07.a", "SERV07.1.c", "SERV07.1.d"],
                               f"{self.componente}6": ["SERV07.a", "SERV07.1.c", "SERV07.1.d", "SERV07.1.e", "SERV07.1.f"],
                               f"{self.componente}7": ["SERV07.a", "SERV07.1.c", "SERV07.1.d",
                                                       "SERV07.1.e", "SERV07.1.f", "SERV07.1.g", "SERV07.1.h"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if any([v in respostas["SERV07"] for v in self.fixadores[f"{self.componente}1"]]):  # Critério fixadores
                    return True
                return False
            case 2:
                if all([v in respostas["SERV07"] for v in self.qualificadores[f"{self.componente}2"]]):  # Critério fixadores
                    return True
                return False
            case 3:
                if all([v in respostas["SERV07"] for v in self.qualificadores[f"{self.componente}3"]]):  # Critério fixadores
                    return True
                return False
            case 4:
                if all([v in respostas["SERV07"] for v in self.qualificadores[f"{self.componente}4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if all([v in respostas["SERV07"] for v in self.qualificadores[f"{self.componente}5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                if all([v in respostas["SERV07"] for v in self.qualificadores[f"{self.componente}6"]]):  # Critério fixadores
                    return True
                return False
            case 7:
                if all([v in respostas["SERV07"] for v in self.qualificadores[f"{self.componente}7"]]):  # Critério fixadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class SUrb():
    def __init__(self):
        self.componente = "SUrb"
        self.nivel_inicial = "1"
        # idc_3127 = 0
        # idc_3117 = 0
        # idc_4006 = 0
        # idc_4024 = 0
        # idc_4039 = 0
        # respostas = {"3127": idc_3127,
        #              "3117": idc_3117,
        #              "4006": idc_4006,
        #              "4024": idc_4024,
        #              "4039": idc_4039}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                c1 = respostas["SERV3127"] > 0 and respostas["SERV3127"] < 36
                c2 = respostas["SERV3117"] > 0 and respostas["SERV3127"] < 36
                if c1 and c2:
                    return True
                return False
            case 2:
                c1 = respostas["SERV3127"] >= 36 and respostas["SERV3127"] < 56
                c2 = respostas["SERV3117"] >= 36 and respostas["SERV3127"] < 56
                if c1 and c2:
                    return True
                return False
            case 3:
                c1 = respostas["SERV3127"] >= 56 and respostas["SERV3127"] < 79
                c2 = respostas["SERV3117"] >= 56 and respostas["SERV3127"] < 79
                if c1 and c2:
                    return True
                return False
            case 4:
                c1 = respostas["SERV3127"] >= 78 and respostas["SERV3127"] < 88
                c2 = respostas["SERV3117"] >= 78 and respostas["SERV3127"] < 88
                c3 = respostas["SERV4024"] == "Sim"
                if c1 and c2 and c3:
                    return True
                return False
            case 5:
                c1 = respostas["SERV3127"] >= 88 and respostas["SERV3127"] < 93
                c2 = respostas["SERV3117"] >= 88 and respostas["SERV3127"] < 93
                c3 = respostas["SERV4024"] == "Sim"
                c4 = respostas["SERV4039"] == "Sim"
                if c1 and c2 and c3 and c4:
                    return True
                return False
            case 6:
                c1 = respostas["SERV3127"] >= 93 and respostas["SERV3127"] < 99
                c2 = respostas["SERV3117"] >= 93 and respostas["SERV3127"] < 99
                c3 = respostas["SERV4024"] == "Sim"
                c4 = respostas["SERV4039"] == "Sim"
                c5 = respostas["SERV4006"] == "Sim"
                if c1 and c2 and c3 and c4 and c5:
                    return True
                return False
            case 7:
                c1 = respostas["SERV3127"] >= 99
                c2 = respostas["SERV3117"] >= 99
                c3 = respostas["SERV4024"] == "Sim"
                c4 = respostas["SERV4039"] == "Sim"
                c5 = respostas["SERV4006"] == "Sim"
                if c1 and c2 and c3 and c4 and c5:
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(1, 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class SOn():
    def __init__(self):
        self.componente = "SOn"
        self.nivel_inicial = "1"

        cq11 = ["SERV01.ag", "SERV01.ah", "SERV01.bg",
                "SERV01.bh", "SERV01.cg", "SERV01.ch",
                "SERV01.dg", "SERV01.dh", "SERV01.eg",
                "SERV01.eh", "SERV01.fg", "SERV01.fh",
                "SERV01.gg", "SERV01.gh", "SERV01.hg",
                "SERV01.hh", "SERV01.ig", "SERV01.ih",
                "SERV01.jg", "SERV01.jh", "SERV01.kg",
                "SERV01.kh", "SERV01.lg", "SERV01.lh"]

        cq12 = ["SERV01.ae", "SERV01.af", "SERV01.be",
                "SERV01.bf", "SERV01.cfe", "SERV01.cf",
                "SERV01.de", "SERV01.df", "SERV01.ee",
                "SERV01.ef", "SERV01.fe", "SERV01.ff",
                "SERV01.ge", "SERV01.gf", "SERV01.he",
                "SERV01.hf", "SERV01.ie", "SERV01.if",
                "SERV01.je", "SERV01.jf", "SERV01.ke",
                "SERV01.kf", "SERV01.le", "SERV01.lf"]

        cq13 = ["SERV01.ad", "SERV01.bd", "SERV01.cd",
                "SERV01.dd", "SERV01.ed", "SERV01.fd",
                "SERV01.gd", "SERV01.hd", "SERV01.id",
                "SERV01.jd", "SERV01.kd", "SERV01.ld"]

        cq14 = ["SERV01.ad", "SERV01.ae", "SERV01.bd",
                "SERV01.be", "SERV01.cd", "SERV01.ce",
                "SERV01.dd", "SERV01.de", "SERV01.ed",
                "SERV01.ee", "SERV01.fd", "SERV01.fe"
                "SERV01.gd", "SERV01.ge", "SERV01.hd",
                "SERV01.he", "SERV01.id", "SERV01.ie",
                "SERV01.jd", "SERV01.je", "SERV01.kd",
                "SERV01.ke", "SERV01.ld", "SERV01.le"]

        cq15 = ["SERV01.ac", "SERV01.ad", "SERV01.bc",
                "SERV01.bd", "SERV01.cc", "SERV01.cd",
                "SERV01.dc", "SERV01.dd", "SERV01.ec",
                "SERV01.ed", "SERV01.fc", "SERV01.fd",
                "SERV01.gc", "SERV01.gd", "SERV01.hc",
                "SERV01.hd", "SERV01.ic", "SERV01.icd",
                "SERV01.jc", "SERV01.jd", "SERV01.kc",
                "SERV01.kd", "SERV01.lc", "SERV01.ld"]

        cq16 = ["SERV01.ab", "SERV01.bb", "SERV01.cb",
                "SERV01.db", "SERV01.eb", "SERV01.fb",
                "SERV01.gb", "SERV01.hb", "SERV01.ib",
                "SERV01.jb", "SERV01.kb", "SERV01.lb"
                ]

        cq2 = ["SERV02.a", "SERV02.b", "SERV02.c", "SERV02.d",
               "SERV02.e", "SERV02.f", "SERV02.g", "SERV02.h"]

        cq3 = ["SERV03.a", "SERV03.b", "SERV03.c", "SERV03.d",
               "SERV03.e", "SERV03.f", "SERV03.g", "SERV03.h",
               "SERV03.i", "SERV03.j", "SERV03.k", "SERV03.l"]

        self.qualificadores = {f"{self.componente}1": {'cq1': cq11, 'cq2': cq2, 'cq3': cq3},
                               f"{self.componente}2": {'cq1': cq12, 'cq2': cq2, 'cq3': cq3},
                               f"{self.componente}3": {'cq1': cq13, 'cq2': cq2, 'cq3': cq3},
                               f"{self.componente}4": {'cq1': cq14, 'cq2': cq2, 'cq3': cq3},
                               f"{self.componente}5": {'cq1': cq15, 'cq2': cq2, 'cq3': cq3},
                               f"{self.componente}6": {'cq1': cq16, 'cq2': cq2, 'cq3': cq3}}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}1"]["cq1"]]) >= 3
                c2 = not any([v in respostas["SERV02"] for v in self.qualificadores[f"{self.componente}1"]["cq2"]])
                c3 = not any([v in respostas["SERV03"] for v in self.qualificadores[f"{self.componente}1"]["cq3"]])
                c4 = "SERV04.a" in respostas["SERV04"]
                c5 = "SERV05.b" in respostas["SERV05"] and "SERV05.c" in respostas["SERV05"]
                if c1 and c2 and c3 and c4 and c5:  # Critério triplo qualificadores
                    return True
                return False
            case 2:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}1"]["cq1"]]) >= 3
                c2 = sum([v in respostas["SERV02"] for v in self.qualificadores[f"{self.componente}1"]["cq2"]]) >= 1
                c3 = "SERV03.e" in respostas["SERV03"] and "SERV03.f" in respostas["SERV03"]
                c4 = "SERV04.a" in respostas["SERV04"] and "SERV04.b" in respostas["SERV04"]
                c5 = "SERV05.a" in respostas["SERV05"] and "SERV05.1.a" in respostas["SERV05.1"]
                if c1 and c2 and c3 and c4 and c5:  # Critério triplo qualificadores
                    return True
                return False
            case 3:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}1"]["cq1"]]) >= 3
                c2 = sum([v in respostas["SERV02"] for v in self.qualificadores[f"{self.componente}1"]["cq2"]]) in list(range(2, 5))
                c3 = "SERV03.b" in respostas["SERV03"] and "SERV03.i" in respostas["SERV03"]
                c4 = "SERV04.a" in respostas["SERV04"] and "SERV04.b" in respostas["SERV04"]
                c5 = "SERV05.a" in respostas["SERV05"] and "SERV05.1.a" in respostas["SERV05.1"] and "SERV05.1.b" in respostas["SERV05.1"]
                if c1 and c2 and c3 and c4 and c5:  # Critério triplo qualificadores
                    return True
                return False
            case 4:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}1"]["cq1"]]) >= 3
                c2 = sum([v in respostas["SERV02"] for v in self.qualificadores[f"{self.componente}1"]["cq2"]]) >= 5
                c3a = "SERV03.c" in respostas["SERV03"] and "SERV03.h" in respostas["SERV03"]
                c3b = "SERV03.c" in respostas["SERV03"] and "SERV03.j" in respostas["SERV03"]
                c3c = "SERV03.h" in respostas["SERV03"] and "SERV03.j" in respostas["SERV03"]
                c3 = c3a or c3b or c3c
                c4 = "SERV04.a" in respostas["SERV04"] and "SERV04.b" in respostas["SERV04"] and "SERV04.e" in respostas["SERV04"]
                c5 = "SERV05.a" in respostas["SERV05"] and "SERV05.1.a" in respostas["SERV05.1"] and "SERV05.1.b" in respostas["SERV05.1"] and \
                    "SERV05.1.c" in respostas["SERV05.1"]
                if c1 and c2 and c3 and c4 and c5:  # Critério triplo qualificadores
                    return True
                return False
            case 5:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}1"]["cq1"]]) >= 3
                c2 = sum([v in respostas["SERV02"] for v in self.qualificadores[f"{self.componente}1"]["cq2"]]) >= 5
                c3 = "SERV03.g" in respostas["SERV03"] or "SERV03.a" in respostas["SERV03"]
                c4 = "SERV04.a" in respostas["SERV04"] and "SERV04.b" in respostas["SERV04"] and \
                    "SERV04.e" in respostas["SERV04"] and "SERV04.f" in respostas["SERV04"]
                c5 = "SERV05.a" in respostas["SERV05"] and "SERV05.1.a" in respostas["SERV05.1"] and \
                    "SERV05.1.b" in respostas["SERV05.1"] and "SERV05.1.c" in respostas["SERV05.1"] and "SERV05.1.d" in respostas["SERV05.1"]
                if c1 and c2 and c3 and c4 and c5:  # Critério triplo qualificadores
                    return True
                return False
            case 6:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}1"]["cq1"]]) >= 3
                c2 = sum([v in respostas["SERV02"] for v in self.qualificadores[f"{self.componente}1"]["cq2"]]) >= 5
                c3 = "SERV03.a" in respostas["SERV03"]
                c4 = "SERV04.a" in respostas["SERV04"] and "SERV04.b" in respostas["SERV04"] and \
                    "SERV04.c" in respostas["SERV04"] and "SERV04.e" in respostas["SERV04"] and \
                    "SERV04.f" in respostas["SERV04"]
                c5 = "SERV05.a" in respostas["SERV05"] and "SERV05.1.a" in respostas["SERV05.1"] and \
                    "SERV05.1.b" in respostas["SERV05.1"] and "SERV05.1.c" in respostas["SERV05.1"] and "SERV05.1.d" in respostas["SERV05.1"]
                if c1 and c2 and c3 and c4 and c5:  # Critério triplo qualificadores
                    return True
                return False
            case 7:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}1"]["cq1"]]) >= 3
                c2 = sum([v in respostas["SERV02"] for v in self.qualificadores[f"{self.componente}1"]["cq2"]]) >= 5
                c3 = "SERV03.a" in respostas["SERV03"]
                c4 = "SERV04.a" in respostas["SERV04"] and "SERV04.b" in respostas["SERV04"] and \
                    "SERV04.c" in respostas["SERV04"] and "SERV04.e" in respostas["SERV04"] and \
                    "SERV04.f" in respostas["SERV04"]
                c5 = "SERV05.a" in respostas["SERV05"] and "SERV05.1.a" in respostas["SERV05.1"] and \
                    "SERV05.1.b" in respostas["SERV05.1"] and "SERV05.1.c" in respostas["SERV05.1"] and "SERV05.1.d" in respostas["SERV05.1"]
                if c1 and c2 and c3 and c4 and c5:  # Critério triplo qualificadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class SInteg():
    def __init__(self):
        self.componente = "SInteg"
        self.nivel_inicial = "1"
        self.fixadores = {f"{self.componente}1": ["SERV06.b", "SERV06.c"]}

        cq1 = ["SERV01.ab", "SERV01.bb", "SERV01.cb",
               "SERV01.db", "SERV01.eb", "SERV01.fb",
               "SERV01.gb", "SERV01.hb", "SERV01.ib",
               "SERV01.jb", "SERV01.kb", "SERV01.lb"]

        cq2 = ["SERV01.aa", "SERV01.ba", "SERV01.ca",
               "SERV01.da", "SERV01.ea", "SERV01.fa",
               "SERV01.ga", "SERV01.ha", "SERV01.ia",
               "SERV01.ja", "SERV01.ka", "SERV01.la"]

        self.qualificadores = {f"{self.componente}2": ["SERV06.b", "SERV06.1.f"],
                               f"{self.componente}3": ["SERV06.b", "SERV06.1.e"],
                               f"{self.componente}4": ["SERV06.b", "SERV06.1.d"],
                               f"{self.componente}5": ["SERV06.b", "SERV06.1.c"],
                               f"{self.componente}6": cq1,
                               f"{self.componente}7": cq2}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if any([v in respostas["SERV06"] for v in self.fixadores[f"{self.componente}1"]]):  # Critério fixadores
                    return True
                return False
            case 2:
                if all([v in respostas["SERV06"] for v in self.qualificadores[f"{self.componente}2"]]):  # Critério fixadores
                    return True
                return False
            case 3:
                if all([v in respostas["SERV06"] for v in self.qualificadores[f"{self.componente}3"]]):  # Critério fixadores
                    return True
                return False
            case 4:
                if all([v in respostas["SERV06"] for v in self.qualificadores[f"{self.componente}4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if all([v in respostas["SERV06"] for v in self.qualificadores[f"{self.componente}5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}6"]]) >= 2
                c2 = "SERV06.a" in respostas["SERV06"]
                c3 = "SERV06.1.b" in respostas["SERV06"]
                if c1 and c2 and c3:  # Critério triplo qualificadores
                    return True
                return False
            case 7:
                c1 = sum([v in respostas["SERV01"] for v in self.qualificadores[f"{self.componente}6"]]) >= 2
                c2 = "SERV06.a" in respostas["SERV06"]
                c3 = "SERV06.1.a" in respostas["SERV06"]
                if c1 and c2 and c3:  # Critério triplo qualificadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado

# Monitoramento


class MPlan():
    def __init__(self):
        self.componente = "MPlan"
        self.nivel_inicial = "1"
        self.fixadores = {f"{self.componente}1": ["MON01.a"],
                          f"{self.componente}2": ["MON01.b"],
                          f"{self.componente}3": ["MON01.c"],
                          f"{self.componente}4": ["MON01.d"],
                          f"{self.componente}5": ["MON01.e"],
                          f"{self.componente}6": ["MON01.f"],
                          f"{self.componente}7": ["MON01.g"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if any([v in respostas["MON01"] for v in self.fixadores[f"{self.componente}1"]]):  # Critério fixadores
                    return True
                return False
            case 2:
                if any([v in respostas["MON01"] for v in self.fixadores[f"{self.componente}2"]]):  # Critério fixadores
                    return True
                return False
            case 3:
                if any([v in respostas["MON01"] for v in self.fixadores[f"{self.componente}3"]]):  # Critério fixadores
                    return True
                return False
            case 4:
                if any([v in respostas["MON01"] for v in self.fixadores[f"{self.componente}4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if any([v in respostas["MON01"] for v in self.fixadores[f"{self.componente}5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                if any([v in respostas["MON01"] for v in self.fixadores[f"{self.componente}6"]]):  # Critério fixadores
                    return True
                return False
            case 7:
                if any([v in respostas["MON01"] for v in self.fixadores[f"{self.componente}7"]]):  # Critério fixadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class Coord():
    def __init__(self):
        self.componente = "Coord"
        self.nivel_inicial = "1"
        self.fixadores = {f"{self.componente}1": ["MON03.a"],
                          f"{self.componente}2": ["MON03.b"],
                          f"{self.componente}3": ["MON03.c"],
                          f"{self.componente}4": ["MON03.d"],
                          f"{self.componente}5": ["MON03.e"],
                          f"{self.componente}6": ["MON03.f"],
                          f"{self.componente}7": ["MON03.g"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 1:
                if any([v in respostas["MON03"] for v in self.fixadores[f"{self.componente}1"]]):  # Critério fixadores
                    return True
                return False
            case 2:
                if any([v in respostas["MON03"] for v in self.fixadores[f"{self.componente}2"]]):  # Critério fixadores
                    return True
                return False
            case 3:
                if any([v in respostas["MON03"] for v in self.fixadores[f"{self.componente}3"]]):  # Critério fixadores
                    return True
                return False
            case 4:
                if any([v in respostas["MON03"] for v in self.fixadores[f"{self.componente}4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if any([v in respostas["MON03"] for v in self.fixadores[f"{self.componente}5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                if any([v in respostas["MON03"] for v in self.fixadores[f"{self.componente}6"]]):  # Critério fixadores
                    return True
                return False
            case 7:
                if any([v in respostas["MON03"] for v in self.fixadores[f"{self.componente}7"]]):  # Critério fixadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class Perc():
    def __init__(self):
        self.componente = "Perc"
        self.nivel_inicial = "4"
        self.fixadores = {f"{self.componente}4": ["MON05.b"],
                          f"{self.componente}5": ["MON05.c"],
                          f"{self.componente}6": ["MON05.d"],
                          f"{self.componente}7": ["MON05.e"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 4:
                if any([v in respostas["MON05"] for v in self.fixadores[f"{self.componente}4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if any([v in respostas["MON05"] for v in self.fixadores[f"{self.componente}5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                if any([v in respostas["MON05"] for v in self.fixadores[f"{self.componente}6"]]):  # Critério fixadores
                    return True
                return False
            case 7:
                if any([v in respostas["MON05"] for v in self.fixadores[f"{self.componente}7"]]):  # Critério fixadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


class MTransp():
    def __init__(self):
        self.componente = "MTransp"
        self.nivel_inicial = "4"
        self.fixadores = {f"{self.componente}4": ["MON04.d"],
                          f"{self.componente}5": ["MON04.c"],
                          f"{self.componente}6": ["MON04.b"],
                          f"{self.componente}7": ["MON04.a"]}

    def verificador_interno(self, respostas, nivel):
        match nivel:
            case 4:
                if any([v in respostas["MON04"] for v in self.fixadores[f"{self.componente}4"]]):  # Critério fixadores
                    return True
                return False
            case 5:
                if any([v in respostas["MON04"] for v in self.fixadores[f"{self.componente}5"]]):  # Critério fixadores
                    return True
                return False
            case 6:
                if any([v in respostas["MON04"] for v in self.fixadores[f"{self.componente}6"]]):  # Critério fixadores
                    return True
                return False
            case 7:
                if any([v in respostas["MON04"] for v in self.fixadores[f"{self.componente}7"]]):  # Critério fixadores
                    return True
                return False

    def maturidade(self, respostas: dict):
        resultado = f"{self.componente}{self.nivel_inicial}"
        for nivel in range(int(self.nivel_inicial), 8):
            if self.verificador_interno(respostas=respostas, nivel=nivel):
                resultado = f"{self.componente}{nivel}"
        return resultado


def get_resp_mncp(caps: list, idx_mncp: int) -> dict:
    respostas = {}
    for cap in caps:
        respostas_municipios = extrator.get_capacidade(cap)
        # print("RESPOSTA MNCP ", cap, respostas_municipios[idx_mncp])
        respostas[cap] = respostas_municipios[idx_mncp]
    # respostas["municipio"] = respostas_municipios[idx_mncp]["municipio"]
    return respostas


if "__main__" == __name__:
    from Repostas import Resposta
    from Maturidade import Nivel

     
    # notas_est = extrator.get_capacidade('EST')
    # notas_inf = extrator.get_capacidade('INF')
    # notas_dad = extrator.get_capacidade('DAD')
    # notas_serv = extrator.get_capacidade('SERV')
    # notas_mon = extrator.get_capacidade('MON')

    # notas = [notas_est, notas_inf, notas_dad, notas_serv, notas_mon]
    extrator = Resposta()

    est = [EPlan(), GovCol(), GovTec(), SegPol(), Vis()]
    inf = [IUPlan(), AQua(), ITPlan(), Inst(), HwSw(), GovTI()] # Completo com indices
    # inf = [ITPlan(), Inst(), GovTI()]
    dad = [DPlan(), Digi(), DTransp(), DInteg()]
    serv = [SPlan(), SUrb(), SOn(), SInteg()] # Completo com indices
    # serv = [SPlan(), SOn(), SInteg()]
    mon = [MPlan(), Coord(), Perc(), MTransp()] 
    
    pontuadores_comps = {"EST": est,
                         "INF": inf,
                         "DAD": dad,
                         "SERV": serv,
                         "MON": mon}
    
    # nivel = {"EST": {},
    #     "INF": {},
    #     "DAD": {},
    #     "SERV": {},
    #     "MON": {},
    #     "municipio": ""}

    caps = ["EST", "INF", "DAD", "SERV", "MON"]

    lista_mncps = ['Cabeceira Grande (MG)', 'Cavalcante (GO)']
    verbose = True
    resultado_mncp = {}
    nivel_mncps = []
    # respostas_mncp = get_resp_mncp(caps=caps, idx_mncp=1)
    for nome_cap, pontuadores in pontuadores_comps.items():  # Coletando o pontuador
        respostas_municipios = extrator.get_capacidade(nome_cap)
        # print("RESPOSTAS MUNICIPIOS", respostas_municipios)
        pontuador_cap = Nivel(caps=[nome_cap])
        nivel = {nome_cap: {}}
        for resposta_municipio in respostas_municipios:  # Resposta por municipio por capacidade
            # print("RESPOSTA MUNICIPIO", resposta_municipio)
            nivel["municipio"] = resposta_municipio["municipio"]
            print(f"###### Município - {resposta_municipio['municipio']} #######")
            for pontuador in pontuadores:
                nivel[nome_cap][pontuador.componente] = pontuador.maturidade(resposta_municipio)
            nivel_cap = pontuador_cap.definir_nivel(niveis=nivel)
            if verbose:
                print("NIVEL COMPONENTES: ", nivel)
                print("NIVEL CAPACIDADE: ", nivel_cap , "\n")

            if nivel["municipio"] in resultado_mncp:
                resultado_mncp[resposta_municipio["municipio"]].append({"capacidade": nome_cap,
                                                                        "maturidade": nivel_cap,
                                                                        "componentes": nivel[nome_cap]})
            else:  # Inicializa o resultado
                resultado_mncp.update({resposta_municipio["municipio"]: [{"capacidade": nome_cap,
                                                                        "maturidade": nivel_cap,
                                                                        "componentes": nivel[nome_cap]}]})
            nivel = {nome_cap: {}}
    import json
    print("NIVEL MUNICIPIOS", json.dumps(resultado_mncp, ensure_ascii=False))


    # respostas_mncp = get_resp_mncp(caps=caps, idx_mncp=1)
    # for nome_cap, pontuadores in pontuadores_comps.items():  # Coletando o pontuador
    #     respostas_municipios = extrator.get_capacidade(nome_cap)
    #     # print("RESPOSTAS MUNICIPIOS", respostas_municipios)
    #     pontuador_cap = Nivel(caps=[nome_cap])
    #     nivel = {"municipio": "",
    #              nome_cap: {"maturidade": 0,
    #                         "componentes": {}}}
    #     nivel_mncps = []
    #     for resposta_municipio in respostas_municipios:  # Resposta por municipio por capacidade
    #         # print("RESPOSTA MUNICIPIO", resposta_municipio)
    #         nivel["municipio"] = resposta_municipio["municipio"]
    #         print(f"###### Município - {resposta_municipio['municipio']} #######")
    #         for pontuador in pontuadores:
    #             nivel[nome_cap]["componentes"][pontuador.componente] = pontuador.maturidade(resposta_municipio) 
    #         nivel_cap = pontuador_cap.definir_nivel(niveis=nivel)
    #         nivel[nome_cap]["maturidade"] = nivel_cap
    #         nivel_mncps.append(nivel)
    #         if verbose:
    #             print("NIVEL COMPONENTES: ", nivel)
    #             print("NIVEL CAPACIDADE: ", nivel_cap , "\n")
    #         # nivel_mncps.append(nivel)
    #     # print("NIVEL MUNICIPIOS", nivel_mncps)
    #     # del nivel_mncps
    #     print("DICT MUNICIPIO: ", nivel_mncps, "\n")
    #     del nivel

# def calculo_mncp(respostas_municipios, pontuadores):
#     for resposta_municipio in respostas_municipios:  # Resposta por municipio por capacidade
#         print("RESPOSTA MUNICIPIO", resposta_municipio)
#         nivel["municipio"] = resposta_municipio["municipio"]
#         for pontuador in pontuadores:
#             nivel[nome_cap][pontuador.componente] = pontuador.maturidade(resposta_municipio) 
#         print("NIVEL: \n", nivel)
#     return nivel

# def calculo_nivel(pontuadores_caps):
#     for nome_cap, pontuadores in pontuadores_caps.items():  # Coletando o pontuador
#         respostas_municipios = extrator.get_capacidade(nome_cap)
#         nivel = {nome_cap: {}}
#         calculo_mncp(respostas_municipios, pontuadores)
#         del nivel