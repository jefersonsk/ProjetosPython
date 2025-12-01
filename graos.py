cod_grao = 0
soma_quantidade_01 = 0
soma_quantidade_02 = 0
soma_quantidade_03 = 0
soma_quantidade_04 = 0
flag = True
flag_erro = True

while flag:
    
    while flag_erro:
        try:
            cod_grao = int(input("Grão: "))
            
            if cod_grao == 0:
                flag_erro = False
            elif cod_grao < 0 or cod_grao > 4:
                raise ValueError("Erro 1")
            else:
                flag_erro = False

            if cod_grao != 0:
                quantidade_grao = int(input("Quantidade: "))
                if quantidade_grao < 0:
                    raise ValueError("Erro 2")
                else:
                    flag_erro = False

        except:
            print('Digite um número inteiro válido.')
        
    if cod_grao == 1:
        soma_quantidade_01 = soma_quantidade_01 + quantidade_grao
    elif cod_grao == 2:
        soma_quantidade_02 = soma_quantidade_02 + quantidade_grao
    elif cod_grao == 3:
        soma_quantidade_03 = soma_quantidade_03 + quantidade_grao
    elif cod_grao == 4:
        soma_quantidade_04 = soma_quantidade_04 + quantidade_grao
    elif cod_grao == 0:
        flag = False
    
    flag_erro = True

total_armazenado = soma_quantidade_01 + soma_quantidade_02 + soma_quantidade_03 + soma_quantidade_04

print(f"1 {soma_quantidade_01} {((soma_quantidade_01 * 100) / total_armazenado):.2f}")
print(f"2 {soma_quantidade_02} {((soma_quantidade_02 * 100) / total_armazenado):.2f}")
print(f"3 {soma_quantidade_03} {((soma_quantidade_03 * 100) / total_armazenado):.2f}")
print(f"4 {soma_quantidade_04} {((soma_quantidade_04 * 100) / total_armazenado):.2f}")