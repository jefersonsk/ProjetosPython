hora_inicial, hora_final = map(int, input().split(" "))

if hora_inicial < hora_final:
    total = hora_final - hora_inicial
elif hora_inicial > hora_final:
    total = (24 - hora_inicial) + hora_final
else:
    total = 24

print(f"O JOGO DUROU {total} HORA(S)")