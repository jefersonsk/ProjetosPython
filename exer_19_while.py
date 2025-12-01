soma_par = 0
produto_impar = 1
cont = 100

fim = int(input())

if fim > cont:
    while cont <= fim:
        if cont % 2 == 0:
            soma_par = soma_par + cont
        else:
            produto_impar = produto_impar * cont
        cont += 1
    print(soma_par)
    print(produto_impar)
else:
    print('Valor inválido.')

