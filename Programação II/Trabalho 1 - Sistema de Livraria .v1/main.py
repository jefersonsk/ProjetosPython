import os
from livro import Livro
from utilidades import (
    Cor,
    imprimir_cabecalho,
    criar_menu,
    verificar_lista,
    verificar_numero,
    verificar_vazio,
    validar_ano,
    pausar,
    mostrar_erro,
    fazer_buscas,
    escolher_operador
    )


#======================================
# MANIPULAÇÃO DE ARQUIVOS
#======================================


def inicializar_arquivo(nome_arquivo: str):
    cabecalho = ["CóDIGO",
                 "TíTULO",
                 "EDITORA",
                 "ÁREA/GÊNERO",
                 "ANO",
                 "VALOR",
                 "ESTOQUE"]

    arquivo_existe = os.path.exists(nome_arquivo)

    if not arquivo_existe or os.path.getsize(nome_arquivo) == 0:
        with open(nome_arquivo, "a") as arquivo:
            linha = ",".join(cabecalho)
            arquivo.write(linha + "\n")


def carregar_dados(lista: list, nome_arquivo: str) -> list:
    with open(nome_arquivo, "r") as arquivo:
        arquivo.readline()

        for dados in arquivo:
            try:
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

            except(ValueError, IndexError):
                print(f"{Cor.AMARELO}Aviso: Linha corrompida ignorada.{Cor.RESET}")

        return lista
        
    

def salvar_livro(lista: list, nome_arquivo: str) -> None:
    with open(nome_arquivo, "w") as arquivo:
        cabecalho = "CóDIGO,TÍTULO,EDITORA,ÁREA/GÊNERO,ANO,VALOR,ESTOQUE\n"
        arquivo.write(cabecalho)

        for livro in lista:
            dados = livro.formatar_para_csv()
            arquivo.write(dados + "\n")

        imprimir_cabecalho("DADOS GRAVADOS COM SUCESSO", cor=Cor.VERDE)


#======================================
# FUNÇÕES PRINCIPAIS
#======================================


def cadastrar_livros(lista: list):
    """
    Efetua o cadastro dos livros no sistema.

    Args:
        lista (list): Lista que será usada para armazenar os dados.
    """
    imprimir_cabecalho("CADASTRAR UM NOVO LIVRO", cor=Cor.AZUL)

    if verificar_lista(lista):
        codigo = 1
    else:
        codigo = lista[-1].codigo + 1

    print(f"{Cor.MAGENTA}CÓDIGO{Cor.RESET}: Cod#{codigo:04}")
    titulo = verificar_vazio("TÍTULO: ", cor=Cor.MAGENTA)
    editora = input(f"{Cor.MAGENTA}EDITORA: {Cor.RESET}")
    area = input(f"{Cor.MAGENTA}ÁREA: {Cor.RESET}")
    ano = validar_ano("ANO: ", cor=Cor.MAGENTA)
    valor = verificar_numero("VALOR: R$ ", float, Cor.MAGENTA)
    quantidade_estoque = verificar_numero("QUANTIDADE ESTOQUE: ", int, Cor.MAGENTA)

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

    imprimir_cabecalho("LIVRO CADASTRADO COM SUCESSO.", cor=Cor.VERDE)

    pausar()


def listar_dados(lista: list):
    """
    Exibe todos os dados de uma lista. Caso ela esteja em branco, uma mensagem de erro é exibida.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """

    imprimir_cabecalho("LISTAR LIVROS", cor=Cor.VERDE)

    if verificar_lista(lista):
        mostrar_erro("E03", Cor.AMARELO)
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
    imprimir_cabecalho("BUSCAR LIVROS POR TíTULO", cor=Cor.VERDE)
    fazer_buscas(lista, "Digite o título do livro: ", "titulo", "E04")


def buscar_livros_categoria(lista: list):
    """
    Efetua busca dos livros utilizando como parâmetro a categoria.

    Args:
        lista (list): Lista que será usada para exibir os dados.
    """
    imprimir_cabecalho("BUSCAR LIVROS POR CATEGORIA", cor=Cor.VERDE)
    fazer_buscas(lista, "Digite a categoria desejada: ", "area", "E05")


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


def carregar_estoque(lista: list) -> list:
    if verificar_lista(lista):
        lista_livros = carregar_dados(lista, "livraria.txt")
        imprimir_cabecalho("DADOS CARREGADOS", cor=Cor.VERDE)
        pausar()
        return lista_livros
    else:
        mostrar_erro("E10", Cor.VERMELHO)


def atualizar_estoque(lista: list):
    salvar_livro(lista, "livraria.txt")

    imprimir_cabecalho("ARQUIVO ATUALIZADO.", cor=Cor.VERDE)


def encerrar_atividades(lista: list) -> None:
    """
    Encerra o sistema.

    Args:
        _: Parâmetro ignorado intencionalmente (necessário para manter a
           assinatura do menu).
    """
    
    imprimir_cabecalho("Deseja atualizar arquivo de estoque? ", cor=Cor.AZUL)
    criar_menu(["SIM"], bloqueado=False)

    opcao = verificar_numero("Digite a opção desejada: ", int, Cor.AMARELO)

    if opcao == 1:
        salvar_livro(lista, "livraria.txt")

    print(f"\n{Cor.VERDE}<<< SISTEMA ENCERRADO >>>{Cor.RESET}\n")
    exit()


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
    estoque_carregado = False

    inicializar_arquivo("livraria.txt")
    # carregar_dados(lista_livros, "livraria.txt")

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
        imprimir_cabecalho("SISTEMA DE LIVRARIA .v1", cor=Cor.LARANJA)

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
            ], 
            not estoque_carregado
        )

        opcao = verificar_numero("Digite a opção desejada: ", int, Cor.AMARELO)

        if not estoque_carregado and opcao != 8 and opcao != 0:
            mostrar_erro("E11", Cor.VERMELHO)
            continue
        elif opcao == 8:
            estoque_carregado = True

        opcao_escolhida = escolhas_menu.get(opcao)

        if opcao_escolhida:
            opcao_escolhida(lista_livros)
        else:
            mostrar_erro("E02", Cor.VERMELHO)

if __name__ == "__main__":
    main()
