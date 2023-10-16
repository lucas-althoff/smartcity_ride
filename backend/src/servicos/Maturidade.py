class Nivel:
    def __init__(s, nivel_componente,
                 nivel_capacidade={"EST": 0, "INFRA": 0, "DAD": 0, "SERV": 0, "MON": 0},
                 comps=["EST", "INFRA", "DAD", "SERV", "MON"]) -> None:
        # s.nca = nivel_capacidade
        s.nco = nivel_componente
        s.nca = nivel_capacidade
        s.comps = comps

    def definir_nivel(s):
        try:
            for comp in s.comps:  # Roda a regra em todos os componentes 
                s.nca[comp] = s.regras(comp=comp).index(False)  # Assinala valor em s.nca ao indice do primeiro nível False na lista de booleanos
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
            case "EST":
                result = [s.nco['Eplan'] == 1 and (s.nco['GovTec'] >= 1 or s.nco['SegPol'] >= 1), 
                          s.nco['Eplan'] == 2 and s.nco['GovCol'] == 2 and (s.nco['GovTec'] >= 2 or s.nco['SegPol'] >= 2 or s.nco['Vis'] >= 2),
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "INF":
                result = [s.nco[comp]['AQua'] == 1 and s.nco[comp]['HwSw'] == 1,
                          s.nco[comp]['ITplan'] == 2 and s.nco[comp]['IUPlan'] == 2 and s.nco['Aqua'] == 2 and s.nco['Inst'] == 2 and s.nco['HwSw'] == 2,
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "DAD":
                result = [s.nco['DPlan'] == 1 and s.nco['Digi'] == 1 and s.nco['DInteg'] == 1, 
                          s.nco['DPlan'] == 2 and s.nco['Digi'] == 2 and s.nco['DTransp'] == 2, 
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "SERV":
                result = [s.nco['SPlan'] == 1 and s.nco['SUrb'] == 1 and s.nco['SOn'] == 1, 
                          s.nco['SPlan'] == 2 and s.nco['SUrb'] == 2 and s.nco['SOn'] == 2 and s.nco['SInteg'] == 2,
                          False,
                          False,
                          False,
                          False,
                          False,
                          False]  # Manter sempre o último elemento como False
            case "MON":
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
