import os

def verifica_vazio(mensagem: str) -> str:
    flag = True

    while flag:
        verificar = input(mensagem)
        if verificar.strip() == "":
            print("ERRO: Digitar o nome do aluno.")
        else:
            flag = False

    return verificar

def valida_numero(mensagem: str, tipo: float | int, mensagem_erro: str) -> float:
    flag = True

    while flag:
        try:
            verificar = float(input(mensagem))
            if verificar < 0 or verificar > 10:
                raise TypeError("ERRO 1")
            
            flag = False

        except TypeError: 
            print("ERRO: Digite uma nota entre 0 e 10.")
        except:
            print(mensagem_erro)

    return str(verificar)

nome = "ALUNO"
título = "NOTAS"
registro = [nome, título]
repetir = "S"
media = 0

arquivo_existe = os.path.exists("boletim.csv")

with open("boletim.csv", "a") as arquivo:
    if arquivo_existe == False:
        linha = ','.join(registro)
        arquivo.write(linha + "\n")

    while repetir != "N":
        notas = []
        nome = verifica_vazio("Nome: ")
        for x in range(0, 3):
            notas.append(valida_numero(f"{x +1}ª Nota: ", float, "ERRO: Digite uma nota válida."))

        notas.insert(0, nome)
        linha = ','.join(notas)
        print(linha)
        arquivo.write(linha + "\n")
        repetir = input("Repetir S/N? ").upper()

arquivo.close()

with open("boletim.csv", "r") as arquivo:
    arquivo.readline()
    for linha in arquivo:
        dados = linha.split(',')
        nota_01 = float(dados[1])
        nota_02 = float(dados[2])
        nota_03 = float(dados[3])
        
        media = (nota_01 + nota_02 + nota_03) / 3
        if media >= 7:
            situacao = "APROVADO"
        elif media >= 5:
            situacao = "EM EXAME"
        else:
            situacao = "REPROVADO"

        print(f"ALUNO: {dados[0]} - NOTAS: {nota_01:.2f} | {nota_02:.2f} | {nota_03:.2f} - NÉDIA: {media:.2f} - SITUAÇÃO: {situacao}")

arquivo.close()