def calcula_tempo(tempo_inicial: int, tempo_final: int, tipo: int) -> int:
    if tempo_inicial <= tempo_final:
        return tempo_final - tempo_inicial
    else:
        return tipo - (tempo_inicial - tempo_final)

hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split(" "))

hora_total = calcula_tempo(hora_inicial, hora_final, 24)
minuto_total = calcula_tempo(minuto_inicial, minuto_final, 60)

if minuto_inicial > minuto_final:
    hora_total -= 1

if hora_inicial == hora_final:
    if minuto_inicial < minuto_final:
        hora_total = 0
    elif minuto_inicial > minuto_final:
        hora_total = 23
    else:
        hora_total = 24
    
print(f"O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)")