lista_par = []
lista_impar = []

lista = [int(input()) for x in range(15)]

for x in lista:
    if x % 2 == 0:
        lista_par.append(x)
    else:
        lista_impar.append(x)

    if len(lista_par) == 5:
        for posicao, numero in enumerate(lista_par):
            print(f"par[{posicao}] = {numero}")
        lista_par = []

    if len(lista_impar) == 5:
        for posicao, numero in enumerate(lista_impar):
            print(f"impar[{posicao}] = {numero}")
        lista_impar = []

for posicao, numero in enumerate(lista_impar):
    print(f"impar[{posicao}] = {numero}")

for posicao, numero in enumerate(lista_par):
    print(f"par[{posicao}] = {numero}")