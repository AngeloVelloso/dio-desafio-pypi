# portal_sped

Description. 
The package portal_sped is used to:
	- get_table_sped: download a table from site (Public Tables for use in SPED)[http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal&msclkid=1cca5d23bdc411ecb3bab3d8d466c5b9].
	- transform_dataframe: made a dataframe with the information downloaded above.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install get_table_sped.

```bash
pip install get_table_sped
```

## Usage

```python
from get_table_sped.utils import tabela_sped
tabela_sped.get_table_sped(29, 53)
```

Above command will download table for RO.

## Author
Ângelo Velloso

## License
[MIT](https://choosealicense.com/licenses/mit/)