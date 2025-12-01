soma_par = 0

fim = int(input())

for x in range(1, fim + 1):
    if x % 2 == 0:
        soma_par = soma_par + x

print(soma_par)