flag = True

while flag:
    soma = 0

    num_01, num_02 = map(int, input().split(" "))

    if num_01 <= 0 or num_02 <= 0:
        flag = False
    else:

        num_01, num_02 = sorted([num_01, num_02])

        for x in range(num_01, num_02 + 1):
            print(f"{x}", end=" ")
            soma += x

        print(f"Sum={soma}")