#%%
import pandas as pd

# %%
#O FORMATO PARQUET É UM ARQUIVO BINARIO OTIMIZADO PARA  O CUSTO DE ARMAZENAMENTO
df = pd.read_parquet("..\data\data\ptransactions_cart.parquet")
df

# %%
