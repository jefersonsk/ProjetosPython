soma = 0
lista = []

lista = list(map(int, input().split(" ")))

a = lista.pop(0)

for x in lista:
    if x > 0:
        n = x
        break

for x in range(0, n):
    soma += a + x

print(soma)