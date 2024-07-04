# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

condicao = df["IdCustomer"]=="5f8fcbe0-6014-43f8-8b83-38cf2f4887b3"
df_user = df[condicao]
df_user['Points'].sum()
#Total de pontos acumulado pelo usuario da condicao

# %%
#groupby serve para agrupar as coisas
df_summary = df.groupby(["IdCustomer"])["Points"].sum()
#agrupo pelos idcustomer e somo os pontos de todos individuos
# df_summary passa a ser do objeto df.groupby

df_summary.reset_index()
# o reset_index faz com que vire um DF denovo




# %%
#Metodo AGG agrega cada coluna com uma metrica diferente
(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": "max"})
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())

#Agrupando por IDcustomer e AGREGANDO diferentes colunas por diferentes métricas
# com o método AGG
# %%
import datetime

data1 = df["DtTransaction"][0]
now = datetime.datetime.now()

(now - data1).days

#Pegando a quantidade de dias de uma DATA para HOJE
# %%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days


(df.groupby(["IdCustomer"])
   .agg({ "Points": 'sum',
          "UUID": "count",
          "DtTransaction": ['max', recencia]
          })
    .rename(columns={
            "Points":"Valor",
            "UUID": "Frequencia",
            "DtTransaction":"UltimaData"
            })
   .reset_index())
#Agrupar por idCustomer, agregando as colunas por suas metricas
#Em dtTransaction, pegamos a data maxima e a recencia de cada pessoa
# Em ['max', recencia] o parametro recencia é a chamada da funcao recencia
#mas nao eh necessario passar o parametro x pois ele usa o objeto funcao recencia na coluna
# renomeamos as colunas
#e resetamos o index para voltar ao DF