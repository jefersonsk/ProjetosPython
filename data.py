MES_31 = "135781012"
MES_30 = "46911"
data_valida = False
valida_30_flag = False
valida_31_flag = False
valida_dia_mes_ano_flag = False

dia = int(input())
mes = int(input())
ano = int(input())

valida_dia_mes_ano_flag = 0 < dia <= 31 and 0 < mes <= 12 and ano > 0
valida_30_flag = MES_30.find(str(mes)) >= 0
valida_31_flag = MES_31.find(str(mes)) >= 0

if valida_31_flag and mes != 2 and valida_dia_mes_ano_flag:
    if 0 < dia <= 31:
        data_valida = True
        
elif valida_30_flag and mes != 2:
    if 0 < dia <= 30:
        data_valida = True
        
elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        if 0 < dia <= 29:
            data_valida = True
    else:
        if 0 < dia <= 28:
            data_valida = True

if data_valida:
    print("sim")
else:
    print("não")