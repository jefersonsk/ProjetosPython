from utilidades import (
    Cor,
    imprimir_linha,
    imprimir_cabecalho,
    verificar_vazio,
    verificar_lista,
    validar_ano,
    pausar,
    mostrar_erro
)


class Livro:
    def __init__(self, titulo, codigo, editora, area, ano):

        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano

    def mostrar_informacoes(self):
        print(f"{Cor.VERDE_CLARO}{'>' * 6} Cod#{self.codigo:04}{Cor.RESET}")
        print(
            f"{Cor.AZUL}Título / Editora: {Cor.AMARELO}{self.titulo} / {self.editora}{Cor.RESET}")
        print(f"{Cor.AZUL}Categoria: {Cor.AMARELO}{self.area}{Cor.RESET}")
        print(f"{Cor.AZUL}Ano: {Cor.AMARELO}{self.ano}{Cor.RESET}")

        imprimir_linha("-")

    def formatar_para_csv(self):
        return f"{self.codigo},{self.titulo},{self.editora},{self.area},{self.ano}"


class ItemEstoque:
    def __init__(self, livro, valor, quantidade_estoque):
        self.livro = livro
        self.valor = valor
        self.quantidade_estoque = quantidade_estoque

    def calcular_valor_total(self):
        return self.valor * self.quantidade_estoque


class Filial:
    def __init__(self, codigo, nome, endereco, contato):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.livros = []

    def adicionar_ao_estoque(self, livro, valor, quantidade_estoque):
        novo_item = ItemEstoque(livro, valor, quantidade_estoque)
        self.livros.append(novo_item)

    def mostrar_informacoes(self):
        print(f"{Cor.AZUL}Código Filial: {Cor.AMARELO}{self.codigo:02}{Cor.RESET}")
        print(f"{Cor.AZUL}Nome Filial: {Cor.AMARELO}{self.nome}{Cor.RESET}")
        print(f"{Cor.AZUL}Endereço: {Cor.AMARELO}{self.endereco}{Cor.RESET}")
        print(f"{Cor.AZUL}Contato: {Cor.AMARELO}{self.contato}{Cor.RESET}")

    def mostrar_informacoes_resumidas(self):
        print(
            f"{Cor.AZUL}Código Filial: {Cor.AMARELO}{self.codigo:02}{Cor.RESET} "
            f"{Cor.AZUL}Nome: {Cor.AMARELO}{self.nome}{Cor.RESET}"
        )

    def mostrar_livros_filial(self):
        imprimir_cabecalho(
            f"{Cor.AZUL}LISTAGEM DE LIVROS CADASTRADOS NA FILIAL {Cor.RESET}")
        if not self.livros:
            print("Nenhum livro cadastrado na filial.")
        else:
            for dados_livro_filial in self.livros:
                print(
                    f"{Cor.AZUL}Código: Cod#{Cor.AMARELO}{dados_livro_filial.livro.codigo:04}")
                print(
                    f"{Cor.AZUL}Título / Editora: {Cor.AMARELO}{dados_livro_filial.livro.titulo} / {dados_livro_filial.livro.editora}{Cor.RESET}")

                print(
                    f"{Cor.AZUL}Preço: R$ {Cor.AMARELO}{dados_livro_filial.valor:.2f}{Cor.RESET}")
                print(
                    f"{Cor.AZUL}Quantidade em Estoque: {Cor.AMARELO}{dados_livro_filial.quantidade_estoque}{Cor.RESET}")
                print(
                    f"{Cor.AZUL}Valor Total: R$ {Cor.AMARELO}{dados_livro_filial.calcular_valor_total():.2f}{Cor.RESET}")


class Livraria:
    def __init__(self, livros, filiais):
        self.livros = livros
        self.filiais = filiais

    def cadastrar_livros(self):
        """
        Efetua o cadastro dos livros no sistema.

        Args:
            lista (list): Lista que será usada para armazenar os dados.
        """

        imprimir_cabecalho("CADASTRAR UM NOVO LIVRO", cor=Cor.AZUL)

        if verificar_lista(self.livros):
            codigo = 1
        else:
            codigo = self.livros[-1].codigo + 1

        print(f"{Cor.MAGENTA}CÓDIGO{Cor.RESET}: Cod#{codigo:04}")
        titulo = verificar_vazio("TÍTULO: ", cor=Cor.MAGENTA)
        editora = input(f"{Cor.MAGENTA}EDITORA: {Cor.RESET}")
        area = input(f"{Cor.MAGENTA}ÁREA: {Cor.RESET}")
        ano = validar_ano("ANO: ", cor=Cor.MAGENTA)

        self.livros.append(
            Livro(
                codigo=codigo,
                titulo=titulo,
                editora=editora,
                area=area,
                ano=ano
            )
        )

        imprimir_cabecalho("LIVRO CADASTRADO COM SUCESSO.", cor=Cor.VERDE)

        pausar()

    def carregar_dados(self, nome_arquivo) -> list:
        """
        Carrega os dados de um arquivo em uma lista no sistema.

        Args:
            lista (list): lista onde os dados devem ser carregados.
            nome_arquivo (str): Nome do arquivo onde os dados estão salvos.

        Returns:
            list: Retorna lista com os dados já carregados.
        """

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
                        ano=int(cache[4])
                    )

                    self.livros.append(dados_livro)

                except (ValueError, IndexError):
                    print(
                        f"{Cor.AMARELO}Aviso: Linha corrompida ignorada.{Cor.RESET}")

    def carregar_estoque(self) -> list:
        """
        Carrega os dados do arquivo para uma lista.

        Args:
            lista (list): Lista onde os dados devem ser carregados.

        Returns:
            list: Retorno com a lista com os dados já carregados.
        """

        if verificar_lista(self.livros):
            self.carregar_dados("livraria.txt")
            imprimir_cabecalho("DADOS CARREGADOS", cor=Cor.VERDE)
            pausar()
        else:
            mostrar_erro("E10", Cor.VERMELHO)

    def listar_dados(self):
        """
        Exibe todos os dados de uma lista. Caso ela esteja em branco, uma mensagem de erro é exibida.

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        imprimir_cabecalho("LISTA DE LIVROS CADASTRADOS", cor=Cor.VERDE)

        if verificar_lista(self.livros):
            mostrar_erro("E03", Cor.AMARELO)
        else:
            for dados in self.livros:
                dados.mostrar_informacoes()

            pausar()

    def atualizar_estoque(self) -> None:
        """
        Grava os dados adicionandos no arquivo informado.

        Args:
            lista (list): Lista com os dados a serem gravados no arquivo
        """

        self.salvar_livro("livraria.txt")

        imprimir_cabecalho("ARQUIVO ATUALIZADO.", cor=Cor.VERDE)

    def salvar_livro(self, nome_arquivo: str) -> None:
        """
        Salva os dados da lista em um arquivo.

        Args:
            lista (list): Lista com os dados que devem ser salvos.
            nome_arquivo (str): Nome do arquivo em que os dados serão salvos.
        """

        with open(nome_arquivo, "w") as arquivo:
            cabecalho = "CóDIGO,TÍTULO,EDITORA,ÁREA/GÊNERO,ANO,VALOR,ESTOQUE\n"
            arquivo.write(cabecalho)

            for livro in self.livros:
                dados = livro.formatar_para_csv()
                arquivo.write(dados + "\n")

            imprimir_cabecalho("DADOS GRAVADOS COM SUCESSO", cor=Cor.VERDE)
