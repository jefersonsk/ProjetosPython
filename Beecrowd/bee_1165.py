quantidade = int(input())

for x in range(quantidade):
    contador = 0

    numero =  int(input())

    for y in range(1, numero + 1):
        if numero % y == 0:
            contador += 1

    print(f"{numero} eh primo" if contador == 2 else f"{numero} nao eh primo")