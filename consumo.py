# VARIÁVEIS
flag_erro = flag_distancia = flag_valor = True

# ENTRADA DE DADOS
while flag_erro:
    try:
        if flag_distancia == True:
            distancia = int(input("Distância: "))
            if distancia > 0:
                flag_erro = False
                flag_distancia = False
            else:
                raise ValueError("Erro 1")
            
        if flag_valor == True:
            valor = float(input("Valor: "))
            if valor >= 0:
                flag_erro = False
                flag_valor = False
            else:
                raise ValueError("Erro 2")
    
    except:
        print("Digite um número positivo.")

    if flag_distancia == True or flag_valor == True:
        flag_erro = True

# PROCESSAMENTO
consumo = distancia / valor

# SAÍDA DE DADOS
print(f"{consumo:.3f} km/l")