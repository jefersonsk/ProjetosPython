numeros = []

for x in range(100):
    numeros.append(int(input()))

maior = max(numeros)
posicao = numeros.index(maior) + 1

print(f"{maior}\n{posicao}")