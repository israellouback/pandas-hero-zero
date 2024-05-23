#%%
import pandas as pd

# %%
dados = {"nome": ["Téo", "Nah", "Napoleão"],
        "idade": [31, 32, 14]
         }


# %%
df = pd.DataFrame(dados)
df

# %%
#descricao de todas colunas (numericas ou nao)
df.describe(include='all')

# %%
#Media da coluna idade
sumario = df.describe()
sumario['idade']['mean']
# %%
#Ultimo nome da coluna nome
df['nome'].iloc[-1]
# %%
