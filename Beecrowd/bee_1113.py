flag = True

while flag:

    num_01, num_02 = map(int, input().split(" "))

    if num_01 == num_02:
        flag = False
    elif num_01 != num_02:
        if num_01 < num_02:
            tipo = "Crescente"
        else:
            tipo = "Decrescente"

        print(tipo)