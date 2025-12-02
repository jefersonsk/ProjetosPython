cidade = input("Digite uma cidade: ").upper()
print(cidade)

with open('pessoas.csv', 'r') as arquivo:
    for linha in arquivo:
        dados = linha.split(',')
              
        if dados[3].upper() == cidade:
            print(f"{dados[0]} mora na cidade de {cidade}.")

arquivo.close()