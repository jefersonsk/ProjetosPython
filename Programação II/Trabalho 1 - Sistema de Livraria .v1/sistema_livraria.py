import unicodedata
from datetime import date

VERDE = "\033[32m"
LARANJA = "\033[33m"
AZUL = "\033[34m"
CIANO = "\033[36m"
AMARELO = "\033[93m"
VERMELHO = "\033[31m"
MAGENTA = "\033[1;35m"
CINZA = "\033[1;90m"
MAGENTA_CLARO = "\033[1;95m"
VERDE_CLARO = "\033[1;92m"
RESET = "\033[0m"

MENSAGEM_ERRO = {"E01": "Valor inválido.",
                 "E02": "Opção inválida.",
                 "E03": "Não existe nenhum dado cadastrado.",
                 "E04": "Livro não encontrado.",
                 "E05": "Categoria não encontrada.",
                 "E06": "Valor não localizado.",
                 "E07": "Quantidade em estoque não localizada.",
                 "E08": "Ano inválido."}

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
        print(f"{">" * 6} Cod#{self.codigo:04}")
        print(f"Título / Editora: {self.titulo} / {self.editora}")
        print(f"Categoria: {self.area}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Estoque: {self.quantidade_estoque}")
        print(f"Valor total em estoque: R$ {self.valor * self.quantidade_estoque:.2f}")
        imprimir_linha("-")

# CRIAÇÃO DE LAYOUT

def criar_menu(lista: list, tipo: str = "principal") -> None:
    """
    Cria menu conforme a lista informada, com opção de tipos "principal" e "submenu" 

    Args:
        lista (list): Lista com as opções que devem ser geradas no menu
        tipo (str, optional): Tipo "principal" irá mostrar a opção para encerrar o sistema.
                              Tipo "submenu" irá mostrar a opção para voltar para o menu anterior. Valor default é "principal".
    """
    for i, item in enumerate(lista, start=1):
        print(f"{VERDE}{i} - {item}{RESET}")

    if tipo.lower() == "principal":
        print(f"{VERDE}0 - ENCERRAR ATIVIDADES{RESET}")
    else:
        print(f"{VERDE}0 - VOLTAR AO MENU PRINCIPAL{RESET}")

    imprimir_linha()

def imprimir_cabecalho(texto: str, caracter: str = "-", quantidade: int = 60, cor: str ="\033[1;97m") -> None:
    """
    Cria cabeçalhos com cores.

    Args:
        texto (str): Texto que deve ser confiugurado no cabeçalho.
        quantidade (int, optional): Quantidade de caracteres do cabeçalho. Default é 60.
        cor (str, optional): Cor do texto. Default é branco "\033[1;97m".
    """
    imprimir_linha()
    print(f"{cor}{texto.center(quantidade)}{RESET}")
    imprimir_linha(caracter, quantidade)

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
    print(f"\n{cor}===== ERRO - {MENSAGEM_ERRO.get(codigo, "Erro Desconhecido")} ====={RESET}")
    pausar()

# VALIDAÇÕES

def verificar_lista(lista: list) -> bool:
    """
    Verifica se a lista tem dados armazenados.

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
        print(texto)
        imprimir_linha()

        criar_menu(["ACIMA DO VALOR (MAIOR OU IGUAL)", "ABAIXO DO VALOR (MENOR OU IGUAL)"], "submenu")

        escolha = verifica_numero("Escolha a opção desejada: ", int)
        imprimir_linha()
        
        if escolha == 1:
            return ">="
        elif escolha == 2:
            return "<="
        elif escolha == 0:
            main()
        else:
            mostrar_erro("E06", VERMELHO)

def verificar_numero(texto: str, tipo_conversao: type) -> int | float:
    """
    Verifica se o que está sendo digitado é número inteiro ou decimal(float), conforme tipo_conversao informada.

    Args:
        texto (str): Texto da pergunta que será mostrada para o usuário.
        tipo_conversao (type): Tipo do dado que será verificado, int ou float

    Returns:
        int | float: Retorna o valor após validação.
    """
    while True:
        try:
            return tipo_conversao(input(texto))
        except (ValueError):
            mostrar_erro("E01", VERMELHO)

def validar_ano() -> int:
    """
    Valida o ano digitado.

    Returns:
        int: Retorna o ano digitado como o tipo inteiro.
    """
    ano_atual = date.today().year

    while True:
        ano = verificar_numero("ANO: ", int)

        if len(str(ano)) == 4 and str(ano).isdigit() and ano <= ano_atual:
            return ano
        else:
            mostrar_erro("E08", VERMELHO)

# FERRAMENTAS

def pausar() -> None:
    """
    Realiza uma pausa na execução e irá retornar após pressionar qualquer tecla.
    """
    input("\nPressione qualquer tecla para continuar...\n")

def fazer_buscas(lista: list, texto: str, tipo: str, erro: str, operador: str = "==", tipo_dado: type = str) -> None:
    """
    Realiza a busca pelos dados conforme escolha definida. Se não encontrar o dado solicitado, retorna mensagem de erro.

    Args:
        lista_livros (list): Lista onde estão os dados cadastrados.
        texto (str): Texto da pergunta que será mostrada para o usuário. 
        tipo (str): Qual tipo de dado que será utilizado na busca.
        erro (str): Código de erro, onde a mensagem será capturada no dicionário MENSAGEM_ERRO.
        operador (str, optional): Operador que deve ser utilizado para realizar a busca, ">=", "<=" ou "==". Default é "==".
        tipo_dado (type, optional): Tipo de dado que será informado para busca: "int", "float" ou "str". Default é "str".
    """
    encontrou = False

    if verificar_lista(lista):
        mostrar_erro("E03", AMARELO)
        return
    
    if tipo_dado == str:
        pesquisa = input(texto)
    else:
        pesquisa = verificar_numero(texto, tipo_dado)
    
    for dados in lista:
        if operador == "==":
            if remover_acentos(str(pesquisa)).upper() in remover_acentos(str(getattr(dados, tipo))).upper():
                dados.mostrar_informacoes()
                encontrou = True
        elif operador == ">=":
            if getattr(dados, tipo) >= pesquisa:
                dados.mostrar_informacoes()
                encontrou = True
        elif operador == "<=":
            if getattr(dados, tipo) <= pesquisa:
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

# FUNÇÕES DO SISTEMA

def cadastrar_livros(lista: list):
    """
    Efetua o cadastro dos livros no sistema.

    Args:
        lista (list): Lista que será usada para armazenar os dados.
    """
    imprimir_cabecalho("CADASTRAR UM NOVO LIVRO", cor = AZUL)

    if verificar_lista(lista):
        codigo = 1
    else:
        codigo = lista[-1].codigo + 1

    print(f"CÓDIGO: Cod#{codigo:04}")
    titulo = input("TÍTULO: ")
    editora = input("EDITORA: ")
    area = input("ÁREA: ")
    ano = validar_ano()
    valor = verificar_numero("VALOR: R$ ", float)
    quantidade_estoque = verificar_numero("QUANTIDADE ESTOQUE: ", int)

    lista.append(Livro(titulo=titulo, codigo=codigo, editora=editora, area=area, ano=ano, 
                         valor=valor, quantidade_estoque=quantidade_estoque))
    
    imprimir_cabecalho("LIVRO CADASTRADO COM SUCESSO.", cor = VERDE)

    pausar()

def listar_dados(lista: list):
    """
    Exibe todos os dados de uma lista. Caso ela esteja em branco, uma mensagem de erro é exibida.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
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
    imprimir_cabecalho("BUSCAR LIVROS POR TíTULO", cor = VERDE)
    fazer_buscas(lista, "Digite o título do livro: ", "titulo", "E04")
    
