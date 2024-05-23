#%%
import pandas as pd

# %%
# Criamos um dicionario para ser nossos dados
#Um DataFrame é um conjunto de séries. Cada coluna comporta como uma série
#É como se series fosse uma coluna, e um df a planilha inteira
data = {
    "nome":["israel","caio","joao","maria"],
    "sobrenome":["louback","cesar","santos","martins"],
    "idade":[23,28,34,45]
}

# %%
#Pegar primeira idade
data["idade"][0]

# %%
#Transformar num DataFrame
df = pd.DataFrame(data)
df
#%%
#Mostra as primeiras 5 linhas do df
df.head(2)

#%%
#Mostra as ultimas 5 linhas do df
df.tail(2)

# %%
#Pegar primeira idade no df
df["idade"].iloc[0]

# %%]
#Pegar coluna de sobrenomes no df
df["sobrenome"]

# %%
#Obter uma LINHA (instancia) do df
df.iloc[0]

# %%
#Obter indices
df.index

# %%
#Obter colunas
df.columns

#%%
#Atribuindo coluna nova
df['peso'] = [70,80,78,90]
df["peso"]

# %%
#O método INFO nos da em texto um resumo do nosso df
# O argumento memory_usage é para ver o consumo de memória do nosso df
df.info(memory_usage='deep')

# %%
#O método DESCRIBE nos da uma cara estatistica de todas colunas NUMERICAS do nosso df
df.describe()

# %%
#o atributo DTYPES nos da os tipos de cada coluna
df.dtypes

