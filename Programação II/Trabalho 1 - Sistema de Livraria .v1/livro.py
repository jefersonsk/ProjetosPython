from utilidades import (
    Cor,
    imprimir_linha,
    imprimir_cabecalho,
    verificar_vazio,
    verificar_lista,
    validar_ano,
    pausar,
    mostrar_erro,
    verificar_numero,
    escolher_operador,
    condicao_atendida
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

    def buscar_livros_titulo(self):
        """
        Efetua busca dos livros utilizando como parâmetro o título.

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        imprimir_cabecalho("BUSCAR LIVROS POR TíTULO", cor=Cor.VERDE)
        self.fazer_buscas(self.livros, "Digite o título do livro: ",
                     "titulo", "E04")

    def buscar_livros_categoria(self):
        """
        Efetua busca dos livros utilizando como parâmetro a categoria.

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        imprimir_cabecalho("BUSCAR LIVROS POR CATEGORIA", cor=Cor.VERDE)
        self.fazer_buscas(
            self.livros, "Digite a categoria desejada: ", "area", "E05")

    def cadastrar_filial(self):
        imprimir_cabecalho("CADASTRO DE FILIAIS", cor=Cor.AZUL)

        if verificar_lista(self.filiais):
            codigo = 1
        else:
            codigo = self.filiais[-1].codigo + 1

        print(f"{Cor.MAGENTA}CÓDIGO{Cor.RESET}: FL{codigo:02}")
        nome_filial = verificar_vazio("NOME FILIAL: ", cor=Cor.MAGENTA)
        endereco = verificar_vazio("ENDEREÇO: ", cor=Cor.MAGENTA)
        contato = verificar_vazio("CONTATO: ", cor=Cor.MAGENTA)

        self.filiais.append(
            Filial(
                codigo=codigo,
                nome=nome_filial,
                endereco=endereco,
                contato=contato,
            ))

        imprimir_cabecalho("FILIAL CADASTRADA COM SUCESSO.", cor=Cor.VERDE)

        pausar()

    def listar_filiais(self):
        imprimir_cabecalho("LISTA DE FILIAIS", cor=Cor.VERDE)

        if verificar_lista(self.filiais):
            mostrar_erro("E03", Cor.AMARELO)
        else:
            for dados in self.filiais:
                dados.mostrar_informacoes()

            pausar()

    def adicionar_livros_filial(self):
        if verificar_lista(self.livros) or verificar_lista(self.filiais):
            mostrar_erro("E04", Cor.AMARELO)
        else:
            filial_encontrada = self.fazer_buscas(
                self.filiais,
                "Digite o código da filial: ",
                "ADICIONAR LIVRO A FILIAL",
                "codigo",
                "E04",
                tipo_dado=int
            )

            if filial_encontrada is None:
                return

            livro_encontrado = self.fazer_buscas(
                self.livros,
                "Digite o código do livro: ",
                "ADICIONAR LIVRO A FILIAL",
                "codigo",
                "E04",
                tipo_dado=int
            )

            if filial_encontrada is None:
                return

            valor_atribuido = verificar_numero(
                "Digite o preço do livro: R$ ", float, Cor.AMARELO)
            quantidade_estoque = verificar_numero(
                "Digite a quantidade em estoque: ", int, Cor.AMARELO)

            filial_encontrada.adicionar_ao_estoque(
                livro_encontrado, valor_atribuido, quantidade_estoque)

            filial_encontrada.mostrar_livros_filial()

    def fazer_buscas(self,
                     lista: list,
                     pergunta: str,
                     cabecalho: str,
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

            imprimir_cabecalho(cabecalho, cor=Cor.AZUL)
            print(f"{Cor.VERDE}Para sair digite 0.{Cor.RESET}")

            if tipo_dado == str:
                pesquisa = input(f"{Cor.AMARELO}{pergunta}{Cor.RESET}")
            else:
                pesquisa = verificar_numero(pergunta, tipo_dado, cor=Cor.AMARELO)

            if pesquisa in (0, "0"):
                return None

            imprimir_cabecalho("RESULTADO DA PESQUISA", cor=Cor.MAGENTA_CLARO)

            for dados in lista:
                dado_pesquisado = getattr(dados, nome_atributo)

                if condicao_atendida(dado_pesquisado, pesquisa, operador):
                    dados.mostrar_informacoes()
                    return dados

            if not encontrou:
                mostrar_erro(erro, Cor.AMARELO)
            else:
                pausar()
                # return None


    def buscar_quantidade_estoque(self):
        """
        Efetua busca dos livros utilizando como parâmetro a quantidade em estoque, optando por valores
        maiores (>=) ou menores (<=).

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        operador = escolher_operador("Como deseja buscar a quantidade do estoque?")

        if operador is None:
            return

        self.fazer_buscas(
            self.filiais,
            "Digite a quantidade em estoque: ",
            "BUSCAR POR QUANTIDADE EM ESTOQUE",
            "quantidade_estoque",
            "E07",
            operador,
            int,
        )

    def verificar_estoque_por_livro(self):
        if verificar_lista(self.livros) or verificar_lista(self.filiais):
            mostrar_erro("E04", Cor.AMARELO)
        else:
            livro_encontrado = self.fazer_buscas(
                self.livros,
                "Digite o código do livro: ",
                "VERIFICAR ESTOQUE POR LIVRO",
                "codigo",
                "E04",
                tipo_dado=int
            )

            if livro_encontrado is None:
                return