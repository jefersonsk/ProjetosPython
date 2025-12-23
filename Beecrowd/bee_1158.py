quantidade = int(input())

for x in range(quantidade):
    contador = 0
    soma = 0

    inicio, consecutivos = map(int, input().split(" "))

    while contador < consecutivos:
        if inicio % 2 != 0:
            soma += inicio
            contador += 1

        inicio += 1

    print(soma)
