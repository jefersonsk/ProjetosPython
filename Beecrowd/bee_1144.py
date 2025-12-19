contador = 1

quantidade = int(input())

for x in range(quantidade):
    
    contador_quadrado = contador ** 2
    contador_cubo = contador ** 3

    print(f"{contador} {contador_quadrado} {contador_cubo}")
    print(f"{contador} {contador_quadrado + 1} {contador_cubo + 1}")

    contador += 1
        