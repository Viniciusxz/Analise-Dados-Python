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

# ----- 
# Tipos de Variaveis em analise de dados:
# Variavel Qualitativa Nominal = Não existe Hierarquia
# -> Exemplo: Cor, Estado, Gênero.
# Variavel qualitativa Ordinal = Tem uma ordem lógica (Hierarquica)
# -> Exemplo: Escolaridade Fundamental < Médio < Superior
# Variavel Quantitativa Discretas = Números inteiros (contagem)
# - Exemplo: Filhos = 2
# Variavel Quantitativa Contínuas = Números decimais
# - Exemplo: Altura = 1.75

print(dados_ibge['Sexo'].value_counts()) # Aqui, uma sintaxe que irá pegar a coluna 'sexo' e contar quantos registros tem de feminino e masculino (1 e 0)
print(dados_ibge['Sexo'].value_counts(normalize = True)) # A mesma situação que a sintaxe acima, mas nesse, o normalize irá criar uma diferença de porcentagem entre cada genero