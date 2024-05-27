#%%
import pandas as pd
#Exercicio: Pegar a ultima transacao de cada IdCustomer
#Resolucao: ordenar o campo 'DataTransaction' ordem decrescente e dropar duplicatas
# do IdCustomer

# %%
df = pd.read_excel('../data/ptransactions.xlsx')
df
# %%
df_last = (df.sort_values(by="DtTransaction",ascending=False).
drop_duplicates(subset="IdCustomer",keep='first'))
df_last
# %%
#Método nunique conta quantos unicos temos na coluna
df_last['IdCustomer'].nunique()
# %%
#Encontrar um IdCustomer especifico
condicao =  df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df[condicao]
# %%
#Encontrar um  ultimo transacao de um IdCustomer especifico
condicao =  df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_last[condicao]
# %%
