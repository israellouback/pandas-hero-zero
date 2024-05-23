#%%
import pandas as pd

# %%
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
# %%
series_dados = pd.Series(dados)
print("Media dos dados: ",series_dados.mean())
print("Desvio Padrão dos dados: ",series_dados.std())
print("Maior valor dos dados: ",series_dados.max())


# %%
