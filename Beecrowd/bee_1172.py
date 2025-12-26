lista = []

for x in range(10):
    numero = int(input())

    if numero <= 0:
        numero = 1

    lista.append(numero)

for x in range(0, 10):
    print(f"X[{x}] = {lista[x]}")