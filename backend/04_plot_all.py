import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Carrega e ordena o CSV
df = pd.read_csv("resultados_ordenados.csv")
df_sorted = df.sort_values(by="similar_score", ascending=False)

# Itera pelas 20 primeiras queries
for _, row in df_sorted.drop_duplicates(subset=["query_full_path"]).head(100).iterrows():
    query_full_path = row["query_full_path"]

    # Filtra as 5 similares dessa query
    similares = df_sorted[df_sorted["query_full_path"] == query_full_path].head(5)

    # Carrega a imagem query (original)
    img_query = Image.open(query_full_path)

    # Carrega as imagens similares
    imgs_similares = [Image.open(p) for p in similares["similar_full_path"]]

    # Cria figura
    fig = plt.figure(figsize=(20, 8))

    # Adiciona subplot para query original
    ax_query = fig.add_subplot(2, 1, 1)
    ax_query.imshow(img_query)
    ax_query.set_title(f"Query\n{query_full_path.split('/')[-1]}")
    ax_query.axis('off')

    # Adiciona 5 subplots para similares
    for i, (img, score) in enumerate(zip(imgs_similares, similares["similar_score"])):
        ax = fig.add_subplot(2, 5, 6 + i)  # segunda linha começa em 6
        ax.imshow(img)
        ax.set_title(f"Sim {i+1} (score={score:.3f})\n{similares.iloc[i]['similar_filename']}")
        ax.axis('off')

    plt.tight_layout()
    plt.show()

