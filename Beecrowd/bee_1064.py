contador = 0
media = 0

for x in range(6):
    numero = float(input())
    if numero > 0:
        contador += 1
        media = media + numero

media = media / contador

print(f"{contador} valores positivos")
print(f"{media:.1f}")