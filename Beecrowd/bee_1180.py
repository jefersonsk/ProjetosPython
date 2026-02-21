quantidade = int(input())

lista = list(map(int, input().split()))

menor = min(lista)
posicao = lista.index(menor)

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")