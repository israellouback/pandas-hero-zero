#%%
import pandas as pd

# %%
#Utilizando APPLY em um DF utilizando o conceito de RFV (RECENCIA-FREQUENCIA-VALOR) para um CRM

data = { "nome": ["Teo", "Nah", "Maria", "Lara"], 
        "recencia": [1,30,10,45], 
        "valor":[100,2000, 15, 500], 
        "frequencia":[2, 5, 1, 15] }

# %%
df_crm =pd.DataFrame(data)
df_crm
# %%
#Funcao que da uma nota para cada cliente de um DF de acordo com a estrategia aplicada de rfv
#RECENCIA: Data da ultima compra de uma pessoa
#FREQUENCIA: Quantas compras uma pessao fez
#VALOR: Valor gasto total em todas as compras
def rfv(row):
    nota = 0

    if row["recencia"] <=10:
        nota+= 10
    elif 10 < row["recencia"] <= 30:
        nota+= 5
    elif row["recencia"] > 30:
        nota+= 0    

    if row["frequencia"]  > 10:
        nota+= 10
    elif 5 <= row["frequencia"] < 10:
        nota+= 5
    elif row["frequencia"] < 30:
        nota+= 0            

    if row["valor"] > 1000:
        nota+= 10
    elif 100 <= row["valor"] < 1000:
        nota+= 5
    elif row["valor"] < 100:
        nota+= 0           

    return nota

# %%
#Aplica para cada linha a funcao RFV
df_crm['RFV'] = df_crm.apply(rfv, axis = 1)
df_crm

# %%
