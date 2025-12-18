quantidade = int(input())

for x in range(quantidade):
    soma = 0

    lista = list(map(int, input().split(" ")))

    lista.sort()

    for x in range(lista[0] + 1, lista[1]):
        if x % 2 != 0:
            soma += x
    
    print(soma)