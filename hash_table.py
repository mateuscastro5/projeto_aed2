class HashTable:
    def __init__(self, tamanho=101):
        self.tamanho = tamanho
        self.baldes = []
        self.colisoes = 0

        for i in range(tamanho):
            self.baldes.append([])

    def _hash(self, chave):
        soma = 0

        for i in range(len(chave)):
            soma = soma + ord(chave[i]) * (i + 1)

        return soma % self.tamanho

    def inserir(self, chave, ocorrencia):
        chave = chave.lower()
        balde = self.baldes[self._hash(chave)]

        for par in balde:
            if par[0] == chave:
                par[1].append(ocorrencia)
                return

        if len(balde) > 0:
            self.colisoes = self.colisoes + 1

        balde.append([chave, [ocorrencia]])

    def buscar(self, chave):
        chave = chave.lower()
        balde = self.baldes[self._hash(chave)]

        for par in balde:
            if par[0] == chave:
                return par[1]

        return []
