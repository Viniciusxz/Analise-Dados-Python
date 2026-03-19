import pandas as pd

dados_ibge = pd.read_csv('dados.csv')
print(dados_ibge.head())
## print(dados_ibge) # aqui o código, "pd.read_csv", uma sintaxe do pandas que permite ler arquivos DATAFRAME (JSON, CSV e etc)