#%%
import pandas as pd
#%%
##Series são como uma coluna do excel
idades = [30,42,90,34]
series_idade =pd.Series(idades,name = 'idades')
series_idade
#%%
# As series possuem varios metodos estatisticos, ai esta vantagem em usa-las no lugar das listas
series_idade.mean()
# %%
series_idade.var()
# %%
series_idade.median()
# %%
# O método describe funciona como uma DESCRIÇÃO da sua série, te fornecendo descrições estatísticas dela 
series_idade.describe()
# %%
# O atributo shape nos da a DIMENSÃO da serie em formato de TUPLA
series_idade.shape

# %%
#Visualiza os indices da serie
series_idade.index
series_idade[2]

# %%
#É possivel alterar os indices da serie
series_idade.index = ['l','b','k','a']
series_idade['a']
# %%
#O método ILOC retorna a POSIÇÃO do elemento na nossa serie
series_idade.iloc[0]
series_idade.iloc[0:4]

# %%
#O método LOC retorna o  ÍNDICE do elemento na nossa série
series_idade.loc['l']
series_idade.loc['l':'k']
# %%
# É possivel nomear as series com metodo name
series_idade.name = 'idades_familia'
series_idade

# %%
