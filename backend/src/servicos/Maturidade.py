class Nivel:
    def __init__(s, nivel_componente,
                 nivel_capacidade={"EST": 0, "INF": 0, "DAD": 0, "SERV": 0, "MON": 0},
                #  comps=["EST", "INF", "DAD", "SERV", "MON"], #TODO: Quando finalizar os outros calculos de componentes inserir todas capacidades
                 comps=["EST"]) -> None:
        # s.nca = nivel_capacidade
        s.nco = nivel_componente
        s.nca = nivel_capacidade
        s.comps = comps

    def definir_nivel(s):
        try:
            for comp in s.comps:  # Roda a regra em todos os componentes 
                s.nca[comp] = s.regras(comp=comp).index(False)  # Assinala valor em s.nca ao indice do primeiro nível False na lista de booleanos
            return s.nca[comp]
        except Exception as e:
            return e

    def regras(s, comp_tag="Estrategia", comp="EST"):
        """ Função para computar as regras lógicas para definir
            :resultado:
                result
            :rtype: 
                <list> de booleanos de tamanho 8
            obs: só estão implementadas as regras até o nível 2
        """
        print("Calling regras with comp:", comp)
        print("Calling:", s.nco)
        try: 
            match comp:  # Regras em ordem de nível de maturidade por componente
                case "EST":
                    result = [s.nco[comp_tag]['Eplan'] == 1 and (s.nco[comp_tag]['GovTec'] >= 1 or s.nco[comp_tag]['SegPol'] >= 1), 
                            s.nco[comp_tag]['Eplan'] == 2 and s.nco[comp_tag]['GovCol'] == 2 and (s.nco[comp_tag]['GovTec'] >= 2 or s.nco[comp_tag]['SegPol'] >= 2 or s.nco[comp_tag]['Vis'] >= 2),
                            False,
                            False,
                            False,
                            False,
                            False,
                            False]  # Manter sempre o último elemento como False
                    print("Entered HERE2", result)
                case "INF":
                    result = [s.nco[comp_tag]['AQua'] == 1 and s.nco[comp_tag]['HwSw'] == 1,
                            s.nco[comp_tag]['ITplan'] == 2 and s.nco[comp_tag]['IUPlan'] == 2 and \
                                  s.nco[comp_tag]['AQua'] == 2 and s.nco[comp_tag]['Inst'] == 2 and s.nco[comp_tag]['HwSw'] == 2,
                            False,
                            False,
                            False,
                            False,
                            False,
                            False]  # Manter sempre o último elemento como False
                case "DAD":
                    result = [s.nco[comp_tag]['DPlan'] == 1 and s.nco[comp_tag]['Digi'] == 1 and s.nco[comp_tag]['DInteg'] == 1, 
                            s.nco[comp_tag]['DPlan'] == 2 and s.nco[comp_tag]['Digi'] == 2 and s.nco[comp_tag]['DTransp'] == 2, 
                            False,
                            False,
                            False,
                            False,
                            False,
                            False]  # Manter sempre o último elemento como False
                case "SERV":
                    result = [s.nco[comp_tag]['SPlan'] == 1 and s.nco[comp_tag]['SUrb'] == 1 and s.nco[comp_tag]['SOn'] == 1, 
                            s.nco[comp_tag]['SPlan'] == 2 and s.nco[comp_tag]['SUrb'] == 2 and s.nco[comp_tag]['SOn'] == 2 and s.nco['SInteg'] == 2,
                            False,
                            False,
                            False,
                            False,
                            False,
                            False]  # Manter sempre o último elemento como False
                case "MON":
                    result = [s.nco[comp_tag]['MPlan'] == 1, 
                            s.nco[comp_tag]['MPlan'] == 2 and s.nco[comp_tag]['Coord'] >= 1 and s.nco[comp_tag]['DTransp'] == 2, 
                            False,
                            False,
                            False,
                            False,
                            False,
                            False,
                            False]  # Manter sempre o último elemento como False
                case _:
                    raise Exception(f"Componente não é válido {comp}")
        except Exception as e:
            raise Exception(f"Problema na regra da capacidade. {e}")
        return result
