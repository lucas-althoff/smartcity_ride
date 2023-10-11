import pandas as pd
from decouple import config
import re
from unidecode import unidecode

class Variaveis:
    """Leitor dos dados de variaveis. Trata as entradas pada """
    def __init__(self):
        self.url = config("DRIVE_FILE")
        self.df_variaveis = pd.DataFrame(columns=['id', 'nome', 'valor'])
        self.dict_variaveis = {}

    def column_cleaner(self, col):
        self.df_variaveis[col] = self.df_variaveis[col].str.replace(r'^[0-9\.\s\-]+', '', regex=True)

    def var_spliter(self, string):
        if len(string) == 1 and re.search(r'^([A-Za-z]+)\.([0-9])\sa\s[A-Za-z]+\.([0-9])', string[0]):
            match = re.search(r'^([A-Za-z]+)\.([0-9])\sa\s[A-Za-z]+\.([0-9])', string[0])
            if match:
                return {f'{match.group(1)}.{x}': None for x in range(int(match.group(2)), int(match.group(3))+1)}
        else:
            var_names = []
            for var in string:
                match = re.search('^([A-Za-z0-9_]+)\s*[=:\-]+.*$', unidecode(var))
                match_1 = re.search('^([A-Za-z0-9_\s\.]+).*$', unidecode(var))
                if match:
                    var_names.append(match.group(1))
                elif match_1:
                    var_name = [x for x in match_1.group(1).split(' ') if x not in ['de', 'por', 'com', 'da', 'ou']][:3]
                    var_names.append('_'.join(var_name))

            return {x: None for x in var_names}

    def read_munic(self):
        self.munic = pd.read_csv(config('MUNIC_FILE')).drop('id', axis=1)

    def reader(self):
        self.df_variaveis = pd.read_csv(self.url)
        self.df_variaveis = self.df_variaveis[['id_chave', 'variaveis']]
        treated_vars = []
        var_names = var.df_variaveis.variaveis.str.split(r'\n')
        for var_name in var_names:
            treated_var = self.var_spliter(var_name)
            treated_vars.append(treated_var)
        self.df_variaveis['variaveis'] = treated_vars
        self.read_munic()
        self.df_variaveis['cross'] = 1
        self.munic['cross'] = 1

        self.df_variaveis = self.df_variaveis.merge(self.munic, on='cross').drop('cross', axis=1)
        # for column in ['nome', 'dimensao', 'topico']:
        #     self.column_cleaner(column)
        self.dict_variaveis = self.df_variaveis.to_dict(orient='records')

        print(self.dict_variaveis)


if __name__ == '__main__':
    var = Variaveis()
    var.reader()