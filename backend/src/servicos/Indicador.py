from TIC import notas_planaltina, dict_indicators
from regrasNivelTIC import *
from ticEstrutura import estrutura_meioambiente, estrutura_economia, estrutura_sociocultural
import math


class Indicador:
    def __init__(self, formula, nome):
        self.formula = formula
        self.nome = nome
        self.func = 'maturidade_'+nome.split('_')[1]
        self.variables = dict_indicators[nome]
        self.val = 0
        # print(f"Indicador [{nome}] inicializado")

    def calcular_indicador(self, data):
        values = {}

        for var_name in self.variables:
            if var_name in data:
                values[var_name] = data[var_name]
            else:
                # Sem dados, considerar indicador como zero
                values[var_name] = 0

            if math.isnan(values[var_name]):
                values[var_name] = 0

        print("######  ", self.nome, self.formula, values)

        # Casos de denominador contendo valor igual a zero
        if self.nome == "ind_3086":
            if values['P'] == 0:
                resultado = 0
                self.val = resultado
                print("###### ", self.nome, resultado)
                return resultado

        substituted_formula = self.formula.format(**values)

        try:
            resultado = eval(substituted_formula)
            self.val = resultado
            print("######  ", self.nome, resultado)
            return resultado
        except Exception as e:
            print(f"Error calculating the indicator: {e}")
            return None

    def calcular_maturidade(self):
        print("FUNCAO", self.func)
        expressao = self.func+'(' + str(self.val)+')'
        print(expressao)
        print(eval(expressao))


def media_ponderada(topico):
    total_sum_pesos = 0
    total_pesos = 0

    for indicador, data in topico["Indicadores"].items():
        total_sum_pesos += data["val"] * data["peso"]
        total_pesos += data["peso"]

    if total_pesos > 0:
        return total_sum_pesos / total_pesos
    else:
        return 0


def computar_media_ponderada(estrutura):
    resultado = {}

    for topico, dados_topico in estrutura["Topicos"].items():
        average = media_ponderada(dados_topico)
        resultado[topico] = average * dados_topico["Peso"] / 100
    return resultado


def computar_media_dimensoes(estrutura, media_topicos):
    media_dimensoes = 0
    for topico, media in media_topicos.items():
        peso = estrutura["Topicos"][topico]['Peso']
        # print("PESO",peso)
        # print("MEDIA",media)
        # print("RESULTADO",media_dimensoes)
        media_dimensoes = media_dimensoes + peso*media

    return media_dimensoes


def popular_indicadores(estrutura, lista_indicadores):
    estrutura = estrutura.copy()
    for topico in estrutura["Topicos"].values():
        for nome_indicador, dados_indicador in topico["Indicadores"].items():

            for ind in lista_indicadores:
                # print("####### INDICADOR PROCURADO ", ind.nome)
                if ind.nome == nome_indicador:
                    matching_indicator = ind
                    # print("####### INDICADOR ENCONTRADO ", matching_indicator.nome)
                    # print("####### INDICADOR COMPLETO ", matching_indicator.__dict__)
                    dados_indicador["val"] = matching_indicator.val
                    # print("####### VALOR ", matching_indicator.val)

    print("Valores dos indicadores extraidos: ", estrutura)
    return estrutura


