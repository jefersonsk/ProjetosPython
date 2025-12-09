inicio = int(input('Início: '))
fim = int(input('Fim: '))
soma = 0

while inicio <= fim:
    soma = soma + inicio
    inicio += 1

print(soma)