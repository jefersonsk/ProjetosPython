def imprime_tela(lista: list) -> print:
    for x in lista:
        print(x)

valores = list(map(int, input().split(" ")))

valores_ordenados = sorted(valores)

imprime_tela(valores_ordenados)
print()
imprime_tela(valores)