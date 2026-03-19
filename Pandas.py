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
print(dados_ibge['Sexo'].value_counts(normalize = True) * 100) # A mesma situação que a sintaxe acima, mas nesse, o normalize irá criar uma diferença de porcentagem entre cada genero

frequencia = dados_ibge['Sexo'].value_counts()
percentual = (dados_ibge['Sexo'].value_counts(normalize = True)) * 100

dist_freq_qualitativas = pd.DataFrame({'Frequência': frequencia, 'Porcentagem (%)': percentual}) # Criei variaveis para guardar esses dados, depois utilizer pd.DataFrame para criar uma tabela de dicionario para ficar mais formal a apresentação de dados.

dist_freq_qualitativas.rename(index = {0: 'Masculino', 1: 'Feminino'}, inplace = True)
dist_freq_qualitativas.rename_axis('Sexo', axis = 'columns', inplace = True) # Substituindo 0 e 1 por Masculino e Feminino em dicionario respectivamente, e utilizando inplace para salvar a sintaxe.
print(dist_freq_qualitativas)


sexo = {0: 'Masculino',
        1: 'Feminino'}
        
cor = {0: 'Indígena',
        2: 'Branca',
        4: 'Preta',
        6: 'Amarela',
        8: 'Parda',
        9: 'Sem declaração'} # Criação de dicionário com as colunas

frequencia1 = pd.crosstab(dados_ibge.Sexo,
                          dados_ibge.Cor)
frequencia1.rename(index = sexo, inplace = True)
frequencia1.rename(columns = cor, inplace = True)
print(frequencia1)

percentual1 = pd.crosstab(dados_ibge.Sexo,
                          dados_ibge.Cor,
                          normalize = True) * 100
percentual1.rename(index = sexo, inplace = True)
percentual1.rename(columns = cor, inplace = True)
print(percentual1)

percentual1 = pd.crosstab(dados_ibge.Sexo,
                          dados_ibge.Cor,
                          aggfunc = 'mean',
                          values = dados_ibge.Renda)
percentual1.rename(index = sexo, inplace = True)
percentual1.rename(columns = cor, inplace = True)
print(percentual1)