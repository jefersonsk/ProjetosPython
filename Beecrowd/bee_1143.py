contador = 1

quantidade = int(input())

for x in range(quantidade):
    print(f"{contador}", end=" ")
    print(f"{contador ** 2}", end=" ")
    print(f"{contador ** 3}")

    contador += 1