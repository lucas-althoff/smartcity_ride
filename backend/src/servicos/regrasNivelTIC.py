# Água e esgoto


def maturidade_3117(valor):
    if valor < .3599:
        return 1
    if valor >= .36 and valor <= .6966:
        return 2
    if valor >= .6967 and valor <= .836:
        return 3
    if valor >= .837 and valor <= .8778:
        return 4
    if valor >= .8779 and valor <= .922:
        return 5
    if valor >= .9221 and valor <= .99:
        return 6
    if valor >= .9901 and valor <= 1:
        return 7
    return 1


def maturidade_3127(valor):
    if valor < .3154:
        return 1
    if valor >= .3155 and valor <= .5319:
        return 2
    if valor >= .532 and valor <= .7329:
        return 3
    if valor >= .733 and valor <= .8778:
        return 4
    if valor >= .8779 and valor <= .922:
        return 5
    if valor >= .9221 and valor <= .99:
        return 6
    if valor >= .9901 and valor <= 1:
        return 7
    return 1


def maturidade_3141(valor):
    if valor < .3154:
        return 1
    if valor >= .36 and valor <= .701:
        return 2
    if valor >= .7011 and valor <= .896:
        return 3
    if valor >= .8961 and valor <= .924:
        return 4
    if valor >= .9241 and valor <= .9799:
        return 5
    if valor >= .98 and valor <= .99:
        return 6
    if valor >= .9901 and valor <= 1:
        return 7
    return 1


# Dados Abertos
def maturidade_3033(valor, nivel_topico=1):
    # Dados abertos da gestão municipal
    if valor < 1:
        return 5
    if valor >= 1 and nivel_topico >= 5:
        return nivel_topico
    if valor >= 1 and nivel_topico < 5:
        return 7
    return 1


# Habitação
def maturidade_3020(valor):
    if valor <= 1 and valor >= .4623:
        return 1
    if valor <= .4622 and valor >= .2484:
        return 2
    if valor <= .2483 and valor >= .056:
        return 3
    if valor <= .0559 and valor >= .0411:
        return 4
    if valor <= .041 and valor >= .0144:
        return 5
    if valor <= .0143 and valor >= .0059:
        return 6
    if valor <= .0058:
        return 7
    return 1


def maturidade_4041(valor):
    if valor == 0:
        return 1
    if valor == 1 or valor == 2:
        return 2
    if valor == 3 or valor == 4:
        return 3
    if valor == 5 or valor == 6:
        return 4
    if valor == 7 or valor == 8:
        return 5
    if valor == 9 or valor == 10:
        return 6
    if valor == 11:
        return 7
    return 1


def maturidade_4045(valor, nivel_topico=4):
    if valor == 4 or valor == 3:
        return 1
    if valor == 2:
        return 2
    if valor == 1:
        return 3
    if valor == 0:
        return 4
    if valor == 0:
        return nivel_topico
    if valor == 0:
        return nivel_topico
    if valor == 0:
        return nivel_topico
    return 1

# Infraestrutura de conectividade


def maturidade_3021(valor):
    # Escala de acesso à banda larga fixa
    if valor < .4:
        return 1
    if valor >= .401 and valor <= .772:
        return 2
    if valor >= .773 and valor <= .1543:
        return 3
    if valor >= .1544 and valor <= .2356:
        return 4
    if valor >= .2357 and valor <= .3134:
        return 5
    if valor >= .3135 and valor <= .5:
        return 6
    if valor >= .501:
        return 7
    return 1


def maturidade_3022(valor):
    # Escala de acesso à banda larga móvel
    if valor < .35:
        return 1
    if valor >= .351 and valor <= .45:
        return 2
    if valor >= .451 and valor <= .62:
        return 3
    if valor >= .621 and valor <= .75:
        return 4
    if valor >= .751 and valor <= .87:
        return 5
    if valor >= .871 and valor <= .9479:
        return 6
    if valor >= .948:
        return 7
    return 1


def maturidade_3040(valor, nivel_topico=1):
    # Cobertura de acesso à banda larga móvel por tecnologias 3G e 4G
    if valor == 0:
        return 3
    if valor == 1:
        return nivel_topico
    return 1


def maturidade_3041(valor, nivel_topico=1):
    # Cobertura de fibra ótica
    if valor == 0:
        return 3
    if valor == 1:
        return nivel_topico
    return 1


