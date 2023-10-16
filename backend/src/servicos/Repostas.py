import pandas as pd
from decouple import config
from io import StringIO
import httpx


class Resposta:
    """Leitor dos dados de variaveis. Trata as entradas pada """

    def __init__(self):
        self.url = config("DRIVE_FORM_FILE")
        self.order_fields = ['EST01', 'EST02']
        self.df_variaveis = pd.DataFrame(columns=['id', 'nome', 'valor'])
        self.dict_variaveis = {}

    def reader(self):
        self.df_variaveis = pd.read_csv(StringIO(httpx.get(self.url).text))

    def treat_order_fields(self, field):
        cols = [col for col in self.df_variaveis if col.startswith(field)]
        df_aux = self.df_variaveis[cols]
        df_aux1 = pd.DataFrame(columns=[field])

        for idx, row in df_aux.iterrows():
            df_aux1 = pd.concat(
                [df_aux1, pd.DataFrame({field: [[val for val in row]]})])

        self.df_variaveis[field] = df_aux1
        self.df_variaveis.drop(cols, inplace=True, axis=1)

    def treat_reg_fields(self, var):
        self.df_variaveis[var] = self.df_variaveis[var].apply(
            lambda x: x.split(','))

    def treat_vars(self):
        self.reader()
        for var in self.order_fields:
            self.treat_order_fields(var)
        other_cols = [col for col in self.df_variaveis if col not in self.order_fields
                      and col not in ['Carimbo de data/hora', 'Observação:', 'E-mail', 'Município']]
        for var in other_cols:
            if self.df_variaveis[var].dtype == 'float64':
                self.df_variaveis[var] = pd.NA
            else:
                self.treat_reg_fields(var)
        self.df_variaveis.rename(columns={
                                 'Carimbo de data/hora': 'atualizacao_dia', 'Município': 'municipio'}, inplace=True)
        self.df_variaveis.drop(['Observação:', 'E-mail'], axis=1, inplace=True)
        self.dict_variaveis = self.df_variaveis.to_json(orient='records')

    def get_capacidade(self, prefix):
        self.treat_vars()
        cols = [col for col in self.df_variaveis if col.startswith(
            prefix)] + ['municipio']
        self.df_variaveis['update_date'] = pd.to_datetime(
            self.df_variaveis['atualizacao_dia'], format='%d/%m/%Y %H:%M:%S')
        df_aux = self.df_variaveis[self.df_variaveis.groupby(
            'municipio').update_date.transform('max') == self.df_variaveis['update_date']][cols]

        return df_aux.to_dict(orient='records')
