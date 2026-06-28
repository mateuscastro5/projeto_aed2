class HeapPrioridade:
    def __init__(self):
        self.itens = []

    def inserir(self, ocorrencia):
        self.itens.append(ocorrencia)
        self._subir(len(self.itens) - 1)

    def remover_maior(self):
        if len(self.itens) == 0:
            return None

        maior = self.itens[0]
        ultimo = self.itens.pop()

        if len(self.itens) > 0:
            self.itens[0] = ultimo
            self._descer(0)

        return maior

    def esta_vazia(self):
        return len(self.itens) == 0

    def _vem_antes(self, i, j):
        if self.itens[i].prioridade != self.itens[j].prioridade:
            return self.itens[i].prioridade > self.itens[j].prioridade
        return self.itens[i].ordem < self.itens[j].ordem

    def _subir(self, i):
        while i > 0:
            pai = (i - 1) // 2
            if self._vem_antes(i, pai):
                self.itens[i], self.itens[pai] = self.itens[pai], self.itens[i]
                i = pai
            else:
                break

    def _descer(self, i):
        tamanho = len(self.itens)

        while True:
            esquerda = 2 * i + 1
            direita = 2 * i + 2
            maior = i

            if esquerda < tamanho and self._vem_antes(esquerda, maior):
                maior = esquerda
            if direita < tamanho and self._vem_antes(direita, maior):
                maior = direita

            if maior == i:
                break

            self.itens[i], self.itens[maior] = self.itens[maior], self.itens[i]
            i = maior