def maturidade_3134(valor, nivel_topico=3):
    # Rede de tecnologia interligando os equipamentos e edifícios públicos
    if valor == 0:
        return 2
    if valor == 1:
        return 3
    if valor == 2:
        return 4
    if valor == 3:
        return nivel_topico
    return 1


def maturidade_4035(valor):
    # Escala de acesso à banda larga fixa de alta velocidade
    if valor < .0203:
        return 1
    if valor >= .0204 and valor <= .0461:
        return 2
    if valor >= .0462 and valor <= .1578:
        return 3
    if valor >= .1579 and valor <= .2356:
        return 4
    if valor >= .751 and valor <= .87:
        return 5
    if valor >= .871 and valor <= .9479:
        return 6
    if valor >= .948:
        return 7
    return 1


def maturidade_4036(valor):
    # Números de estações rádio base
    if valor < .2:
        return 1
    if valor >= .201 and valor <= .5:
        return 2
    if valor >= .501 and valor <= .62:
        return 3
    if valor >= .621 and valor <= .75:
        return 4
    if valor >= .751 and valor <= .85:
        return 5
    if valor >= .851 and valor < .99:
        return 6
    if valor >= .99:
        return 7
    return 1


# Inovação
def maturidade_4024(valor, nivel_topico=5):
    # Qualificação profissional e intermediação de mão de obra
    if valor == 0:
        return 1
    if valor == 1 or valor == 2 or valor == 3:
        return 2
    if valor == 4:
        return 3
    if valor == 5:
        return 4
    if valor == 6 and nivel_topico < 5:
        return 5
    if valor > 5 and nivel_topico >= 5:
        return nivel_topico
    return 1


def maturidade_4025(valor):
    # Inclusão produtiva urbana
    if valor == 0:
        return 1
    if valor == 1 or valor == 2 or valor == 3:
        return 2
    if valor == 4:
        return 3
    if valor == 5 or valor == 6:
        return 4
    if valor == 7:
        return 5
    if valor == 8:
        return 6
    if valor == 9:
        return 7
    return 1


def maturidade_4032(valor, nivel_topico=5):
    # Acesso a crédito, microcrédito e seguro
    if valor == 0:
        return 1
    if valor == 1 or valor == 2 or valor == 3:
        return 2
    if valor == 4:
        return 3
    if valor == 5:
        return 4
    if valor == 6:
        return 5
    if valor >= 6 and nivel_topico > 5:
        return nivel_topico
    return 1


def maturidade_4033(valor, nivel_topico=5):
    # Geração de trabalho e renda no município
    if valor == 0:
        return 1
    if valor == 1 or valor == 2 or valor == 3:
        return 2
    if valor == 4:
        return 3
    if valor == 5:
        return 4
    if valor == 6 and nivel_topico < 5:
        return 5
    if valor > 5 and nivel_topico >= 5:
        return nivel_topico
    return 1


# Resíduos Sólidos
def maturidade_3027(valor):
    # Taxa da população coberta com serviço de coleta de resíduos
    if valor < .5512:
        return 1
    if valor >= .5513 and valor <= .7999:
        return 2
    if valor >= .8 and valor <= .921:
        return 3
    if valor >= .9211 and valor <= .9511:
        return 4
    if valor >= .9512 and valor <= .9812:
        return 5
    if valor >= .9812 and valor <= .99:
        return 6
    if valor >= .9901 and valor <= 1:
        return 7
    return 1


def maturidade_3122(valor, nivel_topico=4):
    # Coleta seletiva de resíduos no município
    if valor == 0:
        return 3
    if valor == 1:
        return 3
    if valor == 1 and nivel_topico < 4:
        return 4
    if valor == 1 and nivel_topico >= 4:
        return nivel_topico
    return 1


# Serviços On-line da Prefeitura
def maturidade_3004(valor):
    # Serviços no website da prefeitura
    if valor == 0:
        return 1
    if valor > 0 and valor <= 4:
        return 2
    if valor >= 5 and valor <= 8:
        return 3
    if valor >= 9 or valor == 12:
        return 4
    if valor >= 13 or valor == 16:
        return 5
    if valor >= 17 or valor == 20:
        return 6
    if valor >= 21:
        return 7
    return 1


# Sistemas e Tecnologia para Gestão Urbana
def maturidade_3016(valor):
    # Sistema de informação geográfica da prefeitura
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3 or valor == 4:
        return 4
    if valor >= 5 and valor <= 7:
        return 5
    if valor == 8 or valor == 9:
        return 6
    if valor == 10:
        return 7
    return 1


