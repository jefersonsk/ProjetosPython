lista = []
lista_verificada = []
flag = True
contador = 0

while contador < 4:
    while flag:
        try:
            numero = float(input())
            if type(numero) is str:
                raise ValueError("Erro 1")
            else:
                lista.append(numero)
                flag = False
        except:
            print("Digite apenas números válidos.")
    
    contador += 1
    flag = True

for y in range(0, len(lista)):
    if lista[y] <= 10:
        print(f"A[{y}] = {lista[y]}")