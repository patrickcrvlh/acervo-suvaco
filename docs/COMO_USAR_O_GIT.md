# Como usar o Git neste projeto

Guia curto para o grupo. Se for a primeira vez, leia inteiro uma vez; depois use a **cola** no final.

---

## 1. Três ideias que explicam quase tudo

**Repositório** é a pasta do projeto com um histórico embutido. O GitHub guarda a cópia central; cada um tem uma cópia completa no próprio computador.

**Commit** é uma foto do projeto num momento, com uma mensagem dizendo o que mudou. O histórico é a sequência dessas fotos. Nada se perde: dá para voltar a qualquer uma.

**Branch** (ramo) é uma linha paralela de trabalho. A `main` é a versão oficial. Cada tarefa ganha um branch próprio, e só entra na `main` depois de revisada. É isso que deixa três pessoas mexerem ao mesmo tempo sem se atropelar.

---

## 2. Configurar uma vez só, em cada computador

Confira se o Git está instalado:
```
git --version
```
Se aparecer um erro, instale em https://git-scm.com (no Windows, pode aceitar todas as opções padrão).

Diga ao Git quem você é. **Use o mesmo e-mail da sua conta do GitHub**, senão seus commits não aparecem com o seu nome:
```
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
git config --global init.defaultBranch main
```

## 3. Baixar o repositório (uma vez)

```
git clone https://github.com/patrickcrvlh/acervo-suvaco.git
cd acervo-suvaco
```

> Por enquanto o repositório fica na conta do Patrick. Quando o repositório oficial do projeto existir, ele será transferido para a organização `suvaco-do-cristo` com todo o histórico. Aí cada um atualiza o endereço com:
> `git remote set-url origin https://github.com/suvaco-do-cristo/acervo-suvaco.git`

Na primeira vez que o Git precisar falar com o GitHub, abre uma janela no navegador pedindo para você entrar na sua conta. Isso é normal — o GitHub não aceita mais a senha digitada no terminal.

---

## 4. O ciclo de todo dia

Toda tarefa segue a mesma sequência. Decore esta:

```
git switch main                 # 1. volta para a versão oficial
git pull                        # 2. baixa o que os outros subiram
git switch -c patrick/nome-da-tarefa   # 3. cria o seu branch

   ... trabalha nos arquivos ...

git status                      # 4. vê o que mudou
git add backend/02_cosine.py    # 5. escolhe o que vai no commit
git commit -m "backend: troca o modelo de embeddings"   # 6. salva a foto
git push -u origin patrick/nome-da-tarefa               # 7. sobe o branch
```

Depois do passo 7, abra o repositório no GitHub. Vai aparecer um botão **Compare & pull request**. Clique, escreva o que você fez, e peça para outro integrante revisar. Quando ele aprovar, clique em **Merge**. Pronto: está na `main`.

### O que cada comando faz

| Comando | O que faz |
|---|---|
| `git status` | Mostra o que mudou e o que já está marcado para o commit. **Rode antes de todo commit.** |
| `git add arquivo` | Marca aquele arquivo para entrar no próximo commit. `git add .` marca tudo — use só depois de olhar o `status`. |
| `git commit -m "..."` | Salva a foto com a mensagem. |
| `git push` | Envia seus commits para o GitHub. |
| `git pull` | Baixa os commits dos outros e junta com os seus. |
| `git switch nome` | Muda para outro branch. |
| `git switch -c nome` | Cria um branch novo e já muda para ele. |

---

## 5. Regras do grupo

1. **Nunca commitar direto na `main`.** Tudo passa por branch e pull request.
2. **Nome de branch:** `seu-nome/o-que-faz`. Exemplo: `yuri/busca-no-banco`.
3. **Mensagem de commit** começa pela parte que mudou: `backend:`, `frontend:`, `banco:` ou `docs:`. Depois, em português, o que mudou — no presente, curto. Exemplo: `frontend: adiciona campo de ano do desfile`.
4. **Um commit, uma ideia.** Se você mudou duas coisas sem relação, faça dois commits.
5. **Nunca sobe:** senha (`.env`), foto do acervo, planilha, arquivo gerado pelos scripts. O `.gitignore` barra, mas confira o `git status`.

---

## 6. Quando dá conflito

Conflito acontece quando duas pessoas mudaram **a mesma linha** do mesmo arquivo. O Git não sabe qual das duas vale e pede para você decidir. Não é erro, é uma pergunta.

O arquivo fica assim:
```
<<<<<<< HEAD
titulo = "Acervo do Suvaco"
=======
titulo = "Acervo Suvaco do Cristo"
>>>>>>> yuri/ajusta-titulo
```

Em cima, a sua versão; embaixo, a do outro. Apague as marcas (`<<<<<<<`, `=======`, `>>>>>>>`), deixe a linha que deve ficar, salve, e:
```
git add arquivo-que-tinha-conflito
git commit -m "resolve conflito no título"
```

O VS Code mostra botões em cima do conflito ("Accept Current", "Accept Incoming", "Accept Both") que fazem isso com um clique.

**Para ter menos conflito:** dê `git pull` com frequência, e combinem no grupo quem está mexendo em qual arquivo.

---

## 7. Comandos de socorro

| Situação | Comando |
|---|---|
| Ver o histórico | `git log --oneline` |
| Ver exatamente o que mudei antes de commitar | `git diff` |
| Desfazer mudanças num arquivo que eu **não** commitei | `git restore arquivo` |
| Tirar um arquivo do `add` (sem perder a mudança) | `git restore --staged arquivo` |
| Guardar minhas mudanças de lado para dar `pull` | `git stash`, depois `git pull`, depois `git stash pop` |
| Esqueci em que branch estou | `git branch` (o atual tem `*`) |

**Nunca use** `git push --force` na `main`. Ele apaga o trabalho dos outros.

---

## Cola

```
git switch main && git pull           # começar o dia
git switch -c meu-nome/tarefa         # começar uma tarefa
git status                            # sempre antes do commit
git add arquivo
git commit -m "parte: o que mudou"
git push -u origin meu-nome/tarefa    # depois abre o pull request no GitHub
```
