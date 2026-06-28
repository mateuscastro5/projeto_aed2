class NoPilha:
    def __init__(self, acao):
        self.acao = acao
        self.proximo = None


class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, acao):
        no = NoPilha(acao)
        no.proximo = self.topo
        self.topo = no

    def desempilhar(self):
        if self.topo is None:
            return None

        no = self.topo
        self.topo = no.proximo
        return no.acao

    def ver_topo(self):
        if self.topo is None:
            return None
        return self.topo.acao

    def esta_vazia(self):
        return self.topo is None

    def listar(self):
        acoes = []
        atual = self.topo

        while atual is not None:
            acoes.append(atual.acao)
            atual = atual.proximo

        return acoes
