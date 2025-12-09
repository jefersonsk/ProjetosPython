anterior = 0
proximo = 1
atual = 0

quantidade = int(input())

# print(f'{anterior}-{proximo}', end='-')

for i in range(1, (quantidade + 1)):

    if i == 1:
        print(anterior, end='-')
    elif i == 2:
        print(f'{proximo}', end='-')
    else:
        atual = anterior + proximo
        print(atual, end='-')
        anterior = proximo
        proximo = atual