contador = 1

quantidade = int(input())

for x in range(quantidade):
    for y in range(1, 5):
        if contador % 4 != 0:
            print(f"{contador}", end=" ")
        else:
            print("PUM")
        
        contador += 1