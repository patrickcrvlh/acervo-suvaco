# Banco de dados — PostgreSQL

## Situação atual

O banco foi criado pelo Igor e roda **na máquina dele**. Isso tem uma consequência que vale entender: um banco local só aceita conexão do próprio computador. Mesmo com o usuário e a senha, ninguém do grupo consegue se conectar a ele de outra máquina.

Então o caminho para o grupo inteiro trabalhar com o banco não é compartilhar a senha — é **compartilhar a estrutura**. Cada um roda o seu próprio PostgreSQL e cria as mesmas tabelas a partir de um arquivo que fica aqui no repositório.

## O que precisa entrar nesta pasta

| Arquivo | O que é | Quem faz |
|---|---|---|
| `schema.sql` | Os comandos que criam as tabelas (sem dados). | Igor |
| `amostra.sql` | Algumas linhas de exemplo, para testar. Opcional. | Igor |
| `.env.example` | Modelo de configuração, sem senha. | já está aqui |

### Como o Igor exporta (no terminal da máquina dele)

Estrutura das tabelas, sem nenhum dado:
```
pg_dump -U postgres -d NOME_DO_BANCO --schema-only --no-owner -f schema.sql
```

Uma amostra dos dados, em formato de INSERT (mais fácil de ler e de revisar):
```
pg_dump -U postgres -d NOME_DO_BANCO --data-only --inserts --no-owner -f amostra.sql
```

Antes de subir a amostra, abra o arquivo e confira: se tiver nome de pessoa, comentário interno ou link do Drive, tire essas linhas ou use só uma amostra pequena. Se o repositório for público, qualquer pessoa na internet lê.

### Como os outros criam o banco igual na própria máquina

```
createdb -U postgres acervo_suvaco
psql -U postgres -d acervo_suvaco -f schema.sql
psql -U postgres -d acervo_suvaco -f amostra.sql
```

Depois copie o `.env.example` para `.env` e coloque a **sua** senha local.

## Mais pra frente

Quando o banco precisar ser um só para todos — para o site funcionar de verdade — ele vai precisar ficar num servidor. Essa decisão fica para quando o repositório oficial do projeto estiver pronto.
