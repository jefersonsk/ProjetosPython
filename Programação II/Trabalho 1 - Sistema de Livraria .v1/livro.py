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
            f"{Cor.AZUL}Título / Editora: "
            f"{Cor.AMARELO}{self.titulo} / {self.editora}{Cor.RESET}"
        )
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

    def formatar_para_csv(self):
        return (
            f"{self.livro.codigo},"
            f"{self.livro.titulo},"
            f"{self.livro.ano},"
            f"{self.livro.editora},"
            f"R${self.valor:.2f},"
            f"{self.quantidade_estoque}"
        )

    def mostrar_informacoes(self):
        print(
            f"{Cor.AZUL}Código: "
            f"{Cor.AMARELO}Cod#{self.livro.codigo:04}{Cor.RESET}"
        )
        print(
            f"{Cor.AZUL}Título / Editora: {Cor.AMARELO}{self.livro.titulo}"
            f" / {self.livro.editora}{Cor.RESET}"
        )
        print(
            f"{Cor.AZUL}Preço: {Cor.AMARELO}R$ {self.valor:<40.2f}{Cor.RESET}"
            f"{Cor.AZUL}Quantidade:  {Cor.AMARELO}{self.quantidade_estoque}"
            f"{Cor.RESET}"
        )
        imprimir_linha()


class Filial:
    def __init__(self, codigo, nome, endereco, contato):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.contato = contato
        self.livros = []

    def formatar_para_csv(self):
        return f"#FL{self.codigo},{self.nome},{self.endereco},{self.contato}"

    def adicionar_ao_estoque(self, livro, valor, quantidade_estoque):
        novo_item = ItemEstoque(livro, valor, quantidade_estoque)
        self.livros.append(novo_item)

    def mostrar_informacoes(self):
        print(
            f"{Cor.AZUL}Código Filial: "
            f"{Cor.AMARELO}{self.codigo:02}{Cor.RESET}"
        )
        print(f"{Cor.AZUL}Nome Filial: {Cor.AMARELO}{self.nome}{Cor.RESET}")
        print(f"{Cor.AZUL}Endereço: {Cor.AMARELO}{self.endereco}{Cor.RESET}")
        print(f"{Cor.AZUL}Contato: {Cor.AMARELO}{self.contato}{Cor.RESET}")

    def mostrar_informacoes_resumidas(self):
        print(
            f"{Cor.AZUL}Código Filial: "
            f"{Cor.AMARELO}{self.codigo:02}{Cor.RESET} "
            f"{Cor.AZUL}Nome: {Cor.AMARELO}{self.nome}{Cor.RESET}"
        )

    def mostrar_livros_filial(self):
        valor_total_estoque = 0

        imprimir_cabecalho(
            f"{Cor.AZUL}LISTAGEM DE LIVROS CADASTRADOS NA FILIAL {Cor.RESET}")

        if not self.livros:
            print("Nenhum livro cadastrado na filial.")
        else:
            for dados_livro_filial in self.livros:
                print(
                    f"{Cor.AZUL}Código: "
                    f"{Cor.AMARELO}Cod#{dados_livro_filial.livro.codigo:04}"
                )
                print(
                    f"{Cor.AZUL}Título / Editora: "
                    f"{Cor.AMARELO}{dados_livro_filial.livro.titulo} / "
                    f"{dados_livro_filial.livro.editora}{Cor.RESET}"
                )

                print(
                    f"{Cor.AZUL}Preço: R$ "
                    f"{Cor.AMARELO}{dados_livro_filial.valor:<30.2f}{Cor.RESET}"
                    f"{Cor.AZUL}Quantidade em Estoque: "
                    f"{Cor.AMARELO}{dados_livro_filial.quantidade_estoque}"
                    f"{Cor.RESET}"
                )

                valor_total_estoque += (
                    dados_livro_filial.valor
                    * dados_livro_filial.quantidade_estoque
                )

                imprimir_linha()

            print(
                f"{Cor.AZUL}Valor Total de Estoque: "
                f"{Cor.AMARELO}R$ {valor_total_estoque:.2f}{Cor.RESET}")


