cont = 0

intervalo, fim = map(int, input().split(" "))

for x in range(1, fim + 1):
    if x % intervalo != 0:
        print(f"{x}", end=" ")
    else:
        print(f"{x}")