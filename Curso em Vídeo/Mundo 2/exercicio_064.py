numero = 0
contador = 0
soma = 0

while numero != 999:
    numero = int(input())
    if numero != 999:
        soma += numero
        contador += 1

print(contador, soma)