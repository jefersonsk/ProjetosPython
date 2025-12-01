resultado_hora = 0

hora_inicial = int(input())
minuto_inicial = int(input())
hora_final = int(input())
minuto_final = int(input())

if hora_inicial < hora_final:
    resultado_hora = hora_final - hora_inicial
elif hora_inicial > hora_final:
    resultado_hora = 24 - (hora_inicial - hora_final)

if minuto_final >= minuto_inicial:
    resultado_minuto = minuto_final - minuto_inicial
elif minuto_final < minuto_inicial:
    resultado_minuto = 60 - (minuto_inicial - minuto_final)
    resultado_hora -= 1

if hora_inicial == hora_final:
    if minuto_inicial < minuto_final:
        resultado_hora = 0
    elif minuto_inicial > minuto_final:
        resultado_hora = 23
    else:
        resultado_hora = 24

print(f"{resultado_hora:02d}:{str(resultado_minuto).ljust(2, '0')}")