contador = 0

numero = int(input())

while contador < 6:
    if numero % 2 != 0:
        print(numero)
        contador += 1
    numero += 1