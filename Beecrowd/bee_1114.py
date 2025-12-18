senha = 2002
flag = True

while flag:

    numero = int(input())

    if numero != senha:
        print("Senha Invalida")
    else:
        print("Acesso Permitido")
        flag = False