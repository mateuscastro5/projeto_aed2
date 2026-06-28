class NoArvore:
    def __init__(self, ocorrencia):
        self.ocorrencia = ocorrencia
        self.esquerda = None
        self.direita = None


class ArvoreBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, ocorrencia):
        if self.raiz is None:
            self.raiz = NoArvore(ocorrencia)
        else:
            self._inserir(self.raiz, ocorrencia)

    def _inserir(self, no, ocorrencia):
        if ocorrencia.id < no.ocorrencia.id:
            if no.esquerda is None:
                no.esquerda = NoArvore(ocorrencia)
            else:
                self._inserir(no.esquerda, ocorrencia)
        else:
            if no.direita is None:
                no.direita = NoArvore(ocorrencia)
            else:
                self._inserir(no.direita, ocorrencia)

    def buscar(self, id_procurado):
        no = self.raiz

        while no is not None:
            if id_procurado == no.ocorrencia.id:
                return no.ocorrencia
            if id_procurado < no.ocorrencia.id:
                no = no.esquerda
            else:
                no = no.direita

        return None

    def em_ordem(self):
        resultado = []
        self._em_ordem(self.raiz, resultado)
        return resultado

    def _em_ordem(self, no, resultado):
        if no is None:
            return

        self._em_ordem(no.esquerda, resultado)
        resultado.append(no.ocorrencia)
        self._em_ordem(no.direita, resultado)
