# Acervo Suvaco do Cristo

Projeto de extensão da UFRJ para preservar e organizar o acervo histórico do bloco de carnaval **Suvaco do Cristo** (Jardim Botânico, Rio de Janeiro), que anunciou que vai parar de desfilar.

O acervo tem mais de 1.400 itens — fotos, documentos, áudios e vídeos — catalogados a mão numa planilha presente na pasta do Drive "Suvaco do Cristo".
Este repositório guarda o sistema que estamos construindo para catalogar essas mídias: detectar mídias repetidas, sugerir os metadados e, mais pra frente, rotular as imagens automaticamente.

## Como o repositório está organizado

```
backend/    scripts em Python que comparam as imagens e acham as duplicatas.
frontend/   páginas do site de catalogação (HTML e CSS puros) quase prontos.
banco/      estrutura do banco de dados PostgreSQL, que ainda falta colocarmos aqui também.
docs/       guias do grupo (como usar o Git, por exemplo)
```

Cada pasta tem o seu próprio `README.md` explicando como rodar aquela parte.

## Situação de cada parte

| Parte | Situação |
|---|---|
| Backend | Pipeline de similaridade funcionando: gera os vetores das imagens e lista as mais parecidas, precisando apenas ajustar com testes empíricos o limiar de similaridade. |
| Frontend | Três telas prontas (enviar, conferir metadados, listar a base). Ainda não está conversando com o backend, falta fazermos. |
| Banco | PostgreSQL criado pelo Igor, rodando por enquanto na máquina dele. A estrutura das tabelas ainda vai entrar aqui. |

## Equipe

Patrick José M. T. de Carvalho, Yuri Altomare de Carvalho e Igor Queiroz.
Orientação: Paulo Mann.
Artigo de referência: *Preservando o patrimônio do carnaval brasileiro por meio de IA* (2026).
Autor: Matheus Sutino
