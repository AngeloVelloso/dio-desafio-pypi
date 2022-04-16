from mechanize import Browser, Request
from pandas import DataFrame, read_csv, concat, to_datetime
from io import StringIO

class TabelaSPED:

    def __init__:
        self.table = DataFrame()
        self.dados = bytes

    def get_table_sped(self, cod_pacote, cod_tabela):
        br = Browser()
        url = f'http://www.sped.fazenda.gov.br/spedtabelas/appconsulta/obterTabelaExterna.aspx?idPacote={cod_pacote}&idTabela={cod_tabela}'
        
        rqst = Request(url=url, method='GET')
        r = br.open(rqst)

        self.dados = r.read()

        return self.dados

    def transform_dataframe(self, datas):
        self.table = read_csv(
            StringIO(str(self.dados,'cp1252')), 
            sep='|', 
            decimal='.', 
            header=None, 
            skiprows=1,
            parse_dates=datas,
            date_parser=lambda dt: to_datetime(dt, format='%d%m%Y', errors='coerce')
        )

        return self.table