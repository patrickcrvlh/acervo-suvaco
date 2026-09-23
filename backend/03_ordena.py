import pandas as pd
pd.set_option('display.max_columns', None)
# Carrega o CSV
df = pd.read_csv("resultados.csv")

# Ordena decrescente pela coluna 'similar_score'
df_sorted = df.sort_values(by="similar_score", ascending=False)

# Mostrar as primeiras linhas (top 20 por exemplo)
print(df_sorted.head(20))

# Se quiser, salva num novo arquivo ordenado
df_sorted.to_csv("resultados_ordenados.csv", index=False)

