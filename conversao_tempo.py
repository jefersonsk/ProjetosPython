flag = True

while flag:
    try:
        valor = int(input())
        if valor > 0:
            flag = False
        else:
            raise TypeError("Erro 1")

    except ValueError:
        print("Você não pode digitar letras!")
    except TypeError:
        print("Digitar um número inteiro e positivo!")

horas = valor // 3600
minutos = (valor - (horas * 3600)) // 60
segundos = valor % 60

print(f"{horas}:{minutos}:{segundos}")