if "__main__" == __name__:
    import pandas as pd

    # ind_3025 = Indicador("GINI", "ind_3025")
    # ind_3087 = Indicador("PIB_PER_CAPITA", "ind_3087")
    # ind_3125 = Indicador("{POP_OCUP_FORMAL}", "ind_3125")
    # ind_4001 = Indicador("IDH_M", "ind_4001")
    # ind_4003 = Indicador("POP_TOT", "ind_4003")
    ind_3117 = Indicador("({AG001}/{G12A})*100", "ind_3117")
    ind_3127 = Indicador("({ES001}/{G12A})*100", "ind_3127")
    ind_3141 = Indicador("({ES026}/{G12A})*100", "ind_3141")
    ind_3027 = Indicador("({CO164}/{POP_TOT})*100", "ind_3027")
    ind_3122 = Indicador("{CS001}", "ind_3122")
    ind_3020 = Indicador("({EDOC_AGSN}/{EDOC_total})*100", "ind_3020")
    ind_4041 = Indicador("{Mhab18}+{Mhab182}+{Mhab183}+{Mhab201}+{Mhab202}+{Mhab203}+{Mhab204}+{Mhab205}+{Mhab206}+{Mhab207}+{Mhab21}", "ind_4041")
    ind_4045 = Indicador("({Mhab191}+{Mhab192}+{Mhab193}+{Mhab194})", "ind_4045")
    ind_3049 = Indicador("({A1}*2)+{B1}+{C1}+{D1}", "ind_3049")
    ind_3076 = Indicador("{A2}+{B2}+{C2}+{D2}", "ind_3076")
    ind_3124 = Indicador("{Mtra181}+({Mtra182}*3)+({Mtra183}*2)+({Mtra184}*2)+({Mtra185}*3)+{Mtra186}+{Mtra187}+({Mtra19}*3)+{Mtra23}", "ind_3124")
    ind_4011 = Indicador("({A3}*3)+{B3}+{C3}+{D3}+({E3}*2)+({F3}*2)", "ind_4011")
    ind_4031 = Indicador("{Mtra086}+{Mtra21}+{Mtra221}+{Mtra222}+{Mtra223}", "ind_4031")
    ind_4046 = Indicador("{Mtra085}+({Mtra24}*2)+{Mtra25}", "ind_4046")
    ind_4005 = Indicador("({existe_pavimentacao}/{total_pavimentacao})*100", "ind_4005")
    ind_3021 = Indicador("({Acesso_SCM}/{POP_TOT})*100", "ind_3021")
    ind_3022 = Indicador("({TOT_ACESSOS}/{POP_TOT})*100", "ind_3022")
    ind_3040 = Indicador("{3G}+({4G}*2)", "ind_3040")
    ind_3041 = Indicador("{fornecedores}", "ind_3041")
    ind_3134 = Indicador("({A4}*3)+({B4}*2)+{C4}+{D4}+({E4}*3)", "ind_3134")  # TODO ajustar a expressão desse indicador
    ind_4035 = Indicador("({Acesso_SCM_12Mbps}/{POP_TOT})*100", "ind_4035")
    ind_4036 = Indicador("({QNTD_EST}/{POP_TOT})*100_000", "ind_4036")
    ind_4024 = Indicador("({MTIP07}*3)+{MTIP081}+{MTIP082}+{MTIP083}", "ind_4024")
    ind_4025 = Indicador("({MTIP09}*3)+{MTIP101}+{MTIP102}+{MTIP103}+{MTIP104}+{MTIP105}+{MTIP106}", "ind_4025")
    ind_4032 = Indicador("({MTIP11}*3)+{MTIP121}+{MTIP122}+{MTIP123}", "ind_4032")
    ind_4033 = Indicador("({MTIP13}*3)+{MTIP141}+{MTIP142}", "ind_4033")
    ind_3016 = Indicador("{A5}+{B5}+{C5}+({D5}*3)+({E5}*3)+{F5}", "ind_3016")
    ind_4010 = Indicador("{A6}+{B6}+{C6}+{D6}+({E6}*2)", "ind_4010")
    ind_4012 = Indicador("{A7}+({B7}*2)+({C7}*3)", "ind_4012")
    ind_3004 = Indicador("{SERV02a}+{SERV02b}+{SERV02c}+{SERV02d}+{SERV02e}+({SERV02f}*2)+({SERV02g}*2) +"
                         "({SERV02h}*3)+({SERV02i}*2)+({SERV02j}*2)+({SERV02k}*3)+{SERV02l}+({SERV02m}*2)", "ind_3004")
    ind_3033 = Indicador("({DAD07a}*3) + ({DAD07b}*2) + {DAD07c}*0", "ind_3033")
    ind_3003 = Indicador("((({IN_LABORATORIO_INFORMATICA}/{ESC_MUN}) + ({IN_EQUIP_LOUSA_DIGITAL}/{ESC_MUN}) +\
                         ({IN_EQUIP_MULTIMIDIA}/{ESC_MUN}) + ({IN_DESKTOP_ALUNO}/{ESC_MUN}) + \
                        ({IN_COMP_PORTATIL_ALUNO}/{ESC_MUN}) + ({IN_TABLET_ALUNO}/{ESC_MUN}) + \
                        ({IN_INTERNET_APRENDIZAGEM_ALUNOS}/{ESC_MUN}))/7)*100", "ind_3003")
    ind_3011 = Indicador("{TX_ANALF}", "ind_3011")
    ind_3086 = Indicador("{N}/{P}", "ind_3086")
    ind_3115 = Indicador("100000*{QT_VAGA_TOTAL}/{POP_TOT}", "ind_3115")
    ind_4006 = Indicador("{A8}+{B8}+{C8}+{D8}+{E8}+{F8}+{G8}", "ind_4006")
    ind_4020 = Indicador("{Medu131}+{Medu132}+{Medu133}+{Medu134}", "ind_4020")
    ind_4034 = Indicador("{DIST_IDADE_SERIE}", "ind_4034")
    ind_4037 = Indicador("({IN_INTERNET}/{ESC_MUN})*100", "ind_4037")
    ind_4048 = Indicador("(({QT_DESKTOP_ALUNO}+{QT_COMP_PORTATIL_ALUNO})/{QT_MATRICULAS})*100_000", "ind_4048")
    ind_3077 = Indicador("({Mcul3901}*2)+({Mcul3902}*2)+({Mcul3903}*2)+({Mcul3904}*2)+({Mcul3905}*2)+({Mcul3906}*2) +"
                         "({Mcul3907}*2)+{Mcul3908}+{Mcul3909}+{Mcul3910}+{Mcul3911}+{Mcul3912}+{Mcul3913}+{Mcul3914}+{Mcul3916}+"
                         "{Mcul3917}+{Mcul3918}+{Mcul3919}+({Mcul40}*2)", "ind_3077")
    ind_3107 = Indicador("({Mcul15}*3)+{Mcul161}*1+{Mcul162}*1+({Mcul18}*2)", "ind_3107")
    ind_3123 = Indicador("{A9}+{B9}+{C9}+{D9}+{E9}+{F9}", "ind_3123")
    ind_4040 = Indicador("{A10}+{B10}+{C10}+{D10}+{E10}+{F10}+{G10}+{H10}", "ind_4040")
    ind_3006 = Indicador("{A11}+{B11}+{C11}+{D11}+{E11}+({F11}*2)", "ind_3006")
    ind_3095 = Indicador("({NUM_LEITOS_PUB}/{POP_TOT})*100_000", "ind_3095")
    ind_3096 = Indicador("({NUM_MED}/{POP_TOT})*100_00", "ind_3096")
    ind_3125 = Indicador("{A12} + ({B12}*2)", "ind_3125")
    ind_4004 = Indicador("{A13}+{B13}+{C13}+{D13}+({E13}*2)", "ind_4004")
    ind_4021 = Indicador("(({NVBP}/{TOT_NV}) + ({NVPN}/{TOT_NV}))/2", "ind_4021")
    ind_3048 = Indicador("{A14}+{B14}+{C14}+{D14}+{E14}", "ind_3048")
    ind_4016 = Indicador("{TX_HOMIC}", "ind_4016")
    ind_4017 = Indicador("({Medu114}*3)+({MASS2411}*3)+({MASS2418}*2)+{MASS2614}", "ind_4017")
    ind_3007 = Indicador("({A15}*2)+{B15}+({C15}*2)+{D15}+({E15}*2)+({F15}*2)+({G15}*2)", "ind_3007")
    ind_4042 = Indicador("{Mgrd01}+{Mgrd06}+{Mgrd07}+{Mgrd08}+{Mgrd11}+{Mgrd14}", "ind_4042")
    ind_3039 = Indicador("({A100}*3)+{A107}+{A108}+{A109}+{A110}+{A111}+{A113}", "ind_3039")
    ind_4039 = Indicador("{A16} + {B16} + {C16}", "ind_4039")
    ind_4043 = Indicador("({MPPM01}*3)+{MPPM101}+{MPPM102}+(({MPPM103}+{MPPM104}+{MPPM105})*2)", "ind_4043")
    ind_4044 = Indicador("{MASS261}+{MASS262}+{MASS263}+{MASS264}+{MASS265}+{MASS266} +"
                         "{MASS267}+{MASS268}+{MASS269}+{MASS610}+{MASS611}+{MASS612}+{MASS613}+{MASS614}", "ind_4044")
    ind_3103 = Indicador("(({A17}+{B17}+{F17})*2)+{C17}+(({D17}+{E17}+{G17})*3)", "ind_3103")
    ind_3147 = Indicador("{A18}+{B18}+{C18}+{D18}+{E18}", "ind_3147")
    ind_3024 = Indicador("({ES005}/({AG010}-{AG019}))*100", "ind_3024")
    ind_3028 = Indicador("(({AG010}-{AG019})/{AG001}) * (1000000/365)", "ind_3028")
    ind_3042 = Indicador("{A19}+({B19}*3)+{C19}", "ind_3042")
    ind_4047 = Indicador("(({ES006}+{ES014}+{ES015})/({ES005}+{ES013}))*100", "ind_4047")
    ind_4007 = Indicador("({CS026}/{CO119})*100", "ind_4007")
    ind_4014 = Indicador("{A20}+{B20}+{C20}+{D20}", "ind_4014")
    ind_4030 = Indicador("(({Mmam10}+{Mmam16})*2)+{Mmam18}+{Mmam203}+{Mmam204}+{Mmam207}+{Mmam208}+{Mmam209}+{Mmam2010}", "ind_4030")
    ind_3056 = Indicador("{A21}+{B21}+{C21}+{D21}+{E21}+{F21}+{G21}+{H21}+{I21}+{J21}+{K21}+{L21}", "ind_3056")
    ind_3113 = Indicador("{A22}+{B22}+{C22}+{D22}", "ind_3113")
    ind_3043 = Indicador("{A23}+({B23}*3)+({C23}*2)+({D23}*3)", "ind_3043")
    ind_3069 = Indicador("{A24}+{B24}", "ind_3069")

    lista_indicadores = [
        ind_3117,
        ind_3127,
        ind_3141,
        ind_3033,
        ind_3020,
        ind_4041,
        ind_4045,
        ind_3040,
        ind_3041,
        ind_4035,
        ind_4036,
        ind_3021,
        ind_3022,
        ind_3134,
        ind_4024,
        ind_4025,
        ind_4032,
        ind_4033,
        ind_3027,
        ind_3122,
        ind_3004,
        ind_3016,
        ind_4010,
        ind_4012,
        ind_3049,
        ind_3076,
        ind_3124,
        ind_4011,
        ind_4031,
        ind_4046,
        ind_4005,
        ind_3024,
        ind_3028,
        ind_3042,
        ind_4047,
        ind_4047,
        ind_4030,
        ind_3043,
        ind_3069,
        ind_3056,
        ind_3113,
        ind_4007,
        ind_4014,
        ind_3077,
        ind_3107,
        ind_3123,
        ind_4040,
        ind_3003,
        ind_3011,
        ind_3086,
        ind_3115,
        ind_4006,
        ind_4020,
        ind_4034,
        ind_4037,
        ind_4048,
        ind_3007,
        ind_4042,
        ind_3039,
        ind_4039,
        ind_4043,
        ind_4044,
        ind_3103,
        ind_3147,
        ind_3006,
        ind_3095,
        ind_3096,
        ind_3125,
        ind_4004,
        ind_4021,
        ind_3048,
        ind_4016,
        ind_4017]

    df = pd.read_csv('/home/lucas/Projetos/e-ride/Dados/dados_tic.csv')
    dados_lista = df.to_dict(orient='records')

    def save_dict(dict):
        df = pd.DataFrame.from_dict(dict, orient="index")
        df.to_csv("resultado.csv")

    municipios = {0: 'Águas Lindas de Goiás',
                  1: 'Alexânia',
                  2: 'Cidade Ocidental',
                  3: 'Cocalzinho de Goias',
                  4: 'Cristalina',
                  5: 'Formosa',
                  6: 'Luziania',
                  7: 'Novo Gama',
                  8: 'Padre Bernardo',
                  9: 'Planaltina',
                  10: 'Santo Antônio do Descoberto',
                  11: 'Valparaíso de Goiás'}

    print('Índices dos municipios:', municipios)
    try:
        i = int(input('Calcular indicadores para qual municipio?'))
    except Exception:
        print('Insira um índice válido')
        i = input('Calcular indicadores para qual municipio?')
    
    # Extrair apenas o municipio para analise
    dados = dados_lista[i]
    # dados_lista = dados_lista[7]
    save_ind = True

    # for dados in dados_lista:
    print(dados)
    print("###################### INICIANDO CALCULO PARA MUNCIPIO - ", dados['municipio'], "############################")
    res = []
    dict_ind = {'indicador': 'resultado',
                'municipio': dados['municipio']}
    for ind in lista_indicadores:
        res = ind.calcular_indicador(dados)
        # print("######   Resultado: ", res)
        # print("######   Nome: ", ind.nome)
        # print("######   DICT: ", dict_ind)
        res = str(res).replace('.', ',')
        dict_ind.update({ind.nome: res})
        if save_ind:
            save_dict(dict_ind)

    print("###########INDICADORES CALCULADOS##############", len(lista_indicadores))

    # estrutura_economia_res = popular_indicadores(estrutura_economia, lista_indicadores)
    # estrutura_sociocultural_res = popular_indicadores(estrutura_sociocultural, lista_indicadores)
    # estrutura_meioambiente_res = popular_indicadores(estrutura_meioambiente, lista_indicadores)

    # print(estrutura_meioambiente_res)
    print("###########RESULTADOS INDICADORES EXTRAIDOS##############")

    # Economia
    # media_topicos = computar_media_ponderada(estrutura_economia_res)
    # print(media_topicos)

    # media_economia = computar_media_dimensoes(estrutura_economia_res, media_topicos)
    # print(media_economia)

    # Meio ambiente

    # media_topicos = computar_media_ponderada(estrutura_meioambiente_res)
    # print(media_topicos)
    # media_meioambiente = com
    # putar_media_dimensoes(estrutura_meioambiente_res, media_topicos)
    # print(media_meioambiente)

    # Sociocultural

    # media_topicos = computar_media_ponderada(estrutura_sociocultural_res)
    # print("Media topicos =", media_topicos)

    # media_sociocultural = computar_media_dimensoes(estrutura_sociocultural_res, media_topicos)
    # print("Media dimensao = ", media_sociocultural)

    print("###########Maturidade INDICADORES CALCULADA ##############")
    for ind in lista_indicadores:
        res = ind.calcular_maturidade()

    print("###########Maturidade TOPICOS CALCULADA ##############")

    print("###########Maturidade DIMENSOES CALCULADA ##############")
