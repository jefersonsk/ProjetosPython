msg_01, dia_inicio = input().split(" ")
dia_inicio = int(dia_inicio)
horario_inicio = list(map(int, input().split(":")))
msg_01, dia_fim = input().split(" ")
dia_fim = int(dia_fim)
horario_fim = list(map(int, input().split(":")))

qtd_dias = (dia_fim - dia_inicio)
horario_inicio_seg = (horario_inicio[0] * 3600) + (horario_inicio[1] * 60) + horario_inicio[2]
horario_fim_seg = (horario_fim[0] * 3600) + (horario_fim[1] * 60) + horario_fim[2]

diferenca = horario_fim_seg - horario_inicio_seg

if diferenca < 0:
    diferenca += 86400
    qtd_dias -= 1

hora = diferenca // 3600
minuto = (diferenca - (hora * 3600)) // 60
segundos = diferenca % 60

print(f"{qtd_dias} dia(s)")
print(f"{hora} hora(s)")
print(f"{minuto} minuto(s)")
print(f"{segundos} segundo(s)")