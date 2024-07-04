# %%
#Objetivo do stack é reduzir colunas (dimensionalidade) e aumentar linhas (EMPILHAR)
#Neste exemplo, o csv contem muitas colunas com diferentes tipos de homicidios
#Neste caso é criado uma coluna com  uma FLAG para cada tipo de homicidio
#Objetivo do unstack é DESEMPILHAR, aumentando as colunas (dimensionalidade)
#Necessario sempre fazer o set_index antes do stack
#Necessario sempre fazer o droplevel depois do unstack para setar as colunas
import pandas as pd

df = pd.read_csv("../data/bia_consolidado.csv", sep=";")
df

# %%

df = df.set_index(["cod", "nome", "período"])
#O SET INDEX FIXA AS COLUNAS!!
#Lista de colunas que virarão index e PERMANCERAO FIXAS
# %%
df_stack = df.stack().reset_index().rename(columns={"level_3":"Tipo Homicidio",
                                                    0:"Qtde"})
#Faz o stack, resetando os index e renomenado as colunas geradas pela stack

#%%
df_unstack = (df_stack.set_index(['cod','nome','período', 'Tipo Homicidio'])
                      .unstack()
                      .reset_index())
# O unstack faz a VOLTA, DESEMPILHA as linhas, criando COLUNAS
# %%

homicidios = df_unstack['Qtde'].columns.tolist()
indentificadores = df_unstack.columns.droplevel(1).tolist()[:3]

df_unstack.columns = indentificadores + homicidios
df_unstack