flag = True
contador = 0
soma = 0

while flag:
    nota = float(input())

    if not 0 <=  nota <= 10:
        print("nota invalida")
    else:
        soma += nota
        contador += 1

    if contador == 2:
        flag = False
    
print(f"media = {soma / contador:.2f}")