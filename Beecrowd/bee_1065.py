contador = 0

for x in range(5):
    numero = int(input())
    if numero % 2 == 0:
        contador += 1

print(f"{contador} valores pares")