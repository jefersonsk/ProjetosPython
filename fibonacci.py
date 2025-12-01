anterior = 0
proximo = 1

quantidade = int(input())

print(anterior, proximo, end=' ')

for i in range(0, (quantidade -2)):

    atual = anterior + proximo
    print(atual, end=' ')
    anterior = proximo
    proximo = atual