# Backend — similaridade entre as imagens do acervo

Quatro scripts que rodam em sequência. Juntos, eles pegam as fotos do acervo, transformam cada uma num vetor de números com um modelo de visão, e listam, para cada foto, as cinco mais parecidas. É a base da detecção de duplicatas.

## Antes de rodar

1. Instale as bibliotecas:
   ```
   pip install -r requirements.txt
   ```
2. Abra o `01_create_dataset.py` e troque o `caminho_raiz` para a pasta onde **você** guardou as imagens do acervo. As imagens não ficam no repositório.

## Ordem de uso

| Script | O que faz | O que gera |
|---|---|---|
| `01_create_dataset.py` | Percorre a pasta das imagens, descarta arquivo oculto e imagem corrompida, e monta o conjunto de dados. | pasta `suvaco_dataset/` |
| `02_cosine.py` | Passa cada imagem pelo modelo, gera o vetor (embedding) e calcula a similaridade de cosseno entre todas. | `resultados.csv` |
| `03_ordena.py` | Ordena os pares do mais parecido para o menos parecido. | `resultados_ordenados.csv` |
| `04_plot_all.py` | Mostra, para cada imagem, as 5 mais parecidas lado a lado, para conferir no olho. | janelas com as figuras |

Rode sempre de dentro desta pasta:
```
cd backend
python 01_create_dataset.py
python 02_cosine.py
python 03_ordena.py
python 04_plot_all.py
```

Os arquivos gerados (`suvaco_dataset/`, `resultados*.csv`) ficam fora do Git — cada um gera os seus.

## Observações

- O `02_cosine.py` usa o modelo `nateraw/vit-base-beans`. Na primeira vez ele é baixado da internet (algumas centenas de MB).
- Com GPU roda bem mais rápido; sem GPU funciona, só demora.
