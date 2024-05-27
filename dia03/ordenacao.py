#%%
import pandas as pd

# %%
df = pd.read_csv('../data/customers.csv',sep=';')
df
# %%
#Ordenar pela coluna POINTS em ordem DECRESCENTE e NAME pela ordem CRESCENTE
df.sort_values(by=["Points","Name"],ascending=[False,True])

#%%
#Ordenar pela ordem DESCRESCENTE de Points e renomea colunas
#Como sort_values cria outro DF, devemos salva-lo no original
df = (df.sort_values(by="Points",ascending=False)
      .rename(columns={"Name":"Nome","Points":"Pontos"}))
df
