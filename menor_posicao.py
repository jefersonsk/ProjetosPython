lista = []

quantidade = int(input())

for x in range(0, quantidade):
    lista.append(int(input()))

lista_aux = lista.copy()
lista_aux.sort()

menor = lista_aux[0]
posicao = lista.index(menor)

print(f"Menor valor: {menor}")
print(f"Posição: {posicao}")