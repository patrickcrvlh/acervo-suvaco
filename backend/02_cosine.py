import os
import csv
import torch
from PIL import Image
from datasets import load_from_disk
from transformers import AutoImageProcessor, AutoModel
from tqdm.auto import tqdm

"""
ORIENTACOES
DATASET DEVE SER CRIADO PREVIAMENTE NO MESMO DIRETORIO
"""

dataset_dir = "suvaco_dataset"
dataset = load_from_disk(dataset_dir)

"""
Carregando modelo vit-base-beans e preparando
"""
model_ckpt = "nateraw/vit-base-beans"
image_processor = AutoImageProcessor.from_pretrained(model_ckpt)
model = AutoModel.from_pretrained(model_ckpt)

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

"""
Imagem -> Embedding
"""

def transformation_chain(image):
    """
    Se não fizer esse if image.mode != "RGB" o código não roda com todas as imagens do Suvaco.

    
    Passa a imagem pelo processor do modelo
    """
    if image.mode != "RGB":
        image = image.convert("RGB")
    return image_processor(image, return_tensors="pt").pixel_values.squeeze(0)

def extract_embeddings(model):
    """
    Serve para o map() extrair embeddings de batches de imagens.
    """
    def pp(batch):
        images = batch["image"]
        batch_transformed = torch.stack([transformation_chain(img) for img in images])
        batch_transformed = batch_transformed.to(device)

        with torch.no_grad():
            embeddings = model(**{"pixel_values": batch_transformed}).last_hidden_state[:, 0].cpu()
        return {"embedding": [emb.tolist() for emb in embeddings]}
    return pp


"""
Trecho que extrai os embeddings
"""
batch_size = 32 # Definindo batch_size
extract_fn = extract_embeddings(model)

embedding_ds = dataset.map(
        extract_fn,
        batched=True,
        batch_size=batch_size,
        remove_columns=["image"]
)

all_embeddings = torch.tensor(embedding_ds["embedding"])

print(f"[+] Embeddings extraídos de {len(all_embeddings)} imagens.")

"""
Computando similaridade por cossenos
"""

def compute_scores(emb_one, emb_two):
    """
    Cosseno entre dois vetores
    """
    return torch.nn.functional.cosine_similarity(emb_one, emb_two).cpu().numpy().tolist()

def fetch_similar(idx_query, top_k=5):
    """
    Retorna os top 5 mais similares para uma query de índice 'idx_query'
    """
    query_embedding = all_embeddings[idx_query].unsqueeze(0)
    sim_scores = compute_scores(all_embeddings, query_embedding)
    
    sim_scores[idx_query] = -float('inf')  # Não considerar a própria imagem
    
    scored_indices = sorted(range(len(sim_scores)), key=lambda i: sim_scores[i], reverse=True)
    return scored_indices[:top_k], [sim_scores[i] for i in scored_indices[:top_k]]

"""
Salvando todos os resultados em um CSV
query_label, query_filename, query_fullpath, similar_label, similar_filename, similar_full_path, similar_score
"""

saida = "resultados.csv"

with open(saida, mode="w", newline ="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "query_label",
        "query_filename",
        "query_full_path",
        "similar_label",
        "similar_filename",
        "similar_full_path",
        "similar_score"
    ])

    for idx in tqdm(range(len(embedding_ds)), desc="Gerando Similaridades"):
        query_label = embedding_ds[idx]["label"]
        query_filename = embedding_ds[idx]["filename"]
        query_full_path = embedding_ds[idx]["full_path"]

        sim_ids, sim_scores = fetch_similar(idx, top_k=5)

        for sim_idx, sim_score in zip(sim_ids, sim_scores):
            sim_label = embedding_ds[sim_idx]["label"]
            sim_filename = embedding_ds[sim_idx]["filename"]
            sim_full_path = embedding_ds[sim_idx]["full_path"]

            writer.writerow([
                query_label,
                query_filename,
                query_full_path,
                sim_label,
                sim_filename,
                sim_full_path,
                f"{sim_score:.4f}"
            ])

print(f"CSV salvo em: {saida}.")

