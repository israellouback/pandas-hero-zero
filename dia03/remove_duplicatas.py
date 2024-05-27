#%%
import pandas as pd
# %%
data = { "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"], 
        "Idade": [32,33,2,33,31,32], 
        "updated_at":[1,2,3,1,2,3] 
        }
        

# %%
df = pd.DataFrame(data)

# %%
#Ordena o df antes de dropar duplicatas, na ordem DECRESCENTE para ele poder dropar o ultimo
df = df.sort_values(by="updated_at",ascending=False)
df
#%%
#Removendo duplicatas onde são consideradas as colunas do argumento subset 
#argumento keep diz qual instancia duplicada manter
df = df.drop_duplicates(subset=["Nome","Idade"],keep='first')
df

