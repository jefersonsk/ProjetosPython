lista = []

numero = int(input())

for x in range(10):
    lista.append(numero)
    print(f"N[{x}] = {numero}")
    numero *= 2