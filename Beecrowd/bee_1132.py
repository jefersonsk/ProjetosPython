soma = 0
lista = []

lista.append(int(input()))
lista.append(int(input()))

lista.sort()

for x in range(lista[0], lista[1] +1):
    if x % 13 != 0:
        soma += x

print(soma)