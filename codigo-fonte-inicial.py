class Ocorrencia:
    def __init__(self, id_ocorrencia, nome, tipo, descricao, prioridade, ordem):
        self.id = id_ocorrencia
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.prioridade = prioridade
        self.ordem = ordem
        self.status = "Aberto"


ocorrencias = []


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


while True:
    print("\n===== SISTEMA DE OCORRÊNCIAS ACADÊMICAS =====")
    print("1 - Cadastrar ocorrência")
    print("2 - Listar ocorrências")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
