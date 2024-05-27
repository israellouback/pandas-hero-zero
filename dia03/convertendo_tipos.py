#%%
import pandas as pd
# %%
df = pd.read_csv('../data/customers.csv',sep=';')
df
# %%
df.dtypes
# %%
df['Points_double'] = df['Points'] * 2
df

# %%
#Eh possivel passar uma lista de colunas para ele converter
df[['Points','Points_double']].astype(float)
# %%
# %%
