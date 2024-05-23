#%%
import pandas as pd

# %%
df = pd.read_excel('..\data\data\ptransactions.xlsx')
df
# %%
df.head()
# %%
df.tail(10)
# %%
#ORDENACAO DAS COLUNAS EM ORDEM ESTABELECIDAS NA VARIAVEL COLUNAS
colunas = ['UUID','Points','IdCustomer','DtTransaction']
df=df[colunas]
df
# %%
df.info(memory_usage='deep')
# %%
