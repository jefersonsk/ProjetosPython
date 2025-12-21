flag = True

while flag:
    numero = int(input())
    if numero ==0:
        flag = False
    else:
        for x in range(1, numero + 1):
            if x != numero:
                print(f"{x}", end=" ")
            else:
                print(f"{x}")
    numero = 0