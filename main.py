from ocorrencia import Ocorrencia
from fila import Fila
from pilha import Pilha
from heap import HeapPrioridade
from arvore import ArvoreBusca
from hash_table import HashTable


ocorrencias = []
fila = Fila()
historico = Pilha()
heap = HeapPrioridade()
arvore = ArvoreBusca()
indice_nome = HashTable()
indice_tipo = HashTable()


def gerar_id(nome):
    soma = 0

    for letra in nome:
        soma = soma + ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)


def ler_prioridade():
    while True:
        valor = input("Prioridade de 1 a 5: ")
        if valor in ["1", "2", "3", "4", "5"]:
            return int(valor)
        print("Valor inválido. Digite um número de 1 a 5.")


def cadastrar_ocorrencia():
    print("\nCADASTRAR OCORRÊNCIA")

    nome = input("Nome do requisitante: ")
    tipo = input("Tipo da ocorrência: ")
    descricao = input("Descrição: ")
    prioridade = ler_prioridade()

    id_ocorrencia = gerar_id(nome)
    ordem = len(ocorrencias) + 1

    nova = Ocorrencia(id_ocorrencia, nome, tipo, descricao, prioridade, ordem)
    ocorrencias.append(nova)
    fila.enfileirar(nova)
    heap.inserir(nova)
    arvore.inserir(nova)
    indice_nome.inserir(nome, nova)
    indice_tipo.inserir(tipo, nova)
    historico.empilhar("Cadastro da ocorrência " + nova.id)

    print("\nOcorrência cadastrada!")
    print("ID:", nova.id)
    print("Ordem de chegada:", nova.ordem)


def mostrar_ocorrencia(oc):
    print("ID:", oc.id, "| Nome:", oc.nome, "| Tipo:", oc.tipo,
          "| Prioridade:", oc.prioridade, "| Status:", oc.status)


def listar_ocorrencias():
    print("\nLISTAR OCORRÊNCIAS")

    if len(ocorrencias) == 0:
        print("Nenhuma ocorrência cadastrada ainda.")
        return

    for oc in ocorrencias:
        mostrar_ocorrencia(oc)


def atender_por_chegada():
    print("\nATENDER POR ORDEM DE CHEGADA")

    if fila.esta_vazia():
        print("Não há ocorrências aguardando na fila.")
        return

    oc = fila.desenfileirar()
    oc.status = "Atendido"
    historico.empilhar("Atendimento por chegada da ocorrência " + oc.id)

    print("Atendendo ocorrência mais antiga:")
    mostrar_ocorrencia(oc)


def atender_por_prioridade():
    print("\nATENDER POR MAIOR PRIORIDADE")

    if heap.esta_vazia():
        print("Não há ocorrências na fila de prioridade.")
        return

    oc = heap.remover_maior()
    oc.status = "Atendido"
    historico.empilhar("Atendimento por prioridade da ocorrência " + oc.id)

    print("Atendendo ocorrência mais crítica:")
    mostrar_ocorrencia(oc)


def buscar_por_id():
    print("\nBUSCAR OCORRÊNCIA POR ID")

    id_procurado = input("Digite o ID da ocorrência: ")
    oc = arvore.buscar(id_procurado)

    if oc is None:
        print("Nenhuma ocorrência encontrada com esse ID.")
        return

    print("Resultado:")
    mostrar_ocorrencia(oc)


def buscar_por_nome_ou_tipo():
    print("\nBUSCAR POR NOME OU TIPO")
    print("1 - Pelo nome do solicitante")
    print("2 - Pelo tipo da ocorrência")
    escolha = input("Escolha: ")

    if escolha == "1":
        chave = input("Nome do solicitante: ")
        encontradas = indice_nome.buscar(chave)
    elif escolha == "2":
        chave = input("Tipo da ocorrência: ")
        encontradas = indice_tipo.buscar(chave)
    else:
        print("Opção inválida.")
        return

    if len(encontradas) == 0:
        print("Nenhuma ocorrência encontrada.")
        return

    print("Ocorrências encontradas:")
    for oc in encontradas:
        mostrar_ocorrencia(oc)


def ver_historico():
    print("\nHISTÓRICO DE AÇÕES")

    if historico.esta_vazia():
        print("Nenhuma ação registrada ainda.")
        return

    for acao in historico.listar():
        print("-", acao)


def desfazer_ultima_acao():
    print("\nDESFAZER ÚLTIMA AÇÃO")

    if historico.esta_vazia():
        print("Não há ações para desfazer.")
        return

    acao = historico.desempilhar()
    print("Ação removida do histórico:", acao)


while True:
    print("\n===== SISTEMA DE OCORRÊNCIAS ACADÊMICAS =====")
    print("1 - Cadastrar ocorrência (lista, fila, heap, árvore, hash e pilha - req 6.1)")
    print("2 - Listar ocorrências (lista geral - req 6.2)")
    print("3 - Atender por ordem de chegada (fila - req 6.3)")
    print("4 - Atender por maior prioridade (heap - req 6.4)")
    print("5 - Buscar ocorrência por ID (árvore de busca - req 6.5)")
    print("6 - Buscar por nome ou tipo (hash table - req 6.6)")
    print("7 - Ver histórico de ações (pilha - req 6.8)")
    print("8 - Desfazer última ação (pilha - req 6.9)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "3":
        atender_por_chegada()
    elif opcao == "4":
        atender_por_prioridade()
    elif opcao == "5":
        buscar_por_id()
    elif opcao == "6":
        buscar_por_nome_ou_tipo()
    elif opcao == "7":
        ver_historico()
    elif opcao == "8":
        desfazer_ultima_acao()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
