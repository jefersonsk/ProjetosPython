inicio = int(input('Início: '))
fim = int(input('Fim: '))
soma_par = 0
soma_impar = 0
cont_impar = 0

if inicio <= fim:
    while inicio<= fim:
        if inicio % 2 == 0:
            soma_par = soma_par + inicio
        else:
            soma_impar = soma_impar + inicio
            cont_impar += 1
        inicio += 1

    print(soma_par)
    print(soma_impar / cont_impar)
else:
    print('Inválido')