def maturidade_4010(valor):
    # Centros de comando e controle para gestão da cidade
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3 or valor == 4:
        return 4
    if valor == 5:
        return 5
    if valor == 6:
        return 6
    if valor == 10:
        return 7
    return 1


def maturidade_4012(valor):
    # Plataforma integrada de cidade inteligente
    if valor == 0:
        return 1
    if valor == 1:
        return 3
    if valor == 2:
        return 5
    if valor == 3:
        return 7
    return 1


# Transporte
def maturidade_3049(valor):
    # Serviços de compartilhamento de viagens
    if valor == 0:
        return 2
    if valor == 1:
        return 3
    if valor == 2:
        return 4
    if valor == 3:
        return 5
    if valor == 4:
        return 6
    if valor == 5:
        return 7
    return 1


def maturidade_3076(valor):
    # Serviço de informações de transporte público em tempo real
    if valor == 0:
        return 2
    if valor == 1:
        return 3
    if valor == 2:
        return 4
    if valor == 3:
        return 5
    if valor == 4:
        return 7
    return 1


def maturidade_3124(valor):
    # Serviços regulares de transporte de passageiros
    if valor >= 0 and valor < 3:
        return 1
    if valor >= 4 and valor < 6:
        return 2
    if valor >= 7 and valor < 9:
        return 4
    if valor >= 10 and valor < 13:
        return 5
    if valor >= 15 and valor < 16:
        return 6
    if valor == 17:
        return 7
    return 1


def maturidade_4011(valor):
    # Serviços e soluções inteligentes para mobilidade urbana
    if valor == 0:
        return 2
    if valor == 1 or valor == 2:
        return 3
    if valor == 3 or valor == 4:
        return 4
    if valor == 5 and valor == 7:
        return 5
    if valor == 8 and valor == 9:
        return 6
    if valor == 10:
        return 7
    return 1


def maturidade_4031(valor):
    # Acessibilidade no transporte público
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3:
        return 4
    if valor == 4:
        return 5
    if valor == 5:
        return 6
    if valor == 6:
        return 7
    return 1


def maturidade_4046(valor, nivel_topico=4):
    # Ciclomobilidade na cidade
    if valor < .001:
        return 1
    if valor >= .001 and valor <= .5:
        return 2
    if valor >= .5 and valor <= .75:
        return 3
    if valor >= .7501 and nivel_topico < 4:
        return 4
    if valor >= .7501 and nivel_topico >= 4:
        return nivel_topico
    return 1


# Urbanização Vias Públicas

def maturidade_4005(valor):
    # Índice de pavimentação das vias públicas
    if valor < .454:
        return 1
    if valor >= .4541 and valor <= .7828:
        return 2
    if valor >= .7829 and valor <= .8171:
        return 3
    if valor >= .8172 and valor <= .8772:
        return 4
    if valor >= .8773 and valor <= .9373:
        return 5
    if valor >= .9374 and valor <= .99:
        return 6
    if valor >= .9901 and valor <= 1:
        return 7
    return 1


# Cultura


def maturidade_3077(valor):
    # 3077 Estrutura de equipamentos culturais e esportivos
    if valor == 0:
        return 1
    if valor >= 1 and valor <= 3:
        return 2
    if valor >= 4 and valor <= 7:
        return 3
    if valor >= 8 and valor <= 11:
        return 4
    if valor >= 12 and valor <= 15:
        return 5
    if valor >= 16 and valor <= 21:
        return 6
    if valor >= 22 and valor <= 27:
        return 6
    return 1


def maturidade_3107(valor):
    # Proteção do patrimônio cultural material e imaterial
    if valor == 0:
        return 1
    if valor == 1 or valor == 2:
        return 2
    if valor == 3 or valor == 4:
        return 3
    if valor == 5:
        return 4
    if valor == 6:
        return 5
    if valor == 7:
        return 7
    return 1


def maturidade_3123(valor):
    # 3123 Serviços on-line para promoção de cultura
    if valor == 0:
        return 2
    if valor == 1 or valor == 2:
        return 3
    if valor == 3:
        return 4
    if valor == 4:
        return 5
    if valor == 5:
        return 6
    if valor == 6:
        return 7
    return 1


