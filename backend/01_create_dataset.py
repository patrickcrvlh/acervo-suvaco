import os
from PIL import Image
from datasets import Dataset, Features, Value, Image as HFImage

caminho_raiz = os.path.expanduser("~/Documentos/Suvaco")
extensoes_imagens = (".jpg", ".jpeg", ".png", ".bmp", ".JPG", ".JPEG", ".PNG", ".BMP")

"""
OBSERVACAO: MUDAR O CAMINHO RAIZ PRA ONDE VOCÊ TEM AS IMAGENS DO SUVACO.
"""

def is_image_valid(path):
    """
    Função pra verificar se não tem algo de errado na imagem.
    Verifica integridade do arquivo
    EX: Truncado ou corrompido
    """
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception:
        return False

"""
Essa parte agora é para verificar se o arquivo começa com '.' ou '.__' /oculto, pois o modelo não consegue usar essa foto.
Vamos adicionar no dataset apenas imagens nos formatos selecionados.
"""
dados = []
for dirpath, _, filenames in os.walk(caminho_raiz):
    for nome_arquivo in filenames:
        base = os.path.basename(nome_arquivo)
        if base.startswith(".") or base.startswith("._"):
            continue
        if nome_arquivo.endswith(extensoes_imagens):
            caminho_completo = os.path.join(dirpath, nome_arquivo)
            if is_image_valid(caminho_completo):
                pasta_mae = os.path.basename(os.path.dirname(caminho_completo))
                dados.append({
                    "image": caminho_completo,
                    "label": pasta_mae,
                    "filename": nome_arquivo,
                    "full_path": caminho_completo,
                    })

features = Features({
    "image": HFImage(), # HFImage() - 'imagem' pro modelo
    "label": Value("string"),
    "filename": Value("string"),
    "full_path": Value("string"),
    })
dataset = Dataset.from_list(dados).cast(features)

dataset_dir = os.path.join(os.getcwd(), "suvaco_dataset")
dataset.save_to_disk(dataset_dir)

print(f"Dataset salvo com sucesso em: {dataset_dir}")


