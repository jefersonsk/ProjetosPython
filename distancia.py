flag = True

while flag:
    try:
        distancia = int(input())

        if distancia <= 0:
            raise TypeError("Erro 1")
        else:
            flag= False
        
    except TypeError:
        print("Digite um valor positivo.")
    except ValueError:
        print("Você não pode digitar letras!")
    else:
       tempo = distancia * 2
       print(f"{tempo} minutos")