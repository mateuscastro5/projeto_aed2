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
| 6 - Ver histórico de ações       | pilha                         | 6.8       | Lista as ações na ordem inversa (topo primeiro) |
| 7 - Desfazer última ação         | pilha                         | 6.9       | Remove o último registro do histórico           |

> Itens ainda em desenvolvimento: busca por nome/tipo (hash table, 6.6),
> ordenação manual (6.7) e geração de massa de testes.

## Onde cada estrutura aparece (Seção 12 do enunciado)

- **Fila** (`fila.py`): atendimento por ordem de chegada (opção 3).
- **Pilha** (`pilha.py`): histórico de ações e desfazer (opções 6 e 7).
- **Árvore** (`arvore.py`): busca de ocorrência por ID (opção 5).
- **Heap** (`heap.py`): atendimento pela maior prioridade (opção 4).
- **Hash table** (`hash_table.py`): busca por nome/tipo — em desenvolvimento.
- **Ordenação manual** (`ordenacao.py`): ordenar ocorrências — em desenvolvimento.

As demais perguntas obrigatórias serão respondidas ao final do projeto.

## Detalhe sobre o ID

O ID não é digitado: é gerado a partir do nome do solicitante (`gerar_id`),
no formato `PREFIXO-código` (ex.: `ANA-834`). É essa string que serve de chave
na árvore de busca.

## Vídeo de demonstração

https://github.com/user-attachments/assets/a140674d-21b1-4abf-92f1-b44398ae8cb8


