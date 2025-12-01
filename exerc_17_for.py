conta_par = 0
soma_par = 0
conta_impar = 0
media_impar = 0

inicio = int(input())
fim = int(input())

if fim > inicio:
    for x in range(inicio, fim + 1):
        if x % 2 == 0:
            soma_par = soma_par + x
            conta_par += 1
        else:
            media_impar = media_impar + x
            conta_impar += 1
    
    print()
    print(soma_par)
    print(conta_par)
    print()
    print(media_impar / conta_impar)
    print(conta_impar)
else:
    print('Intervalo inválido.')