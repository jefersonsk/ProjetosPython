import os
from livro import Livro, Filial, Livraria
from utilidades import (
    Cor,
    imprimir_cabecalho,
    executar_submenu,
    criar_menu,
    verificar_lista,
    verificar_numero,
    verificar_vazio,
    pausar,
    mostrar_erro,
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
            linha = ";".join(cabecalho)
            arquivo.write(linha + "\n")


# ======================================
# FUNÇÕES PRINCIPAIS
# ======================================


def filiais(sistema):
    escolhas_menu = {
        1: sistema.cadastrar_filial,
        2: sistema.listar_filiais,
        3: sistema.adicionar_livros_filial
    }

    lista_opcoes = [
        "CADASTRO DE FILIAIS",
        "LISTAR FILIAIS",
        "ADICIONAR LIVRO A FILIAIS"
    ]

    executar_submenu("FILIAIS", lista_opcoes, escolhas_menu)


def livros(sistema):
    escolhas_menu = {
        1: sistema.cadastrar_livros,
        2: sistema.listar_livros
    }
    lista_opcoes = [
        "CADASTRAR NOVO LIVRO",
        "LISTAR LIVROS"
    ]

    executar_submenu("LIVROS", lista_opcoes, escolhas_menu)


def pesquisas(sistema):
    escolhas_menu = {
        1: sistema.buscar_livros_titulo,
        2: sistema.buscar_livros_categoria,
        3: sistema.buscar_livros_preco,
        4: sistema.buscar_quantidade_estoque,
    }
    lista_opcoes = [
        "BUSCAR LIVROS POR TÍTULO",
        "BUSCAR LIVROS POR CATEGORIA",
        "BUSCAR LIVROS POR PREÇO",
        "BUSCA POR QUANTIDADE EM ESTOQUE"
    ]

    executar_submenu("PESQUISAS", lista_opcoes, escolhas_menu)


def relatorios(sistema):
    escolhas_menu = {
        1: sistema.relatorio_estoque_por_livro,
        2: sistema.relatorio_estoque_por_filial,
        3: sistema.relatorio_completo
    }
    lista_opcoes = [
        "RELATÓRIO DE ESTOQUE POR LIVRO",
        "RELATÓRIO DE ESTOQUE POR FILIAL",
        "RELATÓRIO COMPLETO"
    ]

    executar_submenu("RELATÓRIOS", lista_opcoes, escolhas_menu)


def encerrar_atividades(sistema, alteracao: bool) -> None:
    """
    Encerra o sistema.

    Args:
        lista (list): Carrega lista para realizar verificações.
        alteracao (bool): Parâmetro que recebe um valor booleano
            True caso o arquivo tenha dados para serem gravados ou
            False caso não tenha dados.
    """

    if not verificar_lista(sistema) and alteracao:

        imprimir_cabecalho(
            "Deseja atualizar arquivo de estoque? ", cor=Cor.AZUL)
        criar_menu(["SIM"], bloqueado=False)

        opcao = verificar_numero("Digite a opção desejada: ", int, Cor.AMARELO)

        if opcao == 1:
            sistema.atualizar_estoque()

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
        1: lambda: filiais(sistema),
        2: lambda: livros(sistema),
        3: lambda: pesquisas(sistema),
        4: lambda: relatorios(sistema),
        5: sistema.carregar_estoque,
        6: sistema.atualizar_estoque,
    }
    precisa_carregar_arquivos = False
    houve_alteracao = False

    inicializar_arquivo("livraria.txt")

    with open("livraria.txt", "r", encoding="utf-8") as arquivo:
        linhas_livros = arquivo.readlines()

    with open("filial.txt", "r", encoding="utf-8") as arquivo:
        linhas_filiais = arquivo.readlines()

    precisa_carregar_arquivos = (
        len(linhas_livros) > 1 or len(linhas_filiais) > 1
    )

    while True:
        imprimir_cabecalho("SISTEMA DE LIVRARIA .v3", cor=Cor.LARANJA)

        criar_menu(
            [
                "FILIAIS",
                "LIVROS",
                "PESQUISAS",
                "RELATÓRIOS",
                "CARREGAR ESTOQUE",
                "ATUALIZAR ARQUIVO DE ESTOQUE"
            ],
            precisa_carregar_arquivos
        )

        opcao = verificar_numero("Digite a opção desejada: ", int, Cor.AMARELO)

        if precisa_carregar_arquivos and opcao != 5 and opcao != 0:
            mostrar_erro("E11", Cor.AMARELO)
            continue
        elif opcao == 5:
            precisa_carregar_arquivos = False

        opcao_escolhida = escolhas_menu.get(opcao)

        if opcao_escolhida:

            opcao_escolhida()

            if sistema.alteracoes_pendentes:
                houve_alteracao = True
            elif opcao == 6:
                houve_alteracao = False

        elif opcao == 0:
            encerrar_atividades(sistema, houve_alteracao)
        else:
            mostrar_erro("E02", Cor.VERMELHO)


if __name__ == "__main__":
    main()
