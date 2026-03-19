import pandas as pd

dados_ibge = pd.read_csv('dados.csv')
print(dados_ibge.head()) # aqui, .head() irá exibir as 5 primeiras linhas de dados do arquivo.csv

print(dados_ibge) # aqui o código, "pd.read_csv", uma sintaxe do pandas que permite ler arquivos DATAFRAME (JSON, CSV e etc)

# ---------
# Separando os dados por coluna:

print(sorted(dados_ibge['UF'].unique().tolist())) # aqui, separei para visualizar apenas a coluna 'UF', em ordem do menor pro maior.
print(sorted(dados_ibge['Anos de Estudo'].unique().tolist()))
print(sorted(dados_ibge['Sexo'].unique().tolist()))
print(sorted(dados_ibge['Cor'].unique().tolist()))

# ----------
# Vizualizando qual é o menor dado e o maior dado de determinada coluna ( idade )
print('A menor idade é: ', dados_ibge.Idade.min())
print('A menor idade é: ', dados_ibge.Idade.max())