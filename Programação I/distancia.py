flag = True

while flag:
    try:
        distancia = int(input())

        if distancia <= 0:
            raise ValueError("Erro 1")
        else:
            flag= False
        
    except ValueError:
        print("ERRO: Dados digitados são inválidos!")
        
    else:
       tempo = distancia * 2
       print(f"{tempo} minutos")