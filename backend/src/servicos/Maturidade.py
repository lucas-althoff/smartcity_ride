class Nivel:
    def __init__(s,
                 nivel_capacidade={"EST": 0, "INF": 0, "DAD": 0, "SERV": 0, "MON": 0},
                 #  comps=["EST", "INF", "DAD", "SERV", "MON"], #TODO: Quando finalizar os outros calculos de componentes inserir todas capacidades
                 caps=["EST"]) -> None:
        # s.nca = nivel_capacidade
        s.nca = nivel_capacidade
        s.caps = caps

    def definir_nivel(s, niveis):
        try:
            for cap in s.caps:  # Roda a regra em todos os componentes
                s.nca[cap] = s.regras(niveis_comps=niveis, cap=cap).index(False)  # Assinala valor em s.nca ao indice do primeiro nível False na lista de booleanos
            return s.nca[cap]
        except Exception as e:
            return e

    def maturidade_estrategia(s, niveis_comps, nivel, cap='EST'):
        match nivel:
            case 1:
                c1 = int(niveis_comps[cap]['EPlan'][-1]) >= 1
                c2 = (int(niveis_comps[cap]['GovTec'][-1]) >= 1) or (int(niveis_comps[cap]['SegPol'][-1]) >= 1)
                if c1 and c2:
                    return True
                return False
            case 2:
                c1 = int(niveis_comps[cap]['EPlan'][-1]) >= 2 and int(niveis_comps[cap]['GovCol'][-1]) >= 2 
                c2 = int(niveis_comps[cap]['GovTec'][-1]) >= 2 or int(niveis_comps[cap]['SegPol'][-1]) >= 2 \
                    or int(niveis_comps[cap]['Vis'][-1]) >= 2
                if c1 and c2:
                    return True
                return False
            case 3:
                return False
            case 4:
                return False
            case 5:
                return False
            case 6:
                return False
            case 7:
                return False

    def maturidade_infraestrutura(s, niveis_comps, nivel, cap='INF'):
        match nivel:
            case 1:
                c1 = int(niveis_comps[cap]['AQua'][-1]) >= 1 and int(niveis_comps[cap]['HwSw'][-1]) >= 1
                if c1:
                    return True
                return False
            case 2:
                c1 = int(niveis_comps[cap]['ITPlan'][-1]) >= 2 and int(niveis_comps[cap]['IUPlan'][-1]) >= 2 
                c2 = int(niveis_comps[cap]['AQua'][-1]) >= 2 and int(niveis_comps[cap]['Inst'][-1]) >= 2 \
                    and int(niveis_comps[cap]['HwSw'][-1]) >= 2
                if c1 and c2:
                    return True
                return False
            case 3:
                return False
            case 4:
                return False
            case 5:
                return False
            case 6:
                return False
            case 7:
                return False

    def maturidade_dados(s, niveis_comps, nivel, cap='DAD'):
        match nivel:
            case 1:
                c1 = int(niveis_comps[cap]['DPlan'][-1]) >= 1 and int(niveis_comps[cap]['Digi'][-1]) >= 1 \
                    and int(niveis_comps[cap]['DInteg'][-1]) >= 1
                if c1:
                    return True
                return False
            case 2:
                c1 = int(niveis_comps[cap]['DPlan'][-1]) >= 2 and int(niveis_comps[cap]['Digi'][-1]) >= 2 \
                    and int(niveis_comps[cap]['DTransp'][-1]) >= 2
                if c1:
                    return True
                return False
            case 3:
                return False
            case 4:
                return False
            case 5:
                return False
            case 6:
                return False
            case 7:
                return False

    def maturidade_servicos(s, niveis_comps, nivel, cap='SERV'):
        match nivel:
            case 1:
                c1 = int(niveis_comps[cap]['SPlan'][-1]) >= 1 and int(niveis_comps[cap]['SUrb'][-1]) >= 1 \
                      and int(niveis_comps[cap]['SOn'][-1]) >= 1
                if c1:
                    return True
                return False
            case 2:
                c1 = int(niveis_comps[cap]['SPlan'][-1]) >= 2 and int(niveis_comps[cap]['SUrb'][-1]) >= 2 \
                    and int(niveis_comps[cap]['SOn'][-1]) >= 2 and int(niveis_comps['SInteg'][-1]) >= 2
                if c1:
                    return True
                return False
            case 3:
                return False
            case 4:
                return False
            case 5:
                return False
            case 6:
                return False
            case 7:
                return False

    def maturidade_monitoramento(s, niveis_comps, nivel, cap='MON'):
        match nivel:
            case 1:
                c1 = int(niveis_comps[cap]['MPlan'][-1]) >= 1
                if c1:
                    return True
                return False
            case 2:
                c1 = int(niveis_comps[cap]['MPlan'][-1]) >= 2 and int(niveis_comps[cap]['Coord'][-1]) >= 1
                if c1:
                    return True
                return False
            case 3:
                return False
            case 4:
                return False
            case 5:
                return False
            case 6:
                return False
            case 7:
                return False

    def regras(s, niveis_comps, cap):
        """ Função para computar as regras lógicas para definir
            :resultado:
                result
            :rtype: 
                <list> de booleanos de tamanho 8
            obs: só estão implementadas as regras até o nível 2
        """
        print("Computando Maturidade para Capacidade:", cap)
        try:
            resultado = []
            match cap:  # Regras em ordem de nível de maturidade por componente
                case "EST":
                    for nivel in range(1, 8):
                        resultado.append(s.maturidade_estrategia(niveis_comps, nivel))
                    print("Lista de Maturidade", resultado)
                case "INF":
                    for nivel in range(1, 8):
                        resultado.append(s.maturidade_infraestrutura(niveis_comps, nivel))
                    print("Lista de Maturidade", resultado)
                case "DAD":
                    for nivel in range(1, 8):
                        resultado.append(s.maturidade_dados(niveis_comps, nivel))
                    print("Lista de Maturidade", resultado)
                case "SERV":
                    for nivel in range(1, 8):
                        resultado.append(s.maturidade_servicos(niveis_comps, nivel))
                    print("Lista de Maturidade", resultado)
                case "MON":
                    for nivel in range(1, 8):
                        resultado.append(s.maturidade_monitoramento(niveis_comps, nivel))
                    print("Lista de Maturidade", resultado)
                case _:
                    raise Exception(f"Componente não é válido {cap}")
        except Exception as e:
            raise Exception(f"Problema na regra da capacidade. {e}")
        return resultado
