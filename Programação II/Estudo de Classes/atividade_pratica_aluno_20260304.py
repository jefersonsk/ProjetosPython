class Aluno:
    def __init__(self, nome_completo, curso, matricula, email, notas):
        self.nome_completo = nome_completo
        self.curso = curso
        self.matricula = matricula
        self.email = email
        self.notas = notas

    def mostrar_informacao(self):
        
        print(f"NOME: {self.nome_completo:<50} MATRÍCULA: {self.matricula:>10}")
        # :.<30 alinha para esquerda em 50 caracteres e o >10 caracteres a partir da direita
        print(f"E-MAIL: {self.email}")
        for chave, dado in self.notas.items():
            print(f"NOTAS: {chave} - {dado}")
        linha()

def lista_dados(lista: list[Aluno]) -> None:
    """
    Recebe uma lista, verifica se possui dados cadastrados e, em caso positvo, exibe os dados na tela.

    Args:
        lista (list[Aluno]): Variável onde estão os cadastrados os dados.

    Returns:
        None
    """

    if not lista:
        print("ERRO: Nenhum dado cadastrado!")
        return
    
    for dado in lista:
        dado.mostrar_informacao()

def verifica_lista(lista: list[Aluno]) -> bool:
    """
    Recebe uma lista, verifica se tem dados e retorna True ou False.

    Args:
        lista(list[Aluno]): Variável onde estão os dados cadatrados.

    Returns:
        bool: Retona True se a lista contêr dados ou False se estiver vazia
    """

    return not lista

def linha(tamanho: int = 42) -> str:
    """ 
    Cria uma linha com o caracter "-".

    Args:
        tamanho(int): Define quantas vezes o caracter "-" será impresso na tela. Se nada for informado, o valor padrão é 42.

    Returns:
        str: A string contendo a linha gerada
    """

    return print("-" * tamanho)

def cabecalho(texto: str) -> None:
    """Cria um cabeçalho com o texto informado.

    Args:
        texto (str): Texto que deve ser configurado dentro da estrutura do cabeçalho.

    Returns:
        None
    """

    linha()
    print(texto.center(42))
    linha()

def menu(lista: list) -> None:
    """Cria menu de escolhas.

    Args:
        lista (list): Lista com as opções que serão geradas no menu.
    """

    contador = 1
    for item in lista:
        print(f"{contador} - {item}")
        contador += 1
    
    linha()

def continua() -> None:
    """
    Faz uma pausa no programa até que uma tecla seja pressionada.

    Returns:
        None
    """

    input("\nPressione qualquer tecla para continuar...\n")

def verifica_nota(mensagem: str) -> float:
    """
    Verifica se o valor digitado é um número com casas decimais.

    Args:
        mensagem (str): Mensagem para montagem da pergunta

    Returns:
        float: Após o tratamento de erro para verificar se é um número decimal ou se está entre o intervalo de 0 a 10, retorna o valor válido.
    """

    flag = True

    while flag:
        try:
            valor = float(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO: Nota inválida!")
        else:
            if valor < 0 or valor > 10:
                print("ERRO: Digite uma nota entre 0 e 10!")
            else:
                flag = False
                return valor

def verifica_opcao(mensagem: str, quantidade: int) -> int:
    """Verifica se o valor digitado é um número inteiro e um valor válido dentro das opções do menu.

    Args:
        mensagem (str): Mensagem para montafem da pergunta.
        quantidade (int): Quantidade de opções do menu

    Returns:
        int: Após verificação se o valor é numérico e aplicação de tratamento de erro, retorno um valor inteiro válido.
    """

    try:
        valor = int(input(mensagem))
    except (ValueError, TypeError):
        print("ERRO: Opção Inválida!")
        continua()
    else:
        if valor < 1 or valor > quantidade:
            print("ERRO: Opção não existe!")
            continua()
        else:
            return valor

lista_alunos = []

while True:
    escolha_menu = 0

    cabecalho("SISTEMA DE CADASTRO DE ALUNOS")
    menu(["CADASTRO", "ALTERAR NOTA", "RELATÓRIO", "ENCERRAR"])

    escolha_menu = verifica_opcao("Escolha a opção desejada: ", 4)

    if escolha_menu == 1:
        cabecalho("CADASTRO DE ALUNO")

        # operador warlus (:=) permite atribuir um valor em uma variável e na mesma linha usar esse valor para
        # validar uma condição.
        while (nome := input("NOME ALUNO (ou 'SAIR' para encerrar): ")).upper() != "SAIR":
            curso = input("CURSO: ")
            matricula = int(input("MATRICULA: "))
            email = str(matricula) + "@aluno.ifrs.edu.br"
            disciplina = input("DISCIPLINA: ")
            nota = verifica_nota("NOTA: ")
            notas = {disciplina: nota}

            dados_aluno = Aluno(nome, curso, matricula, email, notas)
            lista_alunos.append(dados_aluno)

            cabecalho("DADOS INCLUÍDOS COM SUCESSO")
            continua()

    elif escolha_menu == 2:
        cabecalho("ALTERAR NOTA")

        if verifica_lista(lista_alunos):
            print("ERRO: Nenhm dado cadastrado!")
            continua()
            continue

        matricula_aluno = int(input("Digite Matrícula do Aluno: "))

        for dados_aluno in lista_alunos:
            if matricula_aluno == dados_aluno.matricula:
                cabecalho("DADOS DO ALUNO")
                dados_aluno.mostrar_informacao()
                disciplina_aluno = list(dados_aluno.notas.keys())[0]
                nova_nota = verifica_nota("Digite a nova nota: ")
                dados_aluno.notas[disciplina_aluno] = nova_nota
                print(f"Nota do aluno {dados_aluno.nome_completo} foi alterada com sucesso!")
                continua()
            else:
                print("ERRO: Matrícula não localizada!")
                continua()

    elif escolha_menu == 3:
        if verifica_lista(lista_alunos):
            print("ERRO: Nenhm dado cadastrado!")
            continua()
            continue

        cabecalho("RELATÓRIO DE ALUNOS CADASTRADOS")
        lista_dados(lista_alunos)
        continua()

    elif escolha_menu == 4:
        cabecalho("SISTEMA ENCERRADO")
        break