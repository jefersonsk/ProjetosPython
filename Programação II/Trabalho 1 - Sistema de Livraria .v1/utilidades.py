import unicodedata
from datetime import date


class Cor:
    BRANCO = "\033[37m"
    VERDE = "\033[32m"
    AZUL = "\033[34m"
    CIANO = "\033[36m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[31m"
    MAGENTA = "\033[35m"
    CINZA = "\033[90m"
    MAGENTA_CLARO = "\033[1;95m"
    VERDE_CLARO = "\033[1;92m"
    CIANO_CLARO = "\033[1;96m"
    LARANJA = "\033[1;38;5;208m"
    RESET = "\033[0m"


class Erro:
    MENSAGENS = {
        "E01": "Valor inválido.",
        "E02": "Opção inválida.",
        "E03": "Não existe nenhum dado cadastrado.",
        "E04": "Título não localizado.",
        "E05": "Categoria não localizada.",
        "E06": "Sem dados para serem exibidos.",
        "E07": "Quantidade em estoque não localizada.",
        "E08": "Ano inválido.",
        "E09": "Campo não pode ser em branco.",
        "E10": "Dados já foram carregados para o sistema.",
        "E11": "Dados do arquivo não carregados.\nCarregar dados antes de utilizar o aplicativo"
    }


# ======================================
# FERRAMENTAS DE LAYOUT E MENSAGENS
# ======================================


def criar_menu(lista: list, bloqueado: bool = False, tipo: str = "principal") -> None:
    """
    Cria menu conforme a lista informada, com opção de tipos
    "principal" e "submenu"

    Args:
        lista (list): Lista com as opções que devem ser geradas no menu
        bloqueado (bool): 
        tipo (str, optional): Tipo "principal" irá mostrar a opção para
            encerraro sistema. Tipo "submenu" irá mostrar a opção para
            voltar para o menu anterior. Valor default é "principal".
    """
    for i, item in enumerate(lista, start=1):
        if bloqueado and i != 9:
            print(f"{Cor.CINZA}{i} - {Cor.CINZA}{item}{Cor.RESET}")
        else:
            print(f"{Cor.AZUL}{i} - {Cor.VERDE}{item}{Cor.RESET}")

    if tipo.lower() == "principal":
        print(f"{Cor.AZUL}0 - {Cor.VERDE}ENCERRAR ATIVIDADES{Cor.RESET}")
    else:
        print(f"{Cor.AZUL}0 - {Cor.VERDE}VOLTAR AO MENU PRINCIPAL{Cor.RESET}")

    imprimir_linha()


def imprimir_cabecalho(
        texto: str, quantidade: int = 60, cor: str = Cor.BRANCO) -> None:
    """
    Cria cabeçalhos com cores.

    Args:
        texto (str): Texto que deve ser confiugurado no cabeçalho.
        quantidade (int, optional): Quantidade de caracteres do cabeçalho. Default é 60.
        cor (str, optional): Cor do texto. Default é branco "\033[1;97m".
    """
    imprimir_linha()
    print(f"{cor}{texto.center(quantidade)}{Cor.RESET}")
    imprimir_linha()


def imprimir_linha(caracter: str = "-", quantidade: int = 60) -> None:
    """
    Cria uma linha com o caracter e quantidade informados.

    Args:
        caracter (str, optional): Caracter que será impresso. Default é "-".
        quantidade (int, optional): Quantidade de caracteres que serão impressos. Default é 60.
    """
    print(quantidade * caracter)


def mostrar_erro(codigo: str, cor: str) -> None:
    """
    Mostra mensagem de erro conforme código informado. Códigos e mensagens estão armazendados no dicionário MENSAGEM_ERRO.

    Args:
        codigo (str): Código de erro, onde a mensagem será capturada no dicionário MENSAGEM_ERRO.
        cor (str): Cor da mensagem.
    """
    if cor == Cor.AMARELO:
        mensagem = "AVISO"
    else:
        mensagem = "ERRO"

    erro = f"{mensagem} - {Erro.MENSAGENS.get(codigo, 'Erro Desconhecido')}"

    imprimir_cabecalho(texto=erro, cor=cor)

    pausar()


def pausar() -> None:
    """
    Realiza uma pausa na execução e irá retornar após pressionar qualquer
    tecla.
    """
    input("\nPressione ENTER para continuar...\n")

# ======================================
# FUNÇÕES DE VALIDAÇÃO
# ======================================


def verificar_lista(lista: list) -> bool:
    """
    Verifica se a lista tem dados armazenados retornando True se a lista está vazia, caso contrário retorna False.

    Args:
        lista (list): Lista onde os dados são gravados.

    Returns:
        bool: Retorna Retorna True se a lista está vazia e False se tem algum dado gravado.
    """
    return not lista


def escolher_operador(texto: str) -> str:
    """
    Faz a escolha de qual operador "<=" ou ">=" será escolhido para as buscas.

    Args:
        texto (str): Texto da pergunta que será mostrada para usuário.

    Returns:
        str: Retorna "<=" ou ">=".
    """
    while True:
        print(f"{Cor.CIANO}{texto}{Cor.RESET}")
        imprimir_linha()

        criar_menu(
            ["ACIMA DO VALOR (MAIOR OU IGUAL)",
             "ABAIXO DO VALOR (MENOR OU IGUAL)"],
            bloqueado=False,
            tipo="submenu",
        )

        escolha = verificar_numero(
            "Escolha a opção desejada: ", int, cor=Cor.AMARELO)
        imprimir_linha()

        if escolha == 1:
            return ">="
        elif escolha == 2:
            return "<="
        elif escolha == 0:
            return None
        else:
            mostrar_erro("E02", Cor.VERMELHO)


