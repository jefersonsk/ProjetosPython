anterior = 0
proximo = 1
flag = True

while flag:
    try:
        quantidade = int(input('Digite a quantidade: '))

        if quantidade <=0:
            raise ValueError("Erro 1")
        else:
            flag = False
        
    except (ValueError, TypeError):
        print("\033[31mERRO: Dados digitados são inválidos!\033[m")

else:

    print(anterior, proximo, end=' ')

    for i in range(0, (quantidade -2)):
        atual = anterior + proximo
        print(atual, end=' ')
        anterior = proximo
        proximo = atual