quantidade = int(input())

for x in range(quantidade):
    a, b = map(int, input().split(" "))

    if  b == 0:
        saida = "divisao impossivel"
    else:
        saida = a / b

    print(saida)