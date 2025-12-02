nome = "Nome"
idade = "Idade"
clube = "Clube"
registro = [nome, idade, clube]
repetir = "S"
nome_arquivo = ""

nome_arquivo = input("Qual nome do arquivo? ") + ".csv"

with open(nome_arquivo, 'w') as arquivo:
    linha = ','.join(registro)
    arquivo.write(linha + "\n")
    nome = idade = clube = ""
    while repetir != "N":
        nome = input("Nome: ")
        idade = input("Idade: ")
        clube = input("Clube: ")
        registro = [nome, idade, clube]
        linha = ','.join(registro)
        arquivo.write(linha + '\n')
        print(f"Registro arquivado: {registro}")
        repetir = input("Repetir S/N? ").upper()

print("Processamento finalizado. Saindo...")
print("Dados salvos no arquivo: dados.csv")
