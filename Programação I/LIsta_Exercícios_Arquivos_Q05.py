lista_nomes = []
dados_esportes = []

esporte = input("Digite um nome de esporte: ")

with open("pessoas.csv", "r") as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(",")
        if dados[7].upper().strip() == esporte.upper():
            print(dados[0])

arquivo.close()