def maturidade_4040(valor):
    # 4040 Serviços culturais on-line oferecidos para a população
    if valor == 0:
        return 2
    if valor >= 1 or valor <= 3:
        return 3
    if valor == 4 or valor == 5:
        return 4
    if valor == 6:
        return 5
    if valor == 7:
        return 6
    if valor == 8:
        return 7
    return 1


def maturidade_3003(valor):
    # 3003 Índice de equipamentos de tecnologia disponíveis nas escolas públicas municipais
    if valor < .069:
        return 1
    if valor >= .07 and valor <= .139:
        return 2
    if valor >= .14 and valor <= .189:
        return 3
    if valor >= .19 and valor <= .309:
        return 4
    if valor >= .31 and valor <= .549:
        return 5
    if valor >= .55 and valor <= .779:
        return 6
    if valor >= .78 and valor <= 1:
        return 7
    return 1


def maturidade_3011(valor):
    # 3011 – Taxa de analfabetismo
    if valor >= .4:
        return 1
    if valor <= .399 and valor >= .188:
        return 2
    if valor <= .1887 and valor >= .136:
        return 3
    if valor <= .135 and valor >= .096:
        return 4
    if valor <= .095 and valor >= .06:
        return 5
    if valor <= .059 and valor >= .01:
        return 6
    if valor <= .009:
        return 7
    return 1


def maturidade_3086(valor):
    # 3086- Índice de desenvolvimento da educação básica (IDEB) - anos finais
    if valor < .0349:
        return 1
    if valor >= .035 and valor <= .0416:
        return 2
    if valor >= .0417 and valor <= .05:
        return 3
    if valor >= .0501 and valor <= .062:
        return 4
    if valor >= .063 and valor <= .07:
        return 5
    if valor >= .071 and valor <= .089:
        return 6
    if valor >= .09 and valor <= 1:
        return 7
    return 1


def maturidade_3115(valor):
    # 3115 - Vagas no ensino superior
    if valor < 1:
        return 1
    if valor >= 1 and valor <= 2000:
        return 2
    if valor >= 2001 and valor <= 3000:
        return 3
    if valor >= 3001 and valor <= 4000:
        return 4
    if valor >= 4001 and valor <= 5000:
        return
    if valor >= 5001 and valor <= 6000:
        return 6
    if valor >= 6001:
        return 7
    return 1


def maturidade_4006(valor):
    # 4006 - Centros de educação tecnológica
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3 or valor == 4:
        return 4
    if valor == 5:
        return 5
    if valor == 6:
        return 6
    if valor == 7:
        return 7
    return 1


def maturidade_4020(valor, nivel_topico=4):
    # 4020 Ações de educação para comunidades específicas
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3:
        return 4
    if valor == 4:
        return 5
    if valor == 4 and nivel_topico >= 4:
        return nivel_topico
    return 1


def maturidade_4034(valor):
    # 4034 - Taxas de distorção idade-série
    if valor <= .1 and valor >= .51:
        return 1
    if valor <= .5099 and valor >= .31:
        return 2
    if valor <= .3099 and valor >= .21:
        return 3
    if valor <= .2099 and valor >= .16:
        return 4
    if valor <= .1599 and valor >= .11:
        return 5
    if valor <= .1099 and valor >= .06:
        return 6
    if valor <= .009:
        return 7
    return 1


def maturidade_4037(valor):
    # 4037 - Percentual de escolas municipais com acesso à internet
    if valor < .3299:
        return 1
    if valor >= .33 and valor <= .599:
        return 2
    if valor >= .6 and valor <= .7:
        return 3
    if valor >= .701 and valor <= .8:
        return 4
    if valor >= .801 and valor <= .9:
        return 5
    if valor >= .901 and valor <= .99:
        return 6
    if valor >= .9901 and valor <= 1:
        return 7
    return 1


def maturidade_4048(valor):
    # 4048 - Computadores para uso dos alunos
    if valor <= 500:
        return 1
    if valor >= 501 and valor <= 1000:
        return 2
    if valor >= 1001 and valor <= 1500:
        return 3
    if valor >= 1501 and valor <= 2000:
        return 4
    if valor >= 2001 and valor <= 4000:
        return
    if valor >= 4001 and valor <= 6000:
        return 6
    if valor >= 6001:
        return 7
    return 1

# Gestão de Desastres


