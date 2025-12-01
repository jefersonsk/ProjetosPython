lista = []
flag = True

while flag:

    try:
        numero = int(input())
        flag = False
    except:
        print('Digite um número válido.')
    

lista.append(numero)

for x in range(1, 10):
    numero = numero * 2
    lista.append(numero)

for y in range(0, len(lista)):
    print(f"N[{y}] = ", lista[y])