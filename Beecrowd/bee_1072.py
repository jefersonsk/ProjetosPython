conta_in = 0
conta_out = 0

numero = int(input())

for x in range(numero):
    verifica = int(input())
    if verifica >= 10 and verifica <= 20:
        conta_in += 1
    else:
        conta_out += 1

print(f"{conta_in} in")
print(f"{conta_out} out")