soma = 0
divisor = 1

for x in range(1, 40, 2):
    if soma == 0:
        soma += 1
    else:
        soma += x / divisor
    print(f"{x}/{divisor}")
    divisor *= 2

print(f"{soma:.2f}")