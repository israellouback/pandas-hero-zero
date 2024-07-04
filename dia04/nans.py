# NA são dados FALTANTES

# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}

df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum()
#Para sabermos a quantidade de NA's numa coluna é só somarmos todos NA

# %%
df.isna().sum() 
#Para sabermos a quantidade de NA's num DF é só somarmos todos NA

# %%
df.isna().mean()
# Taxa de NA's de cada coluna (PORCENTAGEM DE NAN NA COLUNA)
#Se você tem um CONJUNTO DE VALROES BINARIO (0,1)
# A MEDIA É A PROPORCAO DE 1 NESSE CONJUNTO
# %%
df.fillna({
        "idade": df["idade"].mean(),
        "renda":df["renda"].mean(),
        })
#O [fillna] SERVE PARA PREENCHER VALORES NULOS
# ATRIBUIMOS A MEDIA DAS COLUNAS NO LUGAR DOS NA'S

# %%
df.dropna(subset=["idade", "renda"], how='any')
#Dropa linha que tem NA nas colunas do subset dos de acordo com parametro how

# %%
df.dropna(axis=1, thresh=3)
#axis=1 avalia colunas ; 0= linhas
#thresh = 3 - Aceita até 3 valores nao nulos para manter a coluna