# Sistema de Ocorrências Acadêmicas — AED2

Aplicação de linha de comando que registra, consulta, ordena e atende ocorrências
acadêmicas (chamados de laboratório, pedidos de documento, suporte, etc.). O foco
é aplicar cada estrutura de dados de AED2 numa responsabilidade real do sistema.

## Como executar

Precisa de Python 3 instalado. No terminal, dentro da pasta do projeto:

```
python main.py
```

Não usa banco de dados nem bibliotecas externas — tudo roda em memória nas
estruturas implementadas à mão.

## O que cada opção do menu faz (e qual requisito cumpre)

O próprio menu mostra a estrutura e o requisito em cada linha. Resumo:

| Opção do menu                    | Estrutura usada               | Requisito | Para que serve                                  |
|----------------------------------|-------------------------------|-----------|-------------------------------------------------|
| 1 - Cadastrar ocorrência         | lista, fila, heap, árvore, pilha | 6.1    | Cria a ocorrência e alimenta todas as estruturas |
| 2 - Listar ocorrências           | lista geral (vetor)           | 6.2       | Mostra tudo que foi cadastrado                  |
| 3 - Atender por ordem de chegada | fila (FIFO)                   | 6.3       | Atende o mais antigo primeiro                   |
| 4 - Atender por maior prioridade | heap de máximo                | 6.4       | Atende o mais crítico primeiro                  |
| 5 - Buscar ocorrência por ID     | árvore de busca (BST)         | 6.5       | Localiza uma ocorrência pelo ID                 |
| 6 - Buscar por nome ou tipo      | hash table                    | 6.6       | Lista todas as ocorrências de um nome ou tipo   |
| 7 - Ordenar ocorrências          | ordenação manual + árvore     | 6.7       | Ordena por ID, prioridade ou nome               |
| 8 - Ver histórico de ações       | pilha                         | 6.8       | Lista as ações na ordem inversa (topo primeiro) |
| 9 - Desfazer última ação         | pilha                         | 6.9       | Remove o último registro do histórico           |
| 10 - Gerar massa de testes       | todas                         | extra     | Cadastra ocorrências de exemplo de uma vez      |

Na opção 7, ordenar por ID reaproveita o caminhamento em ordem da árvore de busca
(já sai ordenado); por prioridade e por nome usa um insertion sort feito à mão.

## Perguntas obrigatórias

**Onde foi usada a fila?**
No atendimento por ordem de chegada (opção 3). A fila (`fila.py`) é encadeada,
então quem é cadastrado primeiro é o primeiro a sair quando se atende por chegada.

**Onde foi usada a pilha?**
No histórico de ações e no desfazer (opções 8 e 9). Cada cadastro e cada
atendimento empilham um registro em `pilha.py`; o desfazer remove o do topo.

**Onde foi usada a árvore?**
Na busca de ocorrência por ID (opção 5), com o ID como chave da BST (`arvore.py`).
Ela ainda é reaproveitada na ordenação por ID (opção 7), porque o caminhamento
em ordem da árvore já devolve as ocorrências ordenadas pelo ID.

**Onde foi usada a heap?**
No atendimento pela maior prioridade (opção 4). A heap (`heap.py`) é de máximo,
então o topo é sempre a ocorrência mais crítica; em empate de prioridade, sai
primeiro quem chegou antes.

**Onde foi usada a hash table?**
Na busca por nome do solicitante ou por tipo (opção 6). São dois índices em
`hash_table.py`, e o valor de cada chave é a lista de ocorrências daquele nome
ou tipo.

**Qual algoritmo de ordenação foi implementado?**
Insertion sort, escrito à mão em `ordenacao.py`, usado para ordenar por
prioridade e por nome. A ordenação por ID é feita pelo caminhamento em ordem da
árvore, sem precisar de algoritmo extra.

**Qual estrutura foi mais adequada para busca rápida?**
A hash table, para buscar por nome ou tipo: o acesso é praticamente direto
(tempo médio constante), bem melhor do que varrer a lista inteira. Para a busca
exata por ID, a árvore de busca também é eficiente (proporcional à altura da
árvore), enquanto a busca linear na lista seria a mais lenta das três.

**Qual estrutura foi mais adequada para atendimento por prioridade?**
A heap, sem dúvida. Ela mantém a ocorrência de maior prioridade sempre no topo,
e inserir ou remover custa tempo logarítmico, sem precisar reordenar tudo a cada
atendimento.

**Qual foi a maior dificuldade?**
Manter todas as estruturas sincronizadas no cadastro — uma única ocorrência
precisa entrar em seis lugares ao mesmo tempo (lista, fila, heap, árvore e os
dois índices da hash), além de registrar a ação na pilha. Resolvi centralizando
isso na função `registrar_ocorrencia`, para não esquecer nenhuma estrutura.
A outra parte trabalhosa foi acertar a lógica de subir/descer da heap.

## Detalhe sobre o ID

O ID não é digitado: é gerado a partir do nome do solicitante (`gerar_id`),
no formato `PREFIXO-código` (ex.: `ANA-834`). É essa string que serve de chave
na árvore de busca.

## Vídeo de demonstração

https://github.com/user-attachments/assets/a140674d-21b1-4abf-92f1-b44398ae8cb8


