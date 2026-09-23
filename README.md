# Acervo Suvaco do Cristo

Projeto de extensão da UFRJ para preservar e organizar o acervo histórico do bloco de carnaval **Suvaco do Cristo** (Jardim Botânico, Rio de Janeiro), que anunciou que vai parar de desfilar.

O acervo tem mais de 1.400 itens — fotos, documentos, áudios e vídeos — catalogados a mão numa planilha. Este repositório guarda o sistema que estamos construindo para catalogar essas mídias com apoio de inteligência artificial: detectar mídias repetidas, sugerir os metadados e, mais pra frente, rotular as imagens automaticamente.

## Como o repositório está organizado

```
backend/    scripts em Python que comparam as imagens e acham as parecidas
frontend/   páginas do site de catalogação (HTML e CSS puros)
banco/      estrutura do banco de dados PostgreSQL
docs/       guias do grupo (como usar o Git, por exemplo)
```

Cada pasta tem o seu próprio `README.md` explicando como rodar aquela parte.

## Situação de cada parte

| Parte | Situação |
|---|---|
| Backend | Pipeline de similaridade funcionando: gera os vetores das imagens e lista as mais parecidas. |
| Frontend | Três telas prontas (enviar, conferir metadados, listar a base). Ainda não conversa com o backend. |
| Banco | PostgreSQL criado, rodando por enquanto na máquina de um integrante. A estrutura das tabelas ainda vai entrar aqui. |

## Equipe

Patrick José M. T. de Carvalho, Yuri Altomare de Carvalho e Igor Queiroz.
Orientação: Paulo Mann.
Artigo de referência: Matheus Sutino *et al.*, *Preservando o patrimônio do carnaval brasileiro por meio de IA* (2026).

## Antes de contribuir

Leia [`docs/COMO_USAR_O_GIT.md`](docs/COMO_USAR_O_GIT.md). Resumo das regras:

1. Ninguém faz commit direto na `main`. Cada tarefa ganha um branch próprio.
2. Sempre `git pull` antes de começar a mexer.
3. Senha, foto do acervo e planilha **nunca** sobem. O `.gitignore` já barra, mas confira o `git status` antes de cada commit.
