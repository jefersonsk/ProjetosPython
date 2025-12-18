flag = True

while flag:
    x, y = map(int, input().split(" "))

    if x == 0 or y == 0:
        flag = False
    else:
        if x > 0 and y > 0:
            quadrante = "primeiro"
        elif x > 0 and y < 0:
            quadrante = "quarto"
        elif x <0 and y < 0:
            quadrante = "terceiro"
        else:
            quadrante = "segundo"

        print(quadrante)