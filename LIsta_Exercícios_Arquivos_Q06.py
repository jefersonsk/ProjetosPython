titulo = "TÍTULO"
autor = "AUTOR"
ano_publicacao = "ANO DE PUBLICAÇÃO"
valida = "S"
registro = [titulo, autor, ano_publicacao]

# with open("livros.csv", "w") as arquivo:
linha = ','.join(registro)

print(linha)