def calcular_media(notas):
    total = sum(notas)
    return total / len(notas)


def processar_alunos(lista_de_alunos):
    for aluno in lista_de_alunos:
        media = calcular_media(aluno["notas"])

        if media > 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"O aluno {aluno['nome']} teve média {media} e está {situacao}")


alunos = []

# Adicionando um novo aluno via input
novo_nome = input("Digite o nome do aluno: ")
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))

novo_aluno = {"nome": novo_nome, "notas": [n1, n2]}
alunos.append(novo_aluno)

processar_alunos(alunos)
