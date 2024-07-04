#Carregue os dados do arquivo data/ipea/homicidios.csv de forma correta e informe:

#%%
import pandas as pd

# %%
df = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
df
#%%
#Quantidade de linhas e colunas
df.shape
#%%
#Nome da primeira coluna
df.columns[0]
# %%
#Nome da última coluna
df.columns[-1]