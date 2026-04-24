import os
from livro import Livro, Filial, Livraria
from utilidades import (
    Cor,
    imprimir_cabecalho,
    imprimir_linha,
    criar_menu,
    verificar_lista,
    verificar_numero,
    verificar_vazio,
    pausar,
    mostrar_erro,
    fazer_buscas,
    escolher_operador
)


# ======================================
# MANIPULAÇÃO DE ARQUIVOS
# ======================================


def inicializar_arquivo(nome_arquivo: str) -> None:
    """
    Verifica se o arquivo existe ou se o seu tamanho é igual a 0. Caso verdadeiro, 
    cria o arquivo e adiciona a linha de cabeçalho.

    Args:
        nome_arquivo (str): Nome ou caminho do arquivo que será verificado.
    """

    cabecalho = [
        "CóDIGO",
        "TíTULO",
        "EDITORA",
        "ÁREA/GÊNERO",
        "ANO"
    ]

    arquivo_existe = os.path.exists(nome_arquivo)

    if not arquivo_existe or os.path.getsize(nome_arquivo) == 0:
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            linha = ",".join(cabecalho)
            arquivo.write(linha + "\n")


# ======================================
# FUNÇÕES PRINCIPAIS
# ======================================


# def filiais(lista_livros, lista_filiais: list):
#     escolha_menu = {1: cadastrar_filial,
#                     2: listar_filiais,
#                     3: adicionar_livros_filial}

#     while True:
#         imprimir_cabecalho("FILIAIS", cor=Cor.AZUL)

#         criar_menu(
#             [
#                 "CADASTRO DE FILIAIS",
#                 "LISTAR FILIAIS",
#                 "ADICIONAR LIVRO A FILIAIS"
#             ],
#             bloqueado=False,
#             tipo="submenu"
#         )

#         opcao = verificar_numero("Digite a opção desejada: ", int, Cor.AMARELO)

#         if opcao == 0:
#             return None

#         opcao_escolhida = escolha_menu.get(opcao)

#         opcao_escolhida(lista_livros, lista_filiais)


# def listar_filiais(lista_livros: list, lista_filiais: list):
#     imprimir_cabecalho("LISTA DE FILIAIS", cor=Cor.VERDE)

#     if verificar_lista(lista_filiais):
#         mostrar_erro("E03", Cor.AMARELO)
#     else:
#         for dados in lista_filiais:
#             dados.mostrar_informacoes_filial()

#         pausar()


# def adicionar_livros_filial(lista_livros: list, lista_filiais: list):
#     imprimir_cabecalho("ADICIONAR LIVRO A FILIAL", cor=Cor.VERDE)

#     if verificar_lista(lista_livros) or verificar_lista(lista_filiais):
#         mostrar_erro("E04", Cor.AMARELO)
#     else:
#         while True:
#             imprimir_cabecalho("LISTA DE FILIAIS", cor=Cor.VERDE)

#             for filial in lista_filiais:
#                 filial.mostrar_informacoes_resumidas()

#             imprimir_linha()

#             codigo_filial_escolhida = verificar_numero(
#                 "Digite o código da filial: ",
#                 int,
#             )

#             for filial in lista_filiais:
#                 if codigo_filial_escolhida == filial.codigo:
#                     titulo_livro = fazer_buscas(
#                         lista_livros,
#                         "Digite o título do livro: ",
#                         "titulo",
#                         "E04",
#                         retorno="s"
#                     )

#                     if titulo_livro:
#                         codigo_livro_escolhido = verificar_numero(
#                             "Digite o código do livro: ", int, Cor.AMARELO
#                         )

#                         for livro in lista_livros:
#                             if codigo_livro_escolhido == livro.codigo:
#                                 valor = verificar_numero(
#                                     "Valor: R$ ", float
#                                 )
#                                 quantidade_estoque = verificar_numero(
#                                     "Estoque: ", int
#                                 )

#                                 filial.adicionar_ao_estoque(
#                                     livro, valor, quantidade_estoque
#                                 )

#                             # else:
#                             #     imprimir_cabecalho(
#                             #         "CÓDIGO LIVRO NÃO ENCONTRADO.", cor=Cor.AMARELO)

#                 else:
#                     imprimir_cabecalho(
#                         "CÓDIGO DE FILIAL NÃO LOCALIZADO.", cor=Cor.AMARELO)

#             # for dados_filial in lista_filiais:
#             #     dados_filial.mostrar_informacoes_filial()

#             # escolha = continuar(
#             #     "Deseja vincular esse livro a outra filial? (S/N) ")

#             # if escolha:
#             #     continue
#             # else:
#             #     break


# def cadastrar_filial(lista_livros: list, lista_filiais: list):
#     imprimir_cabecalho("CADASTRO DE FILIAIS", cor=Cor.AZUL)

#     if verificar_lista(lista_filiais):
#         codigo = 1
#     else:
#         codigo = lista_filiais[-1].codigo + 1

#     print(f"{Cor.MAGENTA}CÓDIGO{Cor.RESET}: FL{codigo:02}")
#     nome_filial = verificar_vazio("NOME FILIAL: ", cor=Cor.MAGENTA)
#     endereco = verificar_vazio("ENDEREÇO: ", cor=Cor.MAGENTA)
#     contato = verificar_vazio("CONTATO: ", cor=Cor.MAGENTA)

