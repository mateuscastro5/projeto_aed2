class Ocorrencia:
    def __init__(self, id_ocorrencia, nome, tipo, descricao, prioridade, ordem):
        self.id = id_ocorrencia
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.prioridade = prioridade
        self.ordem = ordem
        self.status = "Aberto"
