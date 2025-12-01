from funcoes import verifica_primo

flag = True

while flag:

    try:
        numero = int(input("Digite valor: "))
        if numero <= 0:
            raise TypeError("Erro 1")
        else:
            flag = False
    except TypeError:
        print("Digite um número positivo!")

print(verifica_primo(numero))