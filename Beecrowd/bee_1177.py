lista = []

numero = int(input())

for x in range(1000):
    lista.append(x % numero)

for posicao, numero in enumerate(lista):
    print(f"N[{posicao}] = {numero}")