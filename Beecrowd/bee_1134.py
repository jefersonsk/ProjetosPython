flag = True
conta_alcool = 0
conta_gasolina = 0
conta_diesel = 0

while flag:
    tipo = int(input())

    if tipo == 1:
        conta_alcool += 1
    elif tipo == 2:
        conta_gasolina += 1
    elif tipo == 3:
        conta_diesel += 1
    elif tipo == 4:
        flag = False

print("MUITO OBRIGADO")
print(f"Alcool: {conta_alcool}")
print(f"Gasolina: {conta_gasolina}")
print(f"Diesel: {conta_diesel}")