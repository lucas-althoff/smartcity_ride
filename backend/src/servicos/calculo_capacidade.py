class Nivel:
    def __init__(s, nivel_capacidade, nivel_componente) -> None:
        s.nca = nivel_capacidade
        s.nco = nivel_componente

    def definir_nivel(s):
        componentes = ["Estrategia", "Infraestrutura", "Dados", "ServicosApp", "Monitoramento"]
        try:
            for componente in componentes:  # Roda a regra em todos os componentes 
                s.nca[componente] = s.regras(comp=componente).index(False)  # Assinala valor em s.nca ao indice do primeiro nível False na lista de booleanos
            return s.nca
        except Exception as e:
            return e

    def regras(s, comp="Estrategia"):
        """ Função para computar as regras lógicas para definir
            :resultado:
                result
            :rtype: 
                <list> de booleanos de tamanho 8
            obs: só estão implementadas as regras até o nível 2
        """
        match comp:  # Regras em ordem de nível de maturidade por componente
            case "Estrategia":
                result = [s.nco['Eplan'] == 1 and (s.nco['GovTec'] >= 1 or s.nco['SegPol'] >= 1), 
                          s.nco['Eplan'] == 2 and s.nco['GovCol'] == 2 and (s.nco['GovTec'] >= 2 or s.nco['SegPol'] >= 2 or s.nco['Vis'] >= 2),
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "Infraestrutura":
                result = [s.nco[comp]['AQua'] == 1 and s.nco[comp]['HwSw'] == 1,
                          s.nco[comp]['ITplan'] == 2 and s.nco[comp]['IUPlan'] == 2 and s.nco['Aqua'] == 2 and s.nco['Inst'] == 2 and s.nco['HwSw'] == 2,
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "Dados":
                result = [s.nco['DPlan'] == 1 and s.nco['Digi'] == 1 and s.nco['DInteg'] == 1, 
                          s.nco['DPlan'] == 2 and s.nco['Digi'] == 2 and s.nco['DTransp'] == 2, 
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "ServicosApp":
                result = [s.nco['SPlan'] == 1 and s.nco['SUrb'] == 1 and s.nco['SOn'] == 1, 
                          s.nco['SPlan'] == 2 and s.nco['SUrb'] == 2 and s.nco['SOn'] == 2 and s.nco['SInteg'] == 2,
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "Monitoramento":
                result = [s.nco['MPlan'] == 1, 
                          s.nco['MPlan'] == 2 and s.nco['Coord'] >= 1 and s.nco['DTransp'] == 2, 
                          False,
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case _:
                raise Exception(f"Componente não é válido {comp}")
        return result


class Componente:
    def __init__(self, tipo, fixadores, qualificadores, universo) -> None:
        self.fixadores = fixadores
        self.qualificadores = qualificadores
        self.universo = universo
        self.tipo = tipo

    def soma(self, respostas: dict):
        peso = list(self.universo.values())
        soma = 0
        for alternativa in self.universo:
            soma = respostas.get(alternativa) * peso
        return soma

    def verificador(self, respostas: dict, limite: dict, qualificadores: list):
        # Verificar qual qualificadores estão presentes no nível mais alto
        for nivel, qualificador in qualificadores.items():
            for val in qualificador:
                # Cria lista com qualificadores encontrados
                encontrados = [any(v in n for n in respostas.values())
                               for v in val]
                if any(encontrados):  # Se todos qualificadores do nível foram encontrados, definir o nível
                    nivel_quali = nivel

        soma = self.soma(respostas)
        for nivel, limites in limite.items():
            if soma in limites:
                nivel_soma = nivel

        # Selecionar o nível de acordo com a melhor classificação
        if int(nivel_soma[-1]) > int(nivel_quali[-1]):
            return nivel_soma
        return nivel_quali


class Eplan(Componente):
    def __init__(self, respostas):
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
        self.respostas = respostas
        super.__init__(self.universo)

class GovCol(Componente):
    def __init__(self, respostas):
        self.fixadores = {"GovCol2": [],
                          "GovCol3": [],
                          "GovCol4": [],
                          "GovCol5": [],
                          "GovCol6": [],
                          "GovCol7": []}
        self.qualificadores = {"GovCol2": [],
                               "GovCol3": [],
                               "GovCol4": [],
                               "GovCol5": [],
                               "GovCol6": [],
                               "GovCol7": []}
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
        self.limite = {"GovCol2": [1, 2, 3, 4, 5],
                       "GovCol3": [6, 7, 8, 9, 10, 11],
                       "GovCol4": [12, 13, 14, 15, 16, 17],
                       "GovCol5": [18, 19, 20, 21, 22, 23],
                       "GovCol6": [24, 25, 26, 27, 28, 29],
                       "GovCol7": [30]}
        self.respostas = respostas
        super.__init__(self.universo)

class Gov(Componente):
    def __init__(self, respostas):
        self.fixadores = {"GovCol2": [],
                          "GovCol3": [],
                          "GovCol4": [],
                          "GovCol5": [],
                          "GovCol6": [],
                          "GovCol7": []}
        self.qualificadores = {"GovCol2": [],
                               "GovCol3": [],
                               "GovCol4": [],
                               "GovCol5": [],
                               "GovCol6": [],
                               "GovCol7": []}
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
        self.limite = {"GovCol2": [1, 2, 3, 4, 5],
                       "GovCol3": [6, 7, 8, 9, 10, 11],
                       "GovCol4": [12, 13, 14, 15, 16, 17],
                       "GovCol5": [18, 19, 20, 21, 22, 23],
                       "GovCol6": [24, 25, 26, 27, 28, 29],
                       "GovCol7": [30]}
        self.respostas = respostas
        super.__init__(self.universo)

def test_extracao():
    import json
    json_path = extracao_extrategia()  # Salva arquivo temporario json contendo respostas 
    with open(json_path,'r'):
        json_estrategia = json.load(json_estrategia)
    dict_estrategia = eval(json_estrategia)
    assert isinstance(dict_estrategia, dict) == True
        

if __name__ == "__main__":
    nivel_capacidade = {"Estrategia": 1,
                        "Infraestrutura": 1,
                        "Dados": 1,
                        "ServicosApp": 1,
                        "Monitoramento": 1}

    nivel_componente = {"Estrategia": {"Eplan": 1,
                                       "GovCol": 0,
                                       "GovTec": 1,
                                       "SegPol": 1,
                                       "Vis": 0},
                        "Infraestrutura": {"IUPlan": 0,
                                           "AQua": 1,
                                           "ITPlan": 0,
                                           "Inst": 0,
                                           "HwSw": 1,
                                           "GovTI": 0},
                        "Dados": {"DPlan": 1,
                                  "Digi": 1,
                                  "DTransp": 1,
                                  "DInteg": 0},
                        "ServicosApp": {"SPlan": 1,
                                        "SUrb": 1,
                                        "SOn": 1,
                                        "SInteg": 0},
                        "Monitoramento": {"MPlan": 1,
                                          "Coord": 0,
                                          "Perc": 0,
                                          "MTransp": 0, }}


    respostas_estrategia = {
        # Lista tamanho max 5 com campo aberto
        "EST01": ["EST01.b", "EST01.d", "EST01.a", "EST01.l", "EST01.m:Idosos"],
        # Lista tamanho max 5 com campo aberto
        "EST02": ["EST02.c", "EST02.e", "EST02.b", "EST02.l", "EST02.m:Idosos"],
        # Lista aberta com campo aberto
        "EST03": ["EST03.c", "EST03.a", "EST03.d"],
        # Lista aberta
        "EST03.1": ["EST03.1.c", "EST03.1.j", "EST03.1.k"],
        # Lista aberta com campo aberto
        "EST04": ["EST04.b", "EST04.c", "EST04.f"],
        # Lista aberta com campo aberto
        "EST05": ["EST05.a", "EST05.e", "EST05.g"],
        # Lista aberta com campo aberto
        "EST05.1": ["EST05.1.a:Elisa", "EST05.1.e:Maria", "EST05.1.g:Marcia"],
        "EST06": "EST06.d",  # Múltipla escolha
        # Lista aberta com campo aberto
        "EST06.1": ["EST06.1.a:Elisa", "EST06.1.b:Jesus", "EST06.1.c:Edison"],
        # Lista aberta com campo aberto
        "EST07": ["EST07.a:Roney", "EST07.c:Erica", "EST07.h:Marcia"],
        # Lista aberta com campo aberto
        "EST07.1": ["EST07.1.a:Luiz", "EST07.1.b:Waleska", "EST07.1.h:Daniela"],
        # Múltipla escolha com campo aberto
        "EST08": "EST08.f:Ana Luisa",
        # Múltipla escolha
        "EST09": "EST09.a"}

    respostas_infraestrutura = None
    respostas_dados = None
    respostas_servicosApp = None
    respostas_monitoramento = None

    respostas = {"nota_global": {"Estrategia": respostas_estrategia,
                                 "Infraestrutura": respostas_infraestrutura,
                                 "Dados": respostas_dados,
                                 "ServicosApp": respostas_servicosApp,
                                 "Monitoramento": respostas_monitoramento}}

    questionario = {"resultado_capacidade": nivel_capacidade,
                    "resultado_comp": nivel_componente,
                    "questoes": respostas}

    pontuador = Componente()
