def pegar_quantidade(item: list) -> list:
    return item[1]

contagem_times = {}
contagem_clube = 0

with open('pessoas.csv', 'r') as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(',')
        dados_time = dados[5]
        if dados_time in contagem_times:
            contagem_clube = contagem_times.get(dados_time)
            contagem_clube += 1
            contagem_times[dados_time] = contagem_clube
        else:
            contagem_times[dados_time] = 1

    resultados_ordenados = sorted(contagem_times.items(), key=pegar_quantidade, reverse=True)
    
for dados in resultados_ordenados:
    print(*dados)