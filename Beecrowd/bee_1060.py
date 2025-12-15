contador = 0

for x in range(6):
    numero = float(input())
    if numero > 0:
        contador += 1

print(f"{contador} valores positivos")