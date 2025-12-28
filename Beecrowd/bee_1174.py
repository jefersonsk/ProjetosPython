lista = []
numeros_validos = []

for x in range(100):
    lista.append(float(input()))

for x in range(len(lista)):
    if lista[x] <= 10:
        print(f"A[{x}] = {lista[x]:.1f}")