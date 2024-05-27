#%%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('../data/customers.csv',sep=';')
df
#%%
df['Points_double'] = df['Points'] * 2
# %%
#Criacao de colunas
df['Points_ratio'] = df['Points_double'] / df['Points']
df['Constante'] = None
df
# %%
#Aplicando o logaritmo em uma coluna
df['Points_log'] = np.log(df['Points'])
df
# %%
#Colocar strings do df em CAPS-LOCK
df["Name"].str.upper()

# %%
#SEPARAR a string por algum caractere
def get_first(x:str): #Retorna a primeira parte da string dividida pelo caractere x
    return x.split("_")[0]
#%%
get_first("Israel_Louback")
# %%
#O metodo .APPLY() APLICA uma funcao em TODOS ELEMENTOS DE UMA COLUNA
df['First_Name'] = df['Name'].apply(get_first) # a funcao nao precisa de parametro pq ela é como objeto
df
# %%
#Funcao LAMBDA: Funcao anonima simples para executar uma vez e rapidamente
get_f = lambda x: x.split("_")[0]
get_f('Israel_louback')
# %%
df['Name'].apply(lambda x: x.split("_")[0])
# %%
#Podemos criar uma funcao para uma nova coluna que ira sumarizar a faixa de pontos
def intervalo_pontos(pontos):
    if pontos < 500:
        return 'baixo'
    elif pontos <1500:
        return 'medio'
    else:
        return 'alto'
df['Faixa_pontos'] = df['Points'].apply(intervalo_pontos)
df   

