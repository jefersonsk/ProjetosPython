lista = []

numero = int(input())

for x in range(1000):
    lista.append(x % numero) # O operador faz o trabalho de zerar o contador automaticamente sempre que atingimos o valor de numero

for posicao, numero in enumerate(lista):
    print(f"N[{posicao}] = {numero}")