lista_nomes = dados_esportes = []

esporte = input("Digite um nome de esporte: ")

with open("pessoas.csv", "r") as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(",")
        dados_esportes.append([dados[0], dados[7].strip()])
       
        if dados_esportes[1].upper()== esporte:
        lista_nomes.append[dados[0]]

print(dados_esportes[1])