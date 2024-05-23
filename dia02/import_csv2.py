#%%
import pandas as pd
# %%
df = pd.read_csv("..\data\data\products.csv",sep= ';',
                 names = ["ID","Name","Description"]) # o df nao tinha cabeçalho, foi preciso criar
df
# %%
#Renomear colunas 'Name' e 'Description'
df.rename(columns={"Name":"Nome",
                "Description":"Descricao"},inplace=True)
                  
df
# %%