def maturidade_3007(valor):
    # 3007 Soluções de tecnologia para gestão e monitoramento de desastres naturais
    if valor == 0:
        return 1
    if valor == 1 or valor == 2:
        return 2
    if valor == 3:
        return 3
    if valor == 4 or valor == 5:
        return 4
    if valor >= 6 and valor <= 8:
        return 5
    if valor == 9 or valor == 10:
        return 6
    if valor > 10:
        return 7
    return 1


def maturidade_4042(valor, nivel_topico=5):
    # 4042 Vulnerabilidade a riscos e desastres naturais
    if valor == 6 or valor == 5:
        return 1
    if valor == 4 or valor == 2:
        return 2
    if valor == 2:
        return 3
    if valor == 1:
        return 4
    if valor == 0 and nivel_topico <= 5:
        return 5
    if valor == 0 and nivel_topico > 5:
        return nivel_topico
    return 1


# Inclusão digital
def maturidade_3039(valor):
    # 3039 Promoção de inclusão digital
    if valor == 0:
        return 1
    if valor >= 1 and valor <= 3:
        return 2
    if valor == 4:
        return 3
    if valor == 5 or valor == 6:
        return 4
    if valor == 7:
        return 5
    if valor == 8:
        return 6
    if valor == 9:
        return 7
    return 1


def maturidade_4039(valor, nivel_topico=5):
    # 4039 Cursos de capacitação tecnológica
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3:
        return 4
    if valor == 4:
        return 5
    if valor == 5 and nivel_topico <= 5:
        return 6
    if valor == 5:
        return 7
    return 1


# Inclusão Social
def maturidade_4043(valor):
    # 4043 Políticas públicas para mulheres
    if valor == 0:
        return 1
    if valor >= 1 and valor <= 3:
        return 3
    if valor == 4 or valor == 5:
        return 4
    if valor == 6 or valor == 7:
        return 5
    if valor == 8 or valor == 9:
        return 6
    if valor == 10 or valor == 11:
        return 7
    return 1


def maturidade_4044(valor):
    # 4044 Inclusão social para grupos específicos
    if valor == 0:
        return 1
    if valor == 1 or valor == 2:
        return 2
    if valor == 3 or valor == 4:
        return 3
    if valor >= 5 and valor <= 7:
        return 4
    if valor >= 8 and valor <= 10:
        return 5
    if valor == 11 or valor == 12:
        return 6
    if valor >= 12:
        return 7
    return 1


# Participação Pública
def maturidade_3103(valor):
    # 3103 Formas presenciais para participação pública
    if valor < 2:
        return 1
    if valor >= 2 and valor <= 4:
        return 2
    if valor >= 5 and valor <= 7:
        return 3
    if valor >= 8 and valor <= 10:
        return 4
    if valor >= 11 and valor <= 13:
        return 5
    if valor == 14 or valor == 15:
        return 6
    if valor > 15:
        return 7
    return 1


def maturidade_3147(valor):
    # 3147 Formas on-line para participação pública
    if valor == 0:
        return 2
    if valor == 1:
        return 3
    if valor == 2:
        return 4
    if valor == 3:
        return 5
    if valor == 4:
        return 6
    if valor == 5:
        return 7
    return 1


# Saúde
def maturidade_3006(valor):
    # 3006 Serviços de telemedicina ou telessaúde
    if valor == 0:
        return 2
    if valor == 1:
        return 3
    if valor == 2 or valor == 3:
        return 4
    if valor == 4 or valor == 5:
        return 5
    if valor >= 6 and valor == 8:
        return 6
    if valor > 8:
        return 7
    return 1


def maturidade_3095(valor):
    # 3095 Leitos hospitalares na rede pública municipal
    if valor < 1:
        return 1
    if valor >= 1 and valor <= 169:
        return 2
    if valor >= 170 and valor <= 248:
        return 3
    if valor >= 249 and valor <= 496:
        return 4
    if valor >= 497 and valor <= 887:
        return 5
    if valor >= 888 and valor <= 1199:
        return 6
    if valor >= 1200:
        return 7
    return 1


def maturidade_3096(valor):
    # 3096 Médicos disponíveis na rede pública municipal
    if valor < 1:
        return 1
    if valor >= 1 and valor <= 72:
        return 2
    if valor >= 73 and valor <= 103:
        return 3
    if valor >= 104 and valor <= 134:
        return 4
    if valor >= 135 and valor <= 164:
        return
    if valor >= 165 and valor <= 194:
        return 6
    if valor >= 195:
        return 7
    return 1


