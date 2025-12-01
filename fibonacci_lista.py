# VARIÁVEIS
FIBONACCI = [0,1]
verifica_fibonacci = []
contador = 0
flag_quantidade = flag_numero = True

# LISTA COM VALORES DO FIBONACCI
for x in range(1, 60):
    FIBONACCI.append(FIBONACCI[x - 1] + FIBONACCI[x])

# ENTRADA DE DADOS
while flag_quantidade:
    try:
        quantidade = int(input())
        if quantidade < 0 or quantidade > 60:
            raise ValueError("Erro 1")
        else:
            flag_quantidade = False
    except:
        print("Digite um valor entre 1 e 60.")

while quantidade > contador:
    while flag_numero:
        try:
            numero = int(input())
            if numero < 0 or numero > 60:
                raise ValueError("Erro 2")
            else:
                verifica_fibonacci.append(numero)
                flag_numero = False

        except:
            print("Digite um número inteiro e positivo.")
    
    flag_numero = True
    contador += 1

# SAÍDA DE DADOS
for y in range(0, len(verifica_fibonacci)):
    posicao = verifica_fibonacci[y]
    print(f"Fib({posicao}) = {FIBONACCI[posicao]}")