class Livraria:
    def __init__(self, livros, filiais):
        self.livros = livros
        self.filiais = filiais
        self.alteracoes_pendentes = False

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

        self.alteracoes_pendentes = True

        pausar()

    def carregar_dados(self, nome_arquivo: str, tipo: str) -> list:
        """
        Carrega os dados de um arquivo em uma lista no sistema.

        Args:
            lista (list): lista onde os dados devem ser carregados.
            nome_arquivo (str): Nome do arquivo onde os dados estão salvos.

        Returns:
            list: Retorna lista com os dados já carregados.
        """

        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            arquivo.readline()

            for dados in arquivo:
                try:
                    linha_limpa = dados.strip()

                    if not linha_limpa:
                        continue

                    cache = dados.strip().split(",")

                    if tipo == "livro":
                        dados_livro = Livro(
                            codigo=int(cache[0]),
                            titulo=cache[1],
                            editora=cache[2],
                            area=cache[3],
                            ano=int(cache[4])
                        )

                        self.livros.append(dados_livro)

                    elif tipo == "filial":
                        dados_filial = Filial(
                            codigo=int(cache[0].replace("#FL", "")),
                            nome=cache[1],
                            endereco=cache[2],
                            contato=cache[3]
                        )

                        self.filiais.append(dados_filial)

                    elif tipo == "estoque_completo":
                        if linha_limpa.startswith("#FL"):
                            filial_atual = None

                            codigo_filial = int(cache[0].replace("#FL", ""))

                            for item_filial in self.filiais:
                                if item_filial.codigo == codigo_filial:
                                    filial_atual = item_filial
                                    break
                            if filial_atual is None:
                                mostrar_erro("E12", Cor.VERMELHO)

                        else:
                            if filial_atual is not None:
                                codigo_livro = int(cache[0])
                                preco = float(cache[4].replace("R$", ""))
                                quantidade = int(cache[5])

                                livro_atual = None

                                for item_livro in self.livros:
                                    if item_livro.codigo == codigo_livro:
                                        livro_atual = item_livro
                                        break

                                if livro_atual:
                                    filial_atual.adicionar_ao_estoque(
                                        livro_atual,
                                        preco,
                                        quantidade
                                    )

                except (ValueError, IndexError):
                    print(
                        f"{Cor.AMARELO}Aviso: Linha corrompida ignorada."
                        f"{Cor.RESET}"
                    )

    def carregar_estoque(self) -> list:
        """
        Carrega os dados do arquivo para uma lista.

        Args:
            lista (list): Lista onde os dados devem ser carregados.

        Returns:
            list: Retorno com a lista com os dados já carregados.
        """

        if verificar_lista(self.livros):
            self.carregar_dados("livraria.txt", "livro")
            self.carregar_dados("filial.txt", "filial")
            self.carregar_dados("estoque_completo.txt", "estoque_completo")

            imprimir_cabecalho("DADOS CARREGADOS", cor=Cor.VERDE)
            pausar()
        else:
            mostrar_erro("E10", Cor.VERMELHO)

    def listar_dados(self):
        """
        Exibe todos os dados de uma lista. Caso ela esteja em branco,
        uma mensagem de erro é exibida.

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
        self.salvar_filial("filial.txt")
        self.salvar_estoque_completo("estoque_completo.txt")

        imprimir_cabecalho(
            "TODOS OS ARQUIVOS ATUALIZADOS COM SUCESSO.", cor=Cor.VERDE
        )

    def salvar_livro(self, nome_arquivo: str) -> None:
        """
        Salva os dados da lista em um arquivo.

        Args:
            lista (list): Lista com os dados que devem ser salvos.
            nome_arquivo (str): Nome do arquivo em que os dados serão salvos.
        """

        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            cabecalho = "CóDIGO,TÍTULO,EDITORA,ÁREA/GÊNERO,ANO,VALOR,ESTOQUE\n"
            arquivo.write(cabecalho)

            for livro in self.livros:
                dados = livro.formatar_para_csv()
                arquivo.write(dados + "\n")

    def salvar_filial(self, nome_arquivo: str) -> None:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            cabecalho = "CÓDIGO,NOME,ENDEREÇO,CONTATO\n"
            arquivo.write(cabecalho)

            for filial in self.filiais:
                dados = filial.formatar_para_csv()
                arquivo.write(dados + "\n")

    def salvar_estoque_completo(self, nome_arquivo: str) -> None:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            cabecalho = "CÓDIGO,NOME,ENDEREÇO,CONTATO\n"
            arquivo.write(cabecalho)

            for filial in self.filiais:
                dados_filiais = filial.formatar_para_csv()
                arquivo.write(dados_filiais + "\n")

                for item in filial.livros:
                    dados_livros = item.formatar_para_csv()
                    arquivo.write(dados_livros + "\n")

    def buscar_livros_titulo(self):
        """
        Efetua busca dos livros utilizando como parâmetro o título.

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        # imprimir_cabecalho("BUSCAR LIVROS POR TíTULO", cor=Cor.VERDE)
        self.fazer_buscas(
            self.livros,
            "Digite o título do livro",
            "BUSCAR LIVROS POR TíTULO",
            "titulo",
            "E04"
        )

    def buscar_livros_categoria(self):
        """
        Efetua busca dos livros utilizando como parâmetro a categoria.

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        self.fazer_buscas(
            self.livros,
            "Digite a categoria desejada",
            "BUSCAR LIVROS POR CATEGORIA",
            "area",
            "E05"
        )

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

        self.alteracoes_pendentes = True

        pausar()

    def listar_filiais(self):
        imprimir_cabecalho("LISTA DE FILIAIS", cor=Cor.VERDE)

        if verificar_lista(self.filiais):
            mostrar_erro("E03", Cor.AMARELO)
        else:
            for dados in self.filiais:
                dados.mostrar_informacoes()
                imprimir_linha()

            pausar()

    def adicionar_livros_filial(self):
        if verificar_lista(self.livros) or verificar_lista(self.filiais):
            mostrar_erro("E06", Cor.AMARELO)
        else:
            filial_encontrada = self.fazer_buscas(
                self.filiais,
                "Digite o código da filial",
                "ADICIONAR LIVRO A FILIAL",
                "codigo",
                "E04",
                tipo_dado=int
            )

            if filial_encontrada is None:
                return

            livro_encontrado = self.fazer_buscas(
                self.livros,
                "Digite o código do livro",
                "ADICIONAR LIVRO A FILIAL",
                "codigo",
                "E04",
                tipo_dado=int
            )

            for item in filial_encontrada.livros:
                if item.livro.codigo == livro_encontrado.codigo:
                    print("CADASTRO DUPLICADO")

                    pausar()

                    return

            if livro_encontrado is None:
                return

            valor_atribuido = verificar_numero(
                "Digite o preço do livro: R$ ", float, Cor.AMARELO)
            quantidade_estoque = verificar_numero(
                "Digite a quantidade em estoque: ", int, Cor.AMARELO)

            filial_encontrada.adicionar_ao_estoque(
                livro_encontrado, valor_atribuido, quantidade_estoque)

            filial_encontrada.mostrar_livros_filial()

            self.alteracoes_pendentes = True

    def fazer_buscas(self,
                     lista: list,
                     pergunta: str,
                     cabecalho: str,
                     nome_atributo: str,
                     erro: str,
                     operador: str = "==",
                     tipo_dado: type = str,
                     sufixo: str = ""
                     ) -> None:
        """
        Realiza a busca pelos dados conforme escolha definida pelo usuário.
        Se não encontrar o dado solicitado, retorna mensagem de aviso.

        Args:
            lista_livros (list): Lista onde estão os dados cadastrados.
            texto (str): Texto da pergunta que será mostrada para o usuário.
            nome_atributo (str): Qual atributo de classe será utilizado na busca dos dados.
            erro (str): Código de aviso, onde a mensagem será capturada no dicionário MENSAGEM_ERRO.
            operador (str, optional): Operador que deve ser utilizado para realizar a busca, ">=", "<=" ou "==". Default é "==".
            tipo_dado (type, optional): Tipo de dado que será informado para busca: "int", "float" ou "str". Default é "str".
        """
        encontrou = False
        prompt_completo = f"{pergunta} [ou 0 para SAIR]: {sufixo} "

        if verificar_lista(lista):
            mostrar_erro("E03", Cor.AMARELO)
            return

        while True:

            imprimir_cabecalho(cabecalho, cor=Cor.AZUL)

            if tipo_dado == str:
                pesquisa = input(
                    f"{Cor.AMARELO}{prompt_completo}{Cor.RESET}")
            else:
                pesquisa = verificar_numero(
                    prompt_completo, tipo_dado, cor=Cor.AMARELO)

            if pesquisa in (0, "0"):
                return None

            imprimir_cabecalho("RESULTADO DA PESQUISA", cor=Cor.MAGENTA_CLARO)

            for dados in lista:
                dado_pesquisado = getattr(dados, nome_atributo)

                if condicao_atendida(dado_pesquisado, pesquisa, operador):
                    dados.mostrar_informacoes()
                    encontrou = True

            if not encontrou:
                mostrar_erro(erro, Cor.AMARELO)
            else:
                pausar()
                return

    def buscar_quantidade_estoque(self):
        """
        Efetua busca dos livros utilizando como parâmetro a quantidade em 
        estoque, optando por valores maiores (>=) ou menores (<=).

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        todos_os_livros = [
            livro for filial in self.filiais for livro in filial.livros]

        operador = escolher_operador(
            "Como deseja buscar a quantidade do estoque?")

        if operador is None:
            return

        self.fazer_buscas(
            todos_os_livros,
            "Digite a quantidade em estoque",
            "BUSCAR POR QUANTIDADE EM ESTOQUE",
            "quantidade_estoque",
            "E07",
            operador,
            int,
        )

    def verificar_estoque_por_livro(self):
        valor_total_estoque = 0
        livro_no_estoque = False

        if verificar_lista(self.livros) or verificar_lista(self.filiais):
            mostrar_erro("E06", Cor.AMARELO)
        else:
            livro_escolhido = self.fazer_buscas(
                self.livros,
                "Digite o código do livro",
                "VERIFICAR ESTOQUE POR LIVRO",
                "codigo",
                "E04",
                tipo_dado=int
            )

            if livro_escolhido is None:
                return

            for filial in self.filiais:
                for item in filial.livros:
                    if livro_escolhido.codigo == item.livro.codigo:
                        livro_no_estoque = True

                        print(
                            f"{Cor.AZUL}Valor: "
                            f"{Cor.AMARELO}R$ {item.valor:.2f} >> "
                            f"{Cor.AZUL}Filial "
                            f"{Cor.AMARELO}{filial.nome:<20}"
                            f"{Cor.AZUL}Estoque: "
                            f"{Cor.AMARELO}{item.quantidade_estoque}"
                            f"{Cor.RESET}"
                        )

                        valor_total_estoque += (
                            item.quantidade_estoque * item.valor
                        )

            imprimir_linha()
            if not livro_no_estoque:
                print(
                    f"{Cor.AMARELO}Este livro ainda não foi adicionado "
                    f"ao estoque de nenhuma filial.{Cor.RESET}"
                )
            else:
                print(
                    f"{Cor.AZUL}Valor total em estoque: R$ "
                    f"{Cor.AMARELO}{valor_total_estoque:.2f}{Cor.RESET}"
                )

            pausar()

    def verificar_estoque_por_filial(self):
        filial_cadastrada = False
        valor_total_estoque = 0

        if verificar_lista(self.livros) or verificar_lista(self.filiais):
            mostrar_erro("E06", Cor.AMARELO)
        else:
            filial_escolhida = self.fazer_buscas(
                self.filiais,
                "Digite o código da filial",
                "VERIFICAR ESTOQUE DA FILIAL",
                "codigo",
                "E12",
                tipo_dado=int
            )

            if filial_escolhida is None:
                return

            filial_escolhida.mostrar_livros_filial()

            pausar()

    def buscar_livros_preco(self):
        """
        Efetua busca dos livros utilizando como parâmetro o preço do livro,
        optando por resultados maiores (>=) ou menores (<=) do valor desejado.

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        todos_os_livros = [
            livro for filial in self.filiais for livro in filial.livros
        ]

        operador = escolher_operador("Como deseja buscar o preço?")

        if operador is None:
            return

        self.fazer_buscas(
            todos_os_livros,
            "Digite o preço da pesquisa",
            "BUSCAR LIVROS POR PREÇO",
            "valor",
            "E06",
            operador,
            float,
            "R$"
        )

    def valor_total_estoque(self):
        """
        Calcula o valor total em estoque.

        Args:
            lista (list): Lista que será usada para exibir os dados.
        """

        todos_os_livros = [
            livro for filial in self.filiais for livro in filial.livros
        ]

        imprimir_cabecalho("VALOR TOTAL EM ESTOQUE", cor=Cor.VERDE)

        valor_total = sum(
            dados.calcular_valor_total() for dados in todos_os_livros
        )

        print(
            f"{Cor.VERDE}Valor total em estoque: "
            f"{Cor.AMARELO}R$ {valor_total:.2f}{Cor.RESET}"
        )

        pausar()
