flag = True
lista = []

while flag:
    numero = int(input())

    if numero < 0:
        flag = False
    else:
        lista.append(numero)

media = sum(lista) / len(lista)

print(f"{media:.2f}")