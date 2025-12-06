import os

nome = "ALUNO"
notas = "NOTAS"
registro = [nome, notas]

with open("boletim.csv", "a") as arquivo:
    if os.path.exists("boletim.csv") == False:
        linha = ','.join(registro)
        arquivo.write(linha + "\n")

    
