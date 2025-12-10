reais = 0
centavos = 0

def verifica_quantidade(valor: int, divisor: int, cedula: str, tipo: str) -> str:
    global reais, centavos
    auxiliar = valor // divisor
    if valor == reais:
        reais = reais - (auxiliar * divisor)
    else:
        centavos = centavos - (auxiliar * divisor)

    print(f"{auxiliar} {cedula}(s) de {tipo}")

flag = True

while flag:
    try:
        dinheiro = float(input())
    except:
        print("ERRO: Digite um número válido.")
    else:
        flag = False

dinheiro_formatado = f"{dinheiro:.2f}"
reais, centavos = dinheiro_formatado.split(".")
reais = int(reais)
centavos = int(centavos)

print("NOTAS: ")
verifica_quantidade(reais, 100, "nota", "R$ 100.00")
verifica_quantidade(reais, 50, "nota", "R$ 50.00")
verifica_quantidade(reais, 20,  "nota", "R$ 20.00")
verifica_quantidade(reais, 10,  "nota", "R$ 10.00")
verifica_quantidade(reais, 5,  "nota", "R$ 5.00")
verifica_quantidade(reais, 2,  "nota", "R$ 2.00")
print("MOEDAS: ")
verifica_quantidade(reais, 1, "moeda", "R$ 1.00")
verifica_quantidade(centavos, 50, "moeda", "R$ 0.50")
verifica_quantidade(centavos, 25, "moeda", "R$ 0.25")
verifica_quantidade(centavos, 10, "moeda", "R$ 0.10")
verifica_quantidade(centavos, 5, "moeda", "R$ 0.05")
verifica_quantidade(centavos, 1, "moeda", "R$ 0.01")