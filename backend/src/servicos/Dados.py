import pandas as pd
from decouple import config
import json

class DadosIndicadores:

    def __init__(self):
        self.url = config("DRIVE_FILE")
        self.df_indicadores = pd.DataFrame(columns=['id', 'dimensao', 'componente'])
        self.dict_indicadores = {}

    def column_cleaner(self, col):
        self.df_indicadores[col] = self.df_indicadores[col].str.replace(r'^[0-9\.\s\-]+', '', regex=True)

    def reader(self):
        self.df_indicadores = pd.read_csv(self.url)
        self.df_indicadores = self.df_indicadores[['id_chave', 'indicador', 'dimensao', 'componente']]
        self.df_indicadores.columns = ['id', 'nome', 'dimensao', 'topico']
        for column in ['nome', 'dimensao', 'topico']:
            self.column_cleaner(column)
        self.dict_indicadores = self.df_indicadores.to_dict(orient='records')
        return {"indicadores": json.dumps(self.dict_indicadores, ensure_ascii=False)}


if __name__ == "__main__":
    from ast import literal_eval

    ind = DadosIndicadores()
    print(ind)
    resultado = ind.reader()
    print(type(resultado))
    print(literal_eval(resultado['indicadores']),type(literal_eval(resultado['indicadores'])))
