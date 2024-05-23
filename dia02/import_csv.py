#%%
import pandas as pd
# %%
#Leitura de arquivo csv
df_customers = pd.read_csv("..\data\data\customers.csv",sep=";")
df_customers

# %%
# Quando se filtra um df, é passado a referência do df original para o filtro, e quaisquer
# alteracoes podem impactar no df original. Quando se vai filtrar um df pra depois manipular os dados
# é melhor usar o método -> .copy(), para criar um novo objeto e guardar esse df

#Dimensao das linhas e colunas dos nossos dados
df_customers.shape

# %%
#Informacoes dos dados
df_customers.info(memory_usage='deep')

# %%
#Altera campo Points de object para int
df_customers["Points"].astype(int)

# %%
df_customers["Points"].describe()
# %%
#É possivel fazer operacoes aritmeticas/vetorias/escalares na colunas
df_customers["Points"] + 1000
df_customers["Points"] - 1000
df_customers["Points"] * 1000
df_customers["Points"] / 1000

# %%
#Tambem é possivel fazer operacos logicas
df_customers["Points"] >  1000

# %%
#E possivel criar uma condicao, e passar essa condicao para POSICAO do seu df, e ele retornará apenas as linhas TRUE
            #! EH ASSIM QUE EH FEITO FILTRO EM PANDAS!
condicao = df_customers["Points"] >  1000
df_customers[condicao]

# %%
#Descobrir quem tem maior pontuacao nos nossos dados
condicao = df_customers['Points'] == df_customers['Points'].max()
df_customers[condicao]

# %%
#E pra pegar apenas o nome do usuario que tem maior ponto
df_customers[condicao]["Name"].iloc[0]
# %%
#Filtrar quem tem entre 1k e 2k de pontos
condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"]<= 2000)
df_customers[condicao]
# %%
#Metodo ->.COPY() para criar outro dataframe, e nao manipular o original
df_add1k = df_customers[condicao].copy() #faço uma copia do dataframe, criando outro objeto
df_add1k['Points'] = df_add1k["Points"] + 1000
df_add1k

# %%
#Selecionar APENAS ALGUMAS COLUNAS DO DF
colunas = ['UUID','Name']
df_customers[colunas]

# %%
#ORDENACAO dos NOMES das colunas em ORDEM ALFABETICA no DF
colunas = df_customers.columns.tolist() # jogo as colunas do meu df pra uma lista
colunas.sort()
#Atribuo ao meu df as colunas ordenadas
df_customers = df_customers[colunas]
df_customers

# %%
#Renomear colunas (RENAME GERA UM DF NOVO) é preciso usar o argumento inplace=TRUE para reescrever o df original
df_customers.rename(columns={"Name":'Nome',
                             "Points":"Pontos"},inplace=True)
# %%