def buscar_livros_categoria(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro a categoria.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR LIVROS POR CATEGORIA", cor = VERDE)
    fazer_buscas(lista, "Digite a categoria desejada: ", "area", "E05")

def buscar_livros_preco(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro o preço do livro, optando por resultados
    maiores (>=) ou menores (<=) do valor desejado.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR LIVROS POR PREÇO", cor = VERDE)

    operador = escolher_operador("Como deseja buscar o preço?")

    fazer_buscas(lista, "Digite o preço da pesquisa: R$ ", "valor", "E04", operador, float)

def buscar_quantidade_estoque(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro a quantidade em estoque, optando por valores
    maiores (>=) ou menores (<=).

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR QUANTIDADE POR ESTOQUE", cor = VERDE)

    operador = escolher_operador("Como deseja buscar a quantidade do estoque?  ")

    fazer_buscas(lista, "Digite a quantidade em estoque: ", "quantidade_estoque",
                 "E07", operador, int)

def valor_total_estoque(lista: list):
    """
    Calcula o valor total em estoque.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    valor_total = 0

    imprimir_cabecalho("VALOR TOTAL EM ESTOQUE", cor = VERDE)

    for dados in lista:
        total_item = dados.valor * dados.quantidade_estoque
        valor_total = valor_total + total_item

    print(f"Valor total em estoque: R$ {valor_total:.2f}")
    pausar()

def encerrar_atividades(_):
    """
    Encerra o sistema.

    Args:
        _: Parâmetro ignorado intencionalmente (necessário para manter a assinatura do menu).
    """
    print(f"\n{VERDE}<<< SISTEMA ENCERRADO >>>{RESET}\n")
    exit()

def main():
    lista_livros = []
    escolhas_menu = {1: cadastrar_livros,
                     2: listar_dados,
                     3: buscar_livros_titulo,
                     4: buscar_livros_categoria,
                     5: buscar_livros_preco,
                     6: buscar_quantidade_estoque,
                     7: valor_total_estoque,
                     0: encerrar_atividades}
    
    lista_livros.append(Livro("Senhor dos Anéis: A Sociedade do Anel", 1, "LPM", "Fantasia", 1999, 110, 5))
    lista_livros.append(Livro("Senhor dos Anéis: Duas Torres", 2, "LPM", "Fantasia", 1999, 110, 15))
    lista_livros.append(Livro("Senhor dos Anéis: O Retorno do Rei", 3, "LPM", "Fantasia", 1999, 110, 10))
    lista_livros.append(Livro("Código Limpo", 4, "POW", "Informática", 2010, 80, 10))
    lista_livros.append(Livro("Eu sou a Lenda", 5, "Globo", "Aventura", 2011, 65, 15))

    while True:
        imprimir_cabecalho("SISTEMA DE LIVRARIA .v1", cor = CIANO)

        criar_menu(["CADASTRAR NOVO LIVRO", 
                    "LISTAR LIVROS", 
                    "BUSCAR LIVROS POR NOME", 
                    "BUSCAR LIVROS POR CATEGORIA", 
                    "BUSCAR LIVROS POR PREÇO",
                    "BUSCA POR QUANTIDADE EM ESTOQUE",
                    "VALOR TOTAL EM ESTOQUE"])

        opcao = verificar_numero("Digite a opção desejada: ", int)

        opcao_escolhida = escolhas_menu.get(opcao)

        if opcao_escolhida:
            opcao_escolhida(lista_livros)
        else:
            mostrar_erro("E02", VERMELHO)

if __name__ == "__main__":
    main()