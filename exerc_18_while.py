fim = int(input())
cont = 1
soma_par = 0

while cont <= fim:
    if cont % 2 == 0:
        soma_par = soma_par + cont
    cont += 1

print(soma_par)