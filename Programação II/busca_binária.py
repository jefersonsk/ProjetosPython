def pesquisa_binaria(minha_lista, item):
    baixo = 0
    alto = len(minha_lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = minha_lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    return None


minha_lista = ["AD", "BC", "HJ", "7", "KWY"]

print(pesquisa_binaria(minha_lista, "HJ"))
print(pesquisa_binaria(minha_lista, -1))
