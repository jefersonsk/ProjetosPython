def verifica_idade(item: int) -> int:
    return item[1]

dados_pessoas = []

with open("pessoas.csv", "r") as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(",")
        dados_pessoas.append([dados[0], dados[2]])
        
dados_pessoas.sort(key=verifica_idade)

print(dados_pessoas[0:3])
print(dados_pessoas[-3:])