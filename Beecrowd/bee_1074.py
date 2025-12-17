quantidade = int(input())

for x in range(quantidade):

    numero = int(input())

    if numero == 0:
        verifica = "NULL"
    else:
        verifica = "EVEN" if numero % 2 == 0 else "ODD"
        verifica = f"{verifica} NEGATIVE" if numero < 0 else f"{verifica} POSITIVE"

    print(verifica)