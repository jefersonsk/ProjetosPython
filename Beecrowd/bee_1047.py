hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split(" "))

inicio_minutos = hora_inicial * 60 + minuto_inicial
fim_minutos = hora_final * 60 + minuto_final

diferenca = fim_minutos - inicio_minutos

# Se a diferença for negativa, significa que o dia virou, então soma-se um dia inteiro(1440), para dara a volta no relógio
if diferenca <= 0:
    diferenca += 1440

hora= diferenca // 60
minutos = diferenca % 60
    
print(f"O JOGO DUROU {hora} HORA(S) E {minutos} MINUTO(S)")