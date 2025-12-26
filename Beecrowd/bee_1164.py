quantidade = int(input())

for x in range(quantidade):
    soma =0

    numero = int(input())

    for y in range(1, numero):
        if numero % y == 0:
            soma += y

    print(f"{numero} eh perfeito" if soma == numero else f"{numero} nao eh perfeito")