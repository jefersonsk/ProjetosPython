def cria_titulo(texto: str, tamanho: int, caracter: str) -> str:
    print(texto)
    print(caracter * tamanho)

def continua():
    return input("Pressione qualquer tecla para continuar...\n")

def mensagem(texto: str) -> str:
    print(f"\n{texto}\n")
    continua()

flag = True
alunos = {}
matricula = 0

while flag:

    cria_titulo("SISTEMA DE CADASTRO DE ALUNOS", 29, "=")

    print("1 - CADASTRO DE ALUNO")
    print("2 - INFORMAÇÕES DE ALUNOS")
    print("3 - ATUALIZAR NOTA")
    print("4 - MÉDIA DE NOTAS")
    print("0 - SAIR")
    cria_titulo("", 29, "=")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cria_titulo("\nCADASTRO DE ALUNO", 29, "=")
        matricula += 1
        print(f"Matricula: {matricula}")
        nome = input("Nome do Aluno: ")
        nota = float(input("Nota: "))

        alunos[matricula] = [nome, nota]

    elif opcao == 2:
        cria_titulo("\nINFORMAÇÕES DE ALUNOS", 29, "=")
        if alunos == {}:
            mensagem("ERRO: SEM ALUNOS CADASTRADOS!")
        else:
            dados = alunos.items()

            for matricula, cadastro in dados:
                print(f"MATRICULA: {matricula} - NOME: {cadastro[0]} - NOTA: {cadastro[1]}")

    elif opcao == 3:
        cria_titulo("\nATUALIZAR NOTA", 29, "=")
        matricula = int(input("MATRICULA: "))
        if matricula in alunos:
            nota = float(input("Digite a nova nota: "))
            alunos[matricula][1] = nota
        else:
            mensagem("MATRICULA NÃO ENCONTRADA!")

    elif opcao == 4:
        cria_titulo("\nMÉDIA DE NOTAS", 29, "=")

        if alunos != {}:
            soma = 0
            contador = 0
            dados = alunos.values()
            for nome, nota in dados:
                soma = soma + nota
                contador += 1

            print(f"MÉDIA TOTAL: {soma / contador:.2f}")
            continua()
        else:
            mensagem("ERRO: SEM ALUNOS CADASTRADOS!")

    elif opcao == 0:
        print("SISTEMA FINALIZADO!")
        flag = False

    else:
        print("ERRO: OPÇÃO INVÁLIDA!")
        continua()