def maturidade_3125(valor, nivel_topico=5):
    # 3125 Prontuário eletrônico
    if valor == 0:
        return 1
    if valor == 1:
        return 3
    if valor == 2:
        return 4
    if valor == 2 and nivel_topico >= 5:
        return nivel_topico
    return 1


def maturidade_4004(valor):
    # 4004 Serviços on-line de saúde oferecidos aos pacientes
    if valor == 0:
        return 2
    if valor >= 1 and valor <= 3:
        return 3
    if valor == 4 or valor == 5:
        return 4
    if valor == 6:
        return 5
    if valor == 7:
        return 6
    if valor == 8:
        return 7
    return 1


def maturidade_4021(valor):
    # 4021 Índice de risco e proteção à saúde dos nascidos vivos
    if valor > .004:
        return 1
    if valor <= .039 and valor >= .0018:
        return 2
    if valor <= .001799 and valor >= .0013:
        return 3
    if valor <= .001299 and valor >= .00095:
        return 4
    if valor <= .000949 and valor >= .00055:
        return 5
    if valor <= .000549 and valor >= .00015:
        return 6
    if valor <= .000149:
        return 7
    return 1


# Segurança pública
def maturidade_3048(valor):
    # 3048 Soluções em monitoramento para a segurança pública
    if valor == 0:
        return 2
    if valor == 1:
        return 3
    if valor == 2:
        return 4
    if valor == 3:
        return 5
    if valor == 4:
        return 6
    if valor == 5:
        return 7
    return 1


def maturidade_4016(valor):
    # 4016 Taxa de homícidio
    if valor > .92:
        return 1
    if valor <= .9199 and valor >= .316:
        return 2
    if valor <= .3159 and valor >= .2238:
        return 3
    if valor <= .2237 and valor >= .141:
        return 4
    if valor <= .1409 and valor >= .071:
        return 5
    if valor <= .0709 and valor >= .0199:
        return 6
    if valor <= .0198:
        return 7
    return 1


def maturidade_4017(valor):
    # 4017 Políticas públicas e ações para segurança pública
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2 or valor == 3:
        return 3
    if valor == 4 or valor == 5:
        return 4
    if valor == 6 or valor == 7:
        return 5
    if valor == 8:
        return 6
    if valor > 8:
        return 7
    return 1

# Água e Esgoto


def maturidade_3024(valor):
    # 3024 Índice de volume de esgoto coletado
    if valor < .3651:
        return 1
    if valor >= .3652 and valor <= .5310:
        return 2
    if valor >= .5311 and valor <= .6376:
        return 3
    if valor >= .6377 and valor <= .7843:
        return 4
    if valor >= .7844 and valor <= .8702:
        return 5
    if valor >= .8703 and valor <= .99:
        return 6
    if valor >= .9901:
        return 7
    return 1


def maturidade_3028(valor):  # Esse calculo usa um intervalo que nao ficou entendido como aplicar
    # 3028 Consumo médio per capita de água
    if valor < 50:
        return 1


def maturidade_3042(valor):
    # 3042 Soluções inteligentes para gestão na distribuição e consumo de água
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3:
        return 4
    if valor == 4:
        return 5
    if valor == 5:
        return 6
    if valor == 6:
        return 7
    return 1


def maturidade_3110(valor):
    # 3110 Índice de perdas na distribuição de água
    if valor > .9443:
        return 1
    if valor <= .9442 and valor >= .4348:
        return 2
    if valor <= .4347 and valor >= .384:
        return 3
    if valor <= .3859 and valor >= .325:
        return 4
    if valor <= .3249 and valor >= .2078:
        return 5
    if valor <= .2077 and valor >= .0009:
        return 6
    if valor <= .0008:
        return 7
    return 1


def maturidade_4047(valor):
    # 4047 Índice de volume de esgoto tratado
    if valor < .0009:
        return 1
    if valor >= .001 and valor <= .23:
        return 2
    if valor >= .2301 and valor <= .4629:
        return 3
    if valor >= .463 and valor <= .6999:
        return 4
    if valor >= .7 and valor <= .85:
        return 5
    if valor >= .8501 and valor <= .99:
        return 6
    if valor >= .9901:
        return 7
    return 1


# Áreas Verdes
def maturidade_4030(valor):
    # 4030 Proteção e gestão do meio ambiente e áreas verdes do município
    if valor == 0:
        return 1
    if valor == 1 or valor == 2:
        return 2
    if valor == 3 or valor == 4:
        return 3
    if valor == 5 or valor == 6:
        return 4
    if valor == 7 or valor == 8:
        return 5
    if valor == 9 or valor == 10:
        return 6
    if valor > 10:
        return 7
    return 1


