lista = []

lista.append(int(input()))
lista.append(int(input()))

lista.sort()

for x in range(lista[0] + 1, lista[1]):
    if x % 5 == 2 or x % 5 == 3:
        print(x)