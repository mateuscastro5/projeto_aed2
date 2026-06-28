def _vem_antes(a, b, criterio):
    if criterio == "prioridade":
        return a.prioridade > b.prioridade
    if criterio == "nome":
        return a.nome.lower() < b.nome.lower()
    return a.id < b.id


def ordenar(lista, criterio):
    copia = list(lista)

    for i in range(1, len(copia)):
        atual = copia[i]
        j = i - 1

        while j >= 0 and _vem_antes(atual, copia[j], criterio):
            copia[j + 1] = copia[j]
            j = j - 1

        copia[j + 1] = atual

    return copia
