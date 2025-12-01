soma_intervalo = 0
soma_fora_intervalo = 0

numeros = input().split()

for n in numeros:
    try:
        if 10 < int(n) < 30:
            soma_intervalo += 1
        else:
            soma_fora_intervalo += 1
    except:
        print(f"Digito {n} inválido!")

print(f'{soma_intervalo} estão no intervalo')
print(f'{soma_fora_intervalo} estão fora do intervalo')