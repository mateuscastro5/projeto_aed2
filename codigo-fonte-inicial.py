class Ocorrencia:
    def __init__(self, id_ocorrencia, nome, tipo, descricao, prioridade, ordem):
        self.id = id_ocorrencia
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.prioridade = prioridade
        self.ordem = ordem
        self.status = "Aberto"


class NoFila:
    def __init__(self, ocorrencia):
        self.ocorrencia = ocorrencia
        self.proximo = None


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def enfileirar(self, ocorrencia):
        no = NoFila(ocorrencia)
        if self.fim is None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no
            self.fim = no

    def desenfileirar(self):
        if self.inicio is None:
            return None

        no = self.inicio
        self.inicio = no.proximo
        if self.inicio is None:
            self.fim = None

        return no.ocorrencia

    def esta_vazia(self):
        return self.inicio is None


ocorrencias = []
fila = Fila()


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

    print("Atendendo ocorrência mais antiga:")
    mostrar_ocorrencia(oc)


while True:
    print("\n===== SISTEMA DE OCORRÊNCIAS ACADÊMICAS =====")
    print("1 - Cadastrar ocorrência")
    print("2 - Listar ocorrências")
    print("3 - Atender próxima ocorrência (ordem de chegada)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "3":
        atender_por_chegada()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
