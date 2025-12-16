conta_par = 0
conta_impar = 0
conta_positivo = 0
conta_negativo = 0

for x in range(5):
    numero = int(input())
    if numero > 0:
        conta_positivo += 1
    elif numero < 0:
        conta_negativo += 1

    if numero % 2 == 0:
        conta_par += 1
    else:
        conta_impar += 1

print(f"{conta_par} valor(es) par(es)")
print(f"{conta_impar} valor(es) impar(es)")
print(f"{conta_positivo} valor(es) positivo(s)")
print(f"{conta_negativo} valor(es) negativo(s)")