def verificar_numero(
    texto: str, tipo_conversao: type, cor: str = Cor.BRANCO
) -> int | float:
    """
    Verifica se o que está sendo digitado é número inteiro(int) ou decimal(float), conforme tipo_conversao informada.

    Args:
        texto (str): Texto da pergunta que será mostrada para o usuário.
        tipo_conversao (type): Tipo do dado que será verificado, int ou float

    Returns:
        int | float: Retorna o valor após validação.
    """
    while True:
        try:
            valor_digitado = tipo_conversao(input(f"{cor}{texto}{Cor.RESET}"))

            if valor_digitado < 0:
                mostrar_erro("E01", Cor.VERMELHO)
            else:
                return valor_digitado
        except ValueError:
            mostrar_erro("E01", Cor.VERMELHO)


def validar_ano(texto: str, cor: str = Cor.BRANCO) -> int:
    """
    Valida o ano digitado.

    Returns:
        int: Retorna o ano digitado como o tipo inteiro.
    """
    ano_atual = date.today().year

    while True:
        ano = verificar_numero(f"{cor}{texto}{Cor.RESET}", int)

        if len(str(ano)) == 4 and str(ano).isdigit() and ano <= ano_atual or ano == 0:
            return ano
        else:
            mostrar_erro("E08", Cor.VERMELHO)


# ======================================
# FERRAMENTAS
# ======================================


def condicao_atendida(dado_livro, pesquisa, operador: str) -> bool:
    """
    Verifica se o dado do livro atende à condição do operador.

    Args:
        dado_livro (_type_): Dado que foi capturado na lista que deve ser comparado com o dado do usuário.
        pesquisa (_type_): Dado informado pelo usuário que está sendo utilizado como base para pesquisa.
        operador (str): Qual operador será usado para retornar os dados.

    Returns:
        bool: Retorna True se localizar o dado informado pelo usuário. Caso contrário, retorna False.
    """
    if operador == "==":
        return (
            remover_acentos(str(pesquisa)).upper()
            in remover_acentos(str(dado_livro)).upper()
        )
    elif operador == ">=":
        return dado_livro >= pesquisa
    elif operador == "<=":
        return dado_livro <= pesquisa
    return False


def fazer_buscas(
    lista: list,
    texto: str,
    nome_atributo: str,
    erro: str,
    operador: str = "==",
    tipo_dado: type = str,
) -> None:
    """
    Realiza a busca pelos dados conforme escolha definida pelo usuário. Se não encontrar o dado solicitado, retorna mensagem de aviso.

    Args:
        lista_livros (list): Lista onde estão os dados cadastrados.
        texto (str): Texto da pergunta que será mostrada para o usuário.
        nome_atributo (str): Qual atributo de classe será utilizado na busca dos dados.
        erro (str): Código de aviso, onde a mensagem será capturada no dicionário MENSAGEM_ERRO.
        operador (str, optional): Operador que deve ser utilizado para realizar a busca, ">=", "<=" ou "==". Default é "==".
        tipo_dado (type, optional): Tipo de dado que será informado para busca: "int", "float" ou "str". Default é "str".
    """
    encontrou = False

    if verificar_lista(lista):
        mostrar_erro("E03", Cor.AMARELO)
        return

    while True:
        if tipo_dado == str:
            pesquisa = input(f"{Cor.AMARELO}{texto}{Cor.RESET}")
        else:
            pesquisa = verificar_numero(texto, tipo_dado, cor=Cor.AMARELO)

        imprimir_cabecalho("RESULTADO DA PESQUISA", cor=Cor.MAGENTA_CLARO)

        for dados in lista:
            dado_livro = getattr(dados, nome_atributo)

            if condicao_atendida(dado_livro, pesquisa, operador):
                dados.mostrar_informacoes()
                encontrou = True

        if not encontrou:
            mostrar_erro(erro, Cor.AMARELO)
        else:
            pausar()
            return


def remover_acentos(texto: str) -> str:
    """
    Verifica o texto informado e remove acentuação e cedilha, retornando o texto normalizado.

    Args:
        texto (str): Texto que será normalizado.

    Returns:
        str: Texto normalizado sem acentos e cedilha.
    """
    # NFKD serve para quebrar o caracter acentuado em duas partes, a letra e o acento. Ex: "Á" é separado em "A" + "´".
    # O normalize serve para remover a conexão entre o caractere e o acento.
    texto_normalizado = unicodedata.normalize("NFKD", texto)
    # encode("ASCII"): realiza a conversão do texto decomposto para o padrão ASCII, onde contém em sua tabela as letras sem acentos.
    # Ele aceita a letra base porém não reconhece o símbolo do acento
    # "ignore": informa o que pode ser descartado. Se localizar algum caractere que não está na tabela ASCII, irá ignorar e não irá adicionar ao texto limpo.
    # decode("utf-8"): O comando encode transforma o texto em formato de bytes. Já o decode pega esses bytes já sem acentos e transforma em string.
    texto_limpo = texto_normalizado.encode("ASCII", "ignore").decode("utf-8")
    return texto_limpo


def verificar_vazio(texto: str, cor: str = Cor.BRANCO) -> str:
    """
    Verifica se o campo está com conteúdo vazio.

    Args:
        texto (str): Texto que deve ser exibido para o usuário.

    Returns:
        str: Se não há conteúdo retorna mensagem de aviso, caso contrário retorna o conteúdo digitado.
    """
    while True:
        texto_digitado = input(f"{cor}{texto}{Cor.RESET}")

        if texto_digitado == "":
            mostrar_erro("E09", Cor.VERMELHO)
        else:
            return texto_digitado
