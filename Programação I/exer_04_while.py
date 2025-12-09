cont = 1
soma = 0
numeros = 0

while cont <= 50:
    if cont % 2 == 0:
        soma = soma + cont
        numeros += 1
    cont += 1
print(soma)
print(numeros)