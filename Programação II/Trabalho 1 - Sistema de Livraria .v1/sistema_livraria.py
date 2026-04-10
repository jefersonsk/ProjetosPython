import unicodedata
from datetime import date
import os

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

MENSAGEM_ERRO = {
    "E01": "Valor inválido.",
    "E02": "Opção inválida.",
    "E03": "Não existe nenhum dado cadastrado.",
    "E04": "Título não localizado.",
    "E05": "Categoria não localizada.",
    "E06": "Sem dados para serem exibidos.",
    "E07": "Quantidade em estoque não localizada.",
    "E08": "Ano inválido.",
    "E09": "Campo não pode ser em branco.",
}


class Livro:
    def __init__(self, titulo, codigo, editora, area, ano, valor, quantidade_estoque):

        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.quantidade_estoque = quantidade_estoque

    def mostrar_informacoes(self):
        print(f"{VERDE_CLARO}{'>' * 6} Cod#{self.codigo:04}{RESET}")
        print(f"{AZUL}Título / Editora: {AMARELO}{self.titulo} / {self.editora}{RESET}")
        print(f"{AZUL}Categoria: {AMARELO}{self.area}{RESET}")
        print(f"{AZUL}Ano: {AMARELO}{self.ano}{RESET}")
        print(f"{AZUL}Valor: {AMARELO}R$ {self.valor:.2f}{RESET}")
        print(f"{AZUL}Estoque: {AMARELO}{self.quantidade_estoque}{RESET}")
        print(
            f"{AZUL}Valor total em estoque: "
            f"{AMARELO}R$ {self.valor * self.quantidade_estoque:.2f}{RESET}"
        )
        imprimir_linha("-")


# CRIAÇÃO DE LAYOUT


def criar_menu(lista: list, tipo: str = "principal") -> None:
    """
    Cria menu conforme a lista informada, com opção de tipos
    "principal" e "submenu"

    Args:
        lista (list): Lista com as opções que devem ser geradas no menu
        tipo (str, optional): Tipo "principal" irá mostrar a opção para
            encerraro sistema. Tipo "submenu" irá mostrar a opção para
            voltar para o menu anterior. Valor default é "principal".
    """
    for i, item in enumerate(lista, start=1):
        print(f"{AZUL}{i} - {VERDE}{item}{RESET}")

    if tipo.lower() == "principal":
        print(f"{AZUL}0 - {VERDE}ENCERRAR ATIVIDADES{RESET}")
    else:
        print(f"{AZUL}0 - {VERDE}VOLTAR AO MENU PRINCIPAL{RESET}")

    imprimir_linha()


def imprimir_cabecalho(
        texto: str, quantidade: int = 60, cor: str = BRANCO) -> None:
    """
    Cria cabeçalhos com cores.

    Args:
        texto (str): Texto que deve ser confiugurado no cabeçalho.
        quantidade (int, optional): Quantidade de caracteres do cabeçalho. Default é 60.
        cor (str, optional): Cor do texto. Default é branco "\033[1;97m".
    """
    imprimir_linha()
    print(f"{cor}{texto.center(quantidade)}{RESET}")
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
    if cor == AMARELO:
        mensagem = "AVISO"
    else:
        mensagem = "ERRO"

    erro = f"{mensagem} - {MENSAGEM_ERRO.get(codigo, 'Erro Desconhecido')}"

    imprimir_cabecalho(texto=erro, cor=cor)

    pausar()


# VALIDAÇÕES


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
        print(f"{CIANO}{texto}{RESET}")
        imprimir_linha()

        criar_menu(
            ["ACIMA DO VALOR (MAIOR OU IGUAL)",
             "ABAIXO DO VALOR (MENOR OU IGUAL)"],
            "submenu",
        )

        escolha = verificar_numero(
            "Escolha a opção desejada: ", int, cor=AMARELO)
        imprimir_linha()

        if escolha == 1:
            return ">="
        elif escolha == 2:
            return "<="
        elif escolha == 0:
            return None
        else:
            mostrar_erro("E02", VERMELHO)


