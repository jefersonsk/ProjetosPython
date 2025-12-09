
entrada = input()

while entrada.upper() != 'FIM':
    pedido = entrada.split(" ")
    entrada = input()
    
cod_cliente = pedido[0]
tipo = pedido[1]
regiao = pedido[2]
peso = float(pedido[3])

if tipo.upper() == "PADRAO":
    if regiao.upper() == "SUL":
        tarifa = peso * 5
    elif regiao.upper() == "SUDESTE":
        tarifa = peso * 6
    elif regiao.upper() == "CENTROOESTE":
        tarifa = peso * 7
    elif regiao.upper() == "NORTE":
        tarifa = peso * 8.5
    elif regiao.upper() == "NORDESTE":
        tarifa = peso * 8
        
if peso < 0:
    envio = "PESO_INVALIDO"
if peso > 100:
    envio = "PESO_ACIMA_DO_LIMITE"
    
if tipo.upper() == "EXPRESSO" and peso > 30 and (regiao.upper() == "NORTE" or regiao.upper() = "NORDESTE"):
    envio = False
    
print(f"CLIENTE {codigo} SERVICO {tipo.upper()}")