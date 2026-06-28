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
