times = []

with open('pessoas.csv', 'r') as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(',')
        times.append(dados[5])

times_normalizados = set(times)
print(times_normalizados)