def verificar_numero(
    texto: str, tipo_conversao: type, cor: str = BRANCO
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
            valor_digitado = tipo_conversao(input(f"{cor}{texto}{RESET}"))

            if valor_digitado < 0:
                mostrar_erro("E01", VERMELHO)
            else:
                return valor_digitado
        except ValueError:
            mostrar_erro("E01", VERMELHO)


def validar_ano(texto: str, cor: str = BRANCO) -> int:
    """
    Valida o ano digitado.

    Returns:
        int: Retorna o ano digitado como o tipo inteiro.
    """
    ano_atual = date.today().year

    while True:
        ano = verificar_numero(f"{cor}{texto}{RESET}", int)

        if len(str(ano)) == 4 and str(ano).isdigit() and ano <= ano_atual or ano == 0:
            return ano
        else:
            mostrar_erro("E08", VERMELHO)


# FERRAMENTAS


def pausar() -> None:
    """
    Realiza uma pausa na execução e irá retornar após pressionar qualquer
    tecla.
    """
    input("\nPressione ENTER para continuar...\n")


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
        mostrar_erro("E03", AMARELO)
        return

    if tipo_dado == str:
        pesquisa = input(f"{AMARELO}{texto}{RESET}")
    else:
        pesquisa = verificar_numero(texto, tipo_dado, cor=AMARELO)

    imprimir_cabecalho("RESULTADO DA PESQUISA", cor=MAGENTA_CLARO)

    for dados in lista:
        dado_livro = getattr(dados, nome_atributo)

        if condicao_atendida(dado_livro, pesquisa, operador):
            dados.mostrar_informacoes()
            encontrou = True

    if not encontrou:
        mostrar_erro(erro, AMARELO)
    else:
        pausar()


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


def verificar_vazio(texto: str, cor: str = BRANCO) -> str:
    """
    Verifica se o campo está com conteúdo vazio.

    Args:
        texto (str): Texto que deve ser exibido para o usuário.

    Returns:
        str: Se não há conteúdo retorna mensagem de aviso, caso contrário retorna o conteúdo digitado.
    """
    while True:
        texto_digitado = input(f"{cor}{texto}{RESET}")

        if texto_digitado == "":
            mostrar_erro("E09", VERMELHO)
        else:
            return texto_digitado


# FUNÇÕES DO SISTEMA


def cadastrar_livros(lista: list):
    """
    Efetua o cadastro dos livros no sistema.

    Args:
        lista (list): Lista que será usada para armazenar os dados.
    """
    imprimir_cabecalho("CADASTRAR UM NOVO LIVRO", cor=AZUL)

    if verificar_lista(lista):
        codigo = 1
    else:
        codigo = lista[-1].codigo + 1

    print(f"{MAGENTA}CÓDIGO{RESET}: Cod#{codigo:04}")
    titulo = verificar_vazio("TÍTULO: ", cor=MAGENTA)
    editora = input(f"{MAGENTA}EDITORA: {RESET}")
    area = input(f"{MAGENTA}ÁREA: {RESET}")
    ano = validar_ano("ANO: ", cor=MAGENTA)
    valor = verificar_numero("VALOR: R$ ", float, MAGENTA)
    quantidade_estoque = verificar_numero("QUANTIDADE ESTOQUE: ", int, MAGENTA)

    lista.append(
        Livro(
            codigo=codigo,
            titulo=titulo,
            editora=editora,
            area=area,
            ano=ano,
            valor=valor,
            quantidade_estoque=quantidade_estoque,
        )
    )

    imprimir_cabecalho("LIVRO CADASTRADO COM SUCESSO.", cor=VERDE)

    pausar()


def listar_dados(lista: list):
    """
    Exibe todos os dados de uma lista. Caso ela esteja em branco, uma mensagem de erro é exibida.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """

    imprimir_cabecalho("LISTAR LIVROS", cor=VERDE)

    if verificar_lista(lista):
        mostrar_erro("E03", AMARELO)
    else:
        for dados in lista:
            dados.mostrar_informacoes()

        pausar()


def buscar_livros_titulo(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro o título.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR LIVROS POR TíTULO", cor=VERDE)
    fazer_buscas(lista, "Digite o título do livro: ", "titulo", "E04")


def buscar_livros_categoria(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro a categoria.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR LIVROS POR CATEGORIA", cor=VERDE)
    fazer_buscas(lista, "Digite a categoria desejada: ", "area", "E05")


def buscar_livros_preco(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro o preço do livro, optando por resultados
    maiores (>=) ou menores (<=) do valor desejado.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR LIVROS POR PREÇO", cor=VERDE)

    operador = escolher_operador("Como deseja buscar o preço?")

    if operador is None:
        return

    fazer_buscas(
        lista, "Digite o preço da pesquisa: R$ ", "valor", "E06", operador, float
    )


def buscar_quantidade_estoque(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro a quantidade em estoque, optando por valores
    maiores (>=) ou menores (<=).

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR QUANTIDADE POR ESTOQUE", cor=VERDE)

    operador = escolher_operador("Como deseja buscar a quantidade do estoque?")

    if operador is None:
        return

    fazer_buscas(
        lista,
        "Digite a quantidade em estoque: ",
        "quantidade_estoque",
        "E07",
        operador,
        int,
    )


def valor_total_estoque(lista: list):
    """
    Calcula o valor total em estoque.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    valor_total = 0

    imprimir_cabecalho("VALOR TOTAL EM ESTOQUE", cor=VERDE)

    valor_total = sum(
        dados.valor * dados.quantidade_estoque for dados in lista)

    print(f"{VERDE}Valor total em estoque: {AMARELO}R$ {valor_total:.2f}{RESET}")
    pausar()


def encerrar_atividades(_):
    """
    Encerra o sistema.

    Args:
        _: Parâmetro ignorado intencionalmente (necessário para manter a
           assinatura do menu).
    """
    print(f"\n{VERDE}<<< SISTEMA ENCERRADO >>>{RESET}\n")
    exit()


def inicializar_arquivo(nome_arquivo: str):
    cabecalho = ["CóDIGO",
                 "TíTULO",
                 "EDITORA",
                 "ÁREA/GÊNERO",
                 "ANO",
                 "VALOR",
                 "ESTOQUE"]

    arquivo_existe = os.path.exists(nome_arquivo)

    if not arquivo_existe:
        with open(nome_arquivo, "a") as arquivo:
            linha = ",".join(cabecalho)
            arquivo.write(linha + "\n")


def carregar_dados(lista: list, nome_arquivo: str) -> list:
    with open(nome_arquivo, "r") as arquivo:
        arquivo.readline()
        for dados in arquivo:
            cache = dados.strip().split(",")
            dados_livro = Livro(
                codigo=int(cache[0]),
                titulo=cache[1],
                editora=cache[2],
                area=cache[3],
                ano=int(cache[4]),
                valor=float(cache[5]),
                quantidade_estoque=int(cache[6])
            )

            lista.append(dados_livro)

        return lista


def carregar_estoque(lista: list) -> list:
    lista_livros = carregar_dados(lista, "livraria.txt")

    imprimir_cabecalho("DADOS CARREGADOS", cor=VERDE)
    pausar()

    return lista_livros


def salvar_livro(lista: list, nome_arquivo: str) -> None:
    with open(nome_arquivo, "w") as arquivo:
        cabecalho = "CóDIGO,TÍTULO,EDITORA,ÁREA/GÊNERO,ANO,VALOR,ESTOQUE\n"
        arquivo.write(cabecalho)

        for livro in lista:
            dados = f"{livro.codigo},{livro.titulo},{livro.editora},{livro.area},{livro.ano},{livro.valor},{livro.quantidade_estoque}"
            arquivo.write(dados + "\n")


def atualizar_estoque(lista: list):
    salvar_livro(lista, "livraria.txt")

    imprimir_cabecalho("DADOS SALVOS NO ARQUIVO.", cor=VERDE)


def main():
    lista_livros = []
    escolhas_menu = {
        1: cadastrar_livros,
        2: listar_dados,
        3: buscar_livros_titulo,
        4: buscar_livros_categoria,
        5: buscar_livros_preco,
        6: buscar_quantidade_estoque,
        7: valor_total_estoque,
        8: carregar_estoque,
        9: atualizar_estoque,
        0: encerrar_atividades,
    }

    inicializar_arquivo("livraria.txt")
    # lista_livros.append(
    #     Livro(
    #         "Senhor dos Anéis: A Sociedade do Anel", 1,
    #         "LPM", "Fantasia", 1999, 110, 5)
    # )
    # lista_livros.append(
    #     Livro("Senhor dos Anéis: Duas Torres", 2,
    #           "LPM", "Fantasia", 1999, 110, 15)
    # )
    # lista_livros.append(
    #     Livro("Senhor dos Anéis: O Retorno do Rei",
    #           3, "LPM", "Fantasia", 1999, 110, 10)
    # )
    # lista_livros.append(Livro("Código Limpo", 4, "POW",
    #                     "Informática", 2010, 80, 10))
    # lista_livros.append(
    #     Livro("Eu sou a Lenda", 5, "Globo", "Aventura", 2011, 65, 15))

    while True:
        imprimir_cabecalho("SISTEMA DE LIVRARIA .v1", cor=LARANJA)

        criar_menu(
            [
                "CADASTRAR NOVO LIVRO",
                "LISTAR LIVROS",
                "BUSCAR LIVROS POR NOME",
                "BUSCAR LIVROS POR CATEGORIA",
                "BUSCAR LIVROS POR PREÇO",
                "BUSCA POR QUANTIDADE EM ESTOQUE",
                "VALOR TOTAL EM ESTOQUE",
                "CARREGAR ESTOQUE",
                "ATUALIZAR ARQUIVO DE ESTOQUE"
            ]
        )

        opcao = verificar_numero("Digite a opção desejada: ", int, AMARELO)

        opcao_escolhida = escolhas_menu.get(opcao)

        if opcao_escolhida:
            opcao_escolhida(lista_livros)
        else:
            mostrar_erro("E02", VERMELHO)


if __name__ == "__main__":
    main()
