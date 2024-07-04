# %%
import pandas as pd
import os
#Funcao que recebe o caminho e cria um df com nome de acordo com ultima parte da string do arquivo
#e usa [cod,nome,periodo] como index para depois fazer a concatencao por eles
def import_etl(path:str):

    name = path.split("/")[-1].split(".")[0]

    df = (pd.read_csv(path, sep=';')
            .rename(columns={"valor":name})
            .set_index(["cod","nome","período"]))
    
    return df

# %%
#lista os arquivos no caminho
path = "../data/ipea/"
files = os.listdir(path)
#cria uma lista para armazenar os dfs
dfs = []
for i in files:
    dfs.append(import_etl(path+i))
    #adiciona os dfs na lista após serem criados na funcao

df_bia = pd.concat(dfs, axis=1).reset_index()
#concatena todos dfs da lista resettando os indices
df_bia.to_csv("../data/bia_consolidado.csv", sep=";", index=False)
#salve o df para csv