# Energia
def maturidade_3043(valor):
    # 3043 Soluções inteligentes para gestão do consumo de energia elétrica
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3 or valor == 4:
        return 4
    if valor >= 5 and valor <= 7:
        return 5
    if valor == 8:
        return 6
    if valor == 9:
        return 7
    return 1


def maturidade_3069(valor, nivel_topico=1):
    # 3069 Soluções para telegestão da iluminação pública
    if valor == 0:
        return 1
    if valor >= 1:
        return nivel_topico


# Qualidade do ar

def maturidade_3056(valor):
    # 3056 Soluções em monitoramento de gases de efeito estufa e qualidade do ar
    if valor == 0:
        return 1
    if valor == 1 or valor == 2:
        return 2
    if valor == 3 or valor == 4:
        return 3
    if valor == 5 or valor == 6:
        return 4
    if valor == 7 or valor <= 9:
        return 5
    if valor >= 10 and valor <= 13:
        return 6
    if valor >= 13:
        return 7
    return 1


def maturidade_3113(valor, nivel_topico=4):
    # 3113 Monitoramento da qualidade do ar
    if valor == 0:
        return 1
    if valor == 1:
        return 2
    if valor == 2:
        return 3
    if valor == 3:
        return 4
    if valor == 4:
        return 5
    if valor == 4 and nivel_topico < 4:
        return 4
    if valor == 4 and nivel_topico >= 4:
        return nivel_topico
    return 1


# Gestão de recursos

def maturidade_4007(valor):
    # 4007 Percentual de material recolhido pela coleta seletiva
    if valor < .01:
        return 1
    if valor >= .011 and valor <= .02:
        return 2
    if valor >= .021 and valor <= .03:
        return 3
    if valor >= .031 and valor <= .0899:
        return 4
    if valor >= .09 and valor <= .2599:
        return 5
    if valor >= .8501 and valor <= .4999:
        return 6
    if valor >= .5:
        return 7
    return 1


def maturidade_4014(valor, nivel_topico=4):
    # 4014 Soluções inteligentes para otimização da coleta de resíduos
    if valor == 0:
        return 2
    if valor == 1:
        return 3
    if valor == 2:
        return 4
    if valor == 3:
        return 5
    if valor == 4:
        return 6
    if valor == 4 and nivel_topico >= 4:
        return nivel_topico
    return 1


lista_maturidade = [
    maturidade_3117,
    maturidade_3127,
    maturidade_3141,
    maturidade_3027,
    maturidade_3122,
    maturidade_3020,
    maturidade_4041,
    maturidade_4045,
    maturidade_3049,
    maturidade_3076,
    maturidade_3124,
    maturidade_4011,
    maturidade_4031,
    maturidade_4046,
    maturidade_4005,
    maturidade_3021,
    maturidade_3022,
    maturidade_3040,
    maturidade_3041,
    maturidade_3134,
    maturidade_4035,
    maturidade_4036,
    maturidade_4024,
    maturidade_4025,
    maturidade_4032,
    maturidade_4033,
    maturidade_3016,
    maturidade_4010,
    maturidade_4012,
    maturidade_3004,
    maturidade_3033,
    maturidade_3003,
    maturidade_3011,
    maturidade_3086,
    maturidade_3115,
    maturidade_4006,
    maturidade_4020,
    maturidade_4034,
    maturidade_4037,
    maturidade_4048,
    maturidade_3077,
    maturidade_3107,
    maturidade_3123,
    maturidade_4040,
    maturidade_3006,
    maturidade_3095,
    maturidade_3096,
    maturidade_3125,
    maturidade_4004,
    maturidade_4021,
    maturidade_3048,
    maturidade_4016,
    maturidade_4017,
    maturidade_3007,
    maturidade_4042,
    maturidade_3039,
    maturidade_4039,
    maturidade_4043,
    maturidade_4044,
    maturidade_3103,
    maturidade_3147,
    maturidade_3024,
    maturidade_3028,
    maturidade_3042,
    maturidade_4047,
    maturidade_4007,
    maturidade_4014,
    maturidade_4030,
    maturidade_3056,
    maturidade_3113,
    maturidade_3043,
    maturidade_3069,
    maturidade_3125]
