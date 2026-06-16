import unicodedata


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
        "E01": "CPF já cadastrado.",
        "E02": "Tipo não autorizado.",
        "E03": "ID não localizado.",
        "E04": "CPF inválido ou formato incorreto.",
        "E05": "CPF inválido.",
        "E06": "Código não localizado.",
        "E07": "Órgão Emissor já cadastrado.",
        "E08": "Órgão Emissor não cadastrado.",
        "E09": "Código inválido.",
        "E100": "Caracter não suportado.",
        "E101": "Opção Inválida."
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
        if bloqueado and i != 5:
            print(f"{Cor.CINZA}{i} - {Cor.CINZA}{item}{Cor.RESET}")
        else:
            print(f"{Cor.AZUL}{i} - {Cor.VERDE}{item}{Cor.RESET}")

    if tipo.lower() == "principal":
        print(f"{Cor.AZUL}0 - {Cor.VERDE}ENCERRAR ATIVIDADES{Cor.RESET}")
    else:
        print(f"{Cor.AZUL}0 - {Cor.VERDE}VOLTAR AO MENU PRINCIPAL{Cor.RESET}")

    imprimir_linha()


def imprimir_cabecalho(
        texto: str, quantidade: int = 80, cor: str = Cor.BRANCO) -> None:
    """
    Cria cabeçalhos com cores.

    Args:
        texto (str): Texto que deve ser confiugurado no cabeçalho.
        quantidade (int, optional): Quantidade de caracteres do cabeçalho. Default é 80.
        cor (str, optional): Cor do texto. Default é branco "\033[1;97m".
    """
    imprimir_linha()
    print(f"{cor}{texto.center(quantidade)}{Cor.RESET}")
    imprimir_linha()


