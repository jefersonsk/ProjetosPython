flag = True
contador = 0
soma = 0

while flag:
    valida = True
    nota = float(input())

    if not 0 <= nota <= 10:
        print("nota invalida")
    else:
        soma += nota
        contador += 1

    if contador == 2:
        print(f"media = {soma / contador:.2f}")
        soma = 0
        contador = 0

        while valida:
            continua = int(input("novo calculo (1-sim 2-nao)\n"))

            if continua == 1:
                valida = False
            elif continua == 2:
                valida = False
                flag = False