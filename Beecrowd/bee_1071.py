lista = []
soma = 0

lista.append(int(input()))
lista.append(int(input()))

lista.sort()

for x in range(lista[0] + 1, lista[1]):
    if x % 2 != 0:
        soma = soma + x

print(soma)