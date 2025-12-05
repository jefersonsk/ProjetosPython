titulo = "TÍTULO"
autor = "AUTOR"
ano_publicacao = "ANO DE PUBLICAÇÃO"
repetir = "S"
registro = [titulo, autor, ano_publicacao]

with open("livros.csv", "w") as arquivo:
    linha = ','.join(registro)
    arquivo.write(linha + "\n")
    while repetir != 'N':
        nome = input("Título: ")
        autor = input("Autor: ")
        ano_publicacao = input("Ano de Publicação: ")
        registro = [titulo, autor, ano_publicacao]
        linha = ','.join(registro)
        arquivo.write(linha + "\n")
        print(f"Registro gravado: {registro}")
        repetir = input("Repetir S/N?\n").upper()

arquivo.close()

print("Processamento finalizado. Saindo...")
print("Dados salvos no arquivo: livros.csv")