lista = []
flag = True
contador = 0

while contador < 10:
    while flag:
        try:
            numero = int(input())
            if type(numero) is int:
                lista.append(numero)
                flag = False
        except:
            print('Digite um número válido.')

    flag = True
    contador += 1

for x in range(0, len(lista)):
    if lista[x] <= 0:
        del lista[x]
        lista.insert(x, 1)

for y in range(0, len(lista)):
    print(f"N[{y}] = {lista[y]}")