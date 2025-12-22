numeros = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", 
    "Doze", "Treze", "Catorze", "Quinze", "Desseseis", "Dezesete", "Dezoito", "Dezenove", "Vinte")
flag = True

while flag:

    escolha = int(input("Digite um número entre 0 e 20: "))

    if 0 < escolha > 20:
        print("ERRO: Digite um número entre 0 e 20!")
    else:
        flag = False

print(f"Você digitou o número {numeros[escolha]}")