#     lista_filiais.append(
#         Filial(
#             codigo=codigo,
#             nome=nome_filial,
#             endereco=endereco,
#             contato=contato,
#         ))

#     imprimir_cabecalho("FILIAL CADASTRADA COM SUCESSO.", cor=Cor.VERDE)

#     pausar()


def continuar(texto: str) -> bool:
    opcao = input(texto)

    if opcao.upper() == "S":
        return True
    elif opcao.upper() == "N":
        return False
    else:
        mostrar_erro("E02", Cor.VERMELHO)
        return True


# def buscar_livros_categoria(lista: list):
#     """
#     Efetua busca dos livros utilizando como parâmetro a categoria.

#     Args:
#         lista (list): Lista que será usada para exibir os dados.
#     """

#     imprimir_cabecalho("BUSCAR LIVROS POR CATEGORIA", cor=Cor.VERDE)
#     fazer_buscas(lista, "Digite a categoria desejada: ", "area", "E05")


def buscar_livros_preco(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro o preço do livro, optando por resultados
    maiores (>=) ou menores (<=) do valor desejado.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """

    imprimir_cabecalho("BUSCAR LIVROS POR PREÇO", cor=Cor.VERDE)

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

    imprimir_cabecalho("BUSCAR QUANTIDADE POR ESTOQUE", cor=Cor.VERDE)

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

    imprimir_cabecalho("VALOR TOTAL EM ESTOQUE", cor=Cor.VERDE)

    valor_total = sum(
        dados.valor * dados.quantidade_estoque for dados in lista)

    print(f"{Cor.VERDE}Valor total em estoque: {Cor.AMARELO}R$ {valor_total:.2f}{Cor.RESET}")
    pausar()


def encerrar_atividades(lista: list, alteracao: bool) -> None:
    """
    Encerra o sistema.

    Args:
        lista (list): Carrega lista para realizar verificações.
        alteracao (bool): Parâmetro que recebe um valor booleano
            True caso o arquivo tenha dados para serem gravados ou
            False caso não tenha dados.
    """

    if not verificar_lista(lista) and alteracao:

        imprimir_cabecalho(
            "Deseja atualizar arquivo de estoque? ", cor=Cor.AZUL)
        criar_menu(["SIM"], bloqueado=False)

        opcao = verificar_numero("Digite a opção desejada: ", int, Cor.AMARELO)

        if opcao == 1:
            salvar_livro(lista, nome_arquivo="livraria.txt")

    print(f"\n{Cor.VERDE}<<< SISTEMA ENCERRADO >>>{Cor.RESET}\n")
    exit()


def main():
    """
    Executa o ciclo principal do sistema de livraria. 

    Responsável por inicializar o ambiente, gerir o estado do stock, 
    exibir o menu interativo e coordenar a execução das funcionalidades 
    escolhidas pelo utilizador até ao encerramento do programa.
    """

    lista_livros = []
    lista_filiais = []
    sistema = Livraria(lista_livros, lista_filiais)
    escolhas_menu = {
        1: sistema.filiais,
        2: sistema.cadastrar_livros,
        3: sistema.listar_dados,
        4: sistema.buscar_livros_titulo,
        5: sistema.buscar_livros_categoria,
        6: buscar_livros_preco,
        7: buscar_quantidade_estoque,
        8: valor_total_estoque,
        9: sistema.carregar_estoque,
        10: sistema.atualizar_estoque,
    }
    estoque_carregado = False
    houve_alteracao = False

    inicializar_arquivo("livraria.txt")

    with open("livraria.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    if len(linhas) <= 1:
        estoque_carregado = True
    else:
        estoque_carregado = False

    while True:
        imprimir_cabecalho("SISTEMA DE LIVRARIA .v1", cor=Cor.LARANJA)

        criar_menu(
            [
                "FILIAIS",
                "CADASTRAR NOVO LIVRO",
                "LISTAR LIVROS",
                "BUSCAR LIVROS POR TÍTULO",
                "BUSCAR LIVROS POR CATEGORIA",
                "BUSCAR LIVROS POR PREÇO",
                "BUSCA POR QUANTIDADE EM ESTOQUE",
                "VALOR TOTAL EM ESTOQUE",
                "CARREGAR ESTOQUE",
                "ATUALIZAR ARQUIVO DE ESTOQUE"
            ],
            not estoque_carregado
        )

        opcao = verificar_numero("Digite a opção desejada: ", int, Cor.AMARELO)

        if not estoque_carregado and opcao != 9 and opcao != 0:
            mostrar_erro("E11", Cor.AMARELO)
            continue
        elif opcao == 9:
            estoque_carregado = True

        opcao_escolhida = escolhas_menu.get(opcao)

        if opcao_escolhida:
            tamanho_antes = len(sistema.livros)

            opcao_escolhida()

            tamanho_depois = len(sistema.livros)

            if tamanho_antes != tamanho_depois and opcao != 9:
                houve_alteracao = True
            elif opcao == 10:
                houve_alteracao = False

        elif opcao == 0:
            encerrar_atividades(lista_livros, houve_alteracao)
        else:
            mostrar_erro("E02", Cor.VERMELHO)


if __name__ == "__main__":
    main()