def imprimir_linha(caracter: str = "-", quantidade: int = 80) -> None:
    """
    Cria uma linha com o caracter e quantidade informados.

    Args:
        caracter (str, optional): Caracter que será impresso. Default é "-".
        quantidade (int, optional): Quantidade de caracteres que serão impressos. Default é 80.
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
        mensagem = "⚠️  AVISO"
    else:
        mensagem = "❌  ERRO"

    erro = f"{mensagem} - {Erro.MENSAGENS.get(codigo, 'Erro Desconhecido')}"

    imprimir_cabecalho(texto=erro, cor=cor)

    pausar()


def pausar() -> None:
    """
    Realiza uma pausa na execução e irá retornar após pressionar qualquer
    tecla.
    """
    input("\nPressione ENTER para continuar...\n")


def imprimir_dados_na_tela(dados_funcionario: tuple, dados_orgao: str):
    id_orgao = dados_funcionario[6]

    print(f"{Cor.CIANO}NOME: {Cor.AMARELO}{dados_funcionario[1]}")
    print(
        f"{Cor.CIANO}CPF: {Cor.AMARELO}{dados_funcionario[2]:<20}"
        f"{Cor.CIANO}RG: {Cor.AMARELO}{dados_funcionario[3]:<20}"
        f"{Cor.CIANO}ORGÃO EMISSOR: {Cor.AMARELO}{dados_orgao}"
    )
    print(
        f"{Cor.CIANO}SALÁRIO: R$ {Cor.AMARELO}{dados_funcionario[5]:<13}"
        f"{Cor.CIANO}CATEGORIA: {Cor.AMARELO}{dados_funcionario[4]}"
        f"{Cor.RESET}"
    )

    imprimir_linha()

# ======================================
# FUNÇÕES DE VALIDAÇÃO
# ======================================


def verificar_numero(
    texto: str,
    tipo_conversao: type,
    cor: str = Cor.BRANCO,
    permitir_vazio: bool = False,
    permitir_zero: bool = False,
) -> int | float:
    """
    Verifica se o que está sendo digitado é número inteiro(int) ou 
    decimal(float), conforme tipo_conversao informada.

    Args:
        texto (str): Texto da pergunta que será mostrada para o usuário.
        tipo_conversao (type): Tipo do dado que será verificado, int ou 
        float

    Returns:
        int | float: Retorna o valor após validação.
    """
    while True:
        try:
            valor_digitado = input(f"{cor}{texto}{Cor.RESET}")

            if valor_digitado == "" and permitir_vazio:
                return None
            else:
                valor_verificado = tipo_conversao(valor_digitado)

            if ((permitir_zero and valor_verificado >= 0)
                    or (not permitir_zero and valor_verificado > 0)):
                return valor_verificado
            else:
                mostrar_erro("E100", Cor.VERMELHO)

        except ValueError:
            mostrar_erro("E100", Cor.VERMELHO)


def continuar() -> bool:

    while True:
        opcao = input("Deseja Continuar [S/N]? ")

        if opcao.upper() == "S":
            return True
        elif opcao.upper() == "N":
            return False
        else:
            mostrar_erro("E02", Cor.VERMELHO)


def enter_para_sair(texto: str, cor: str) -> bool:
    escolha = input(f"{cor}{texto} [Enter para SAIR]: {Cor.RESET}")
    if not escolha:
        return False
    else:
        return escolha


# ======================================
# FERRAMENTAS
# ======================================

def normalizar_texto(texto: str) -> str:
    """
    Verifica o texto informado e remove acentuação e cedilha, retornando o texto normalizado.

    Args:
        texto (str): Texto que será normalizado.

    Returns:
        str: Texto normalizado sem acentos e cedilha.
    """
    # NFKD serve para quebrar o caracter acentuado em duas partes, a
    # letra e o acento. Ex: "Á" é separado em "A" + "´".
    # O normalize serve para remover a conexão entre o caractere e o
    # acento.
    texto_acentos_desconectados = unicodedata.normalize("NFKD", texto)
    # encode("ASCII"): realiza a conversão do texto decomposto para o
    # padrão ASCII, onde contém em sua tabela as letras sem acentos.
    # Ele aceita a letra base porém não reconhece o símbolo do acento
    # "ignore": informa o que pode ser descartado. Se localizar algum
    # caractere que não está na tabela ASCII, irá ignorar e não irá
    # adicionar ao texto limpo.
    # decode("utf-8"): O comando encode transforma o texto em formato de
    # bytes. Já o decode pega esses bytes já sem acentos e transforma
    # em string.
    texto_limpo = texto_acentos_desconectados.encode(
        "ASCII", "ignore").decode("utf-8")
    texto_normalizado = texto_limpo.strip().lower()
    return texto_normalizado


def verificar_vazio(texto: str, cor: str = Cor.BRANCO) -> str:
    """
    Verifica se o campo está com conteúdo vazio.

    Args:
        texto (str): Texto que deve ser exibido para o usuário.

    Returns:
        str: Se não há conteúdo retorna mensagem de aviso, caso 
        contrário retorna o conteúdo digitado.
    """
    while True:
        texto_digitado = input(f"{cor}{texto}{Cor.RESET}")

        if texto_digitado == "":
            mostrar_erro("E09", Cor.VERMELHO)
        else:
            return texto_digitado


def validar_cpf(mensagem: str, cor: str) -> str | bool:
    """
    Args:
        mensagem (str): Mensagem que será mostrada para o usuário.
        cor (str): Cor escolhida para o texto.

    Retorno:
        str | bool: Retorna str quando o CPF é valido ou False(bool) se
        o Enter é pressionado para sair.
    """
    while True:
        cpf_digitado = enter_para_sair(mensagem, cor)

        if not cpf_digitado:
            return False

        # Retira pontos e hífens do CPF
        cpf_normalizado = cpf_digitado.replace(".", "").replace("-", "")

        """ 
            Verifica se o CPF tem 11 dígitos, se todos os dígitos são
            números e se não são todos iguais.
        """
        if (
            len(cpf_normalizado) != 11
            or not cpf_normalizado.isdigit()
            or len(set(cpf_normalizado)) == 1
        ):
            mostrar_erro("E04", Cor.AMARELO)
            continue

        # Calcula o primeiro dígito verificador
        calculo = sum(
            int(cpf_normalizado[posicao]) *
            (10 - posicao) for posicao in range(9)
        )
        primeiro_digito = (calculo * 10) % 11

        """
            Aplicação de Operador Ternário que permite a escrita de uma
            estrutura de if... else em uma única linha
        """
        primeiro_digito = 0 if primeiro_digito == 10 else primeiro_digito

        # Adiciona o primeiro dígito verificador as 9 primeiros dígitos
        verificacao_cpf = cpf_normalizado[:9] + str(primeiro_digito)

        # Calcula o segundo dígito verificador
        calculo = sum(
            int(verificacao_cpf[posicao]) *
            (11 - posicao) for posicao in range(10)
        )
        segundo_digito = (calculo * 10) % 11
        segundo_digito = 0 if segundo_digito == 10 else segundo_digito

        # Adiciona o segundo dígito verificador aos 10 dígitos
        verificacao_cpf += str(segundo_digito)

        # Compara o CPF digitado e o resultado do cálculo
        if cpf_normalizado == verificacao_cpf:
            return verificacao_cpf
        else:
            mostrar_erro("E05", Cor.AMARELO)


def escolher_categoria() -> str:
    opcoes_categoria = {
        "1": "GARÇOM",
        "2": "BARMAN",
        "3": "COZINHEIRO",
        "4": "N/D"
    }

    while True:
        print(f"{Cor.VERDE}CATEGORIAS DISPONÍVEIS{Cor.RESET}")
        print("[1] GARÇOM   [2] BARMAN   [3] COZINHEIRO   [4] N/D")

        escolha_categoria = verificar_vazio(
            "Selecione uma categoria: ", cor=Cor.CIANO
        )

        if escolha_categoria in opcoes_categoria:
            print(f"CATEGORIA: {opcoes_categoria.get(escolha_categoria)}")
            return opcoes_categoria.get(escolha_categoria)
        else:
            mostrar_erro("E06", cor=Cor.AMARELO)


def escolher_orgao_emissor(lista_de_orgaos) -> int:
    lista_ids_orgaos = []

    print(f"{Cor.AMARELO}ESCOLHA ORGÃO EMISSOR:{Cor.RESET}")

    for orgao in lista_de_orgaos:
        print(f"[{orgao[0]}]: {orgao[1]}", end=5 * " ")
        lista_ids_orgaos.append(orgao[0])

    while True:
        escolha_orgao = verificar_numero(
            "\nORGÃO EMISSOR: ",
            tipo_conversao=int,
            cor=Cor.CIANO
        )

        if escolha_orgao in lista_ids_orgaos:
            return escolha_orgao
        else:
            mostrar_erro("E09", cor=Cor.AMARELO)
