# %%
import pandas as pd

df_customer = pd.read_csv("../data/customers.csv", sep=";")
df_customer

# %%
df_transactions = pd.read_excel("../data/transactions.xlsx")
df_transactions

# %%
df_transactions_product = pd.read_parquet("../data/transactions_cart.parquet")
df_transactions_product

# %%
df_join = (df_transactions.merge(df_customer,
                                how="inner",
                                left_on="IdCustomer",
                                right_on="UUID",
                                suffixes=["_transacao", "_cliente"]) # renomeam colunas que tem o mesmo nome nos 2 dfs
                          .merge(df_transactions_product,
                                 how='inner',
                                 left_on="UUID_transacao",
                                 right_on="IdTransaction")
                                 )

df_join
#df_join armazena o resultado de 2 merges encadeados.