while (numero := int(input())) != 0:
    contador = 0
    soma = 0

    while contador < 5:
        if numero % 2 == 0:
            soma += numero
            contador += 1

        numero += 1

    print(soma)