lista = [int(input()) for x in range(20)]

lista.reverse()

for posicao, numero in enumerate(lista):
    print(f"N[{posicao}] = {numero}")