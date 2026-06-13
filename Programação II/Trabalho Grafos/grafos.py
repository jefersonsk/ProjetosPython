from utilidades import (
    Cor,
    verificar_numero,
    imprimir_cabecalho,
    criar_menu,
    enter_para_sair,
    mostrar_erro,
    normalizar_texto,
    imprimir_linha,
    pausar
)


class Aresta:
    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia


class Vertice:
    def __init__(self, nome_cidade):
        self.nome_cidade = nome_cidade
        self.vizinhanca = []
        self.conexoes = []


class Grafo:
    def __init__(self):
        self.cidades = []
        self.conexoes = []

    def cadastra_cidade(self, nome):
        nome_normalizado = normalizar_texto(nome)

        for item in self.cidades:
            cidade_normalizada = normalizar_texto(
                item.nome_cidade)

            if cidade_normalizada == nome_normalizado:
                return False

        nova_cidade = Vertice(nome)
        self.cidades.append(nova_cidade)
        return True

    def cadastra_conexao(self, nome_cidade1, nome_cidade2, distancia):
        vertice1 = None
        vertice2 = None
        nome_cidade1_normalizada = (
            normalizar_texto(nome_cidade1)
        )
        nome_cidade2_normalizada = (
            normalizar_texto(nome_cidade2)
        )

        for item in self.cidades:
            cidade_normalizada = (
                normalizar_texto(item.nome_cidade)
            )

            if cidade_normalizada == nome_cidade1_normalizada:
                vertice1 = item
            elif cidade_normalizada == nome_cidade2_normalizada:
                vertice2 = item

        if vertice1 is None or vertice2 is None:
            return False

        nova_aresta = Aresta(vertice1, vertice2, distancia)

        self.conexoes.append(nova_aresta)

        vertice1.vizinhanca.append(vertice2)
        vertice2.vizinhanca.append(vertice1)
        vertice1.conexoes.append(nova_aresta)
        vertice2.conexoes.append(nova_aresta)
        return True

    def lista_cidades(self):
        nomes_cidades = []

        for item in self.cidades:
            nomes_cidades.append(item.nome_cidade)

        nomes_cidades.sort()

        for item in nomes_cidades:
            print(f"{Cor.AMARELO}{item}{Cor.RESET}")

    def lista_conexoes(self):
        for aresta in self.conexoes:
            print(
                f"{Cor.AZUL}{aresta.cidade1.nome_cidade}, "
                f"{aresta.cidade2.nome_cidade}: "
                f"{Cor.AMARELO}{aresta.distancia} Km{Cor.RESET}"
            )

    def lista_vizinhas(self, nome_cidades):
        cidade_alvo = None
        lista_vizinhos = []

        for item in self.cidades:
            if (
                normalizar_texto(item.nome_cidade)
                == normalizar_texto(nome_cidades)
            ):
                cidade_alvo = item
                break

        if cidade_alvo is not None:
            for item in cidade_alvo.conexoes:
                if item.cidade1 == cidade_alvo:
                    lista_vizinhos.append(
                        [item.distancia, item.cidade2.nome_cidade])
                else:
                    lista_vizinhos.append(
                        [item.distancia, item.cidade1.nome_cidade])

            lista_vizinhos.sort()

            imprimir_cabecalho(
                f"Lista de Cidades Vizinhas de {cidade_alvo.nome_cidade}",
                cor=Cor.VERDE
            )

            for item in lista_vizinhos:
                print(
                    f"{Cor.AZUL}{item[1]}: {Cor.AMARELO}{item[0]:.2f} Km"
                    f"{Cor.RESET}"
                )
        else:
            mostrar_erro("E03", cor=Cor.AMARELO)

    @classmethod
    def carregar_arquivo(cls, nome_arquivo):
        novo_grafo = cls()
        linha = 1

        try:
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                for dados in arquivo:
                    cache = dados.strip().split(";")

                    if len(cache) < 3:
                        imprimir_linha()

                        print(
                            f"{Cor.VERMELHO}Dados Corrompidos."
                            f"Linha {linha} não carregada.{Cor.RESET}"
                        )

                        continue
                    try:
                        distancia = float(cache[2])
                    except ValueError:
                        imprimir_linha()

                        print(
                            f"{Cor.VERMELHO}Dados Corrompidos."
                            f"Linha {linha} não carregada.{Cor.RESET}"
                        )

                        continue

                    linha += 1

                    novo_grafo.cadastra_cidade(cache[0])
                    novo_grafo.cadastra_cidade(cache[1])

                    if cache[0] != cache[1]:

                        novo_grafo.cadastra_conexao(
                            cache[0], cache[1], float(cache[2])
                        )

        except FileNotFoundError:
            pass

        return novo_grafo

    def salva_arquivo(self):
        with open("grafos.csv", "w", encoding="utf-8") as arquivo:
            for dados in self.cidades:
                if not dados.vizinhanca:
                    linha = f"{dados.nome_cidade};{dados.nome_cidade};0"
                    arquivo.write(linha + "\n")

            for dados in self.conexoes:
                linha = (
                    f"{dados.cidade1.nome_cidade};"
                    f"{dados.cidade2.nome_cidade};"
                    f"{dados.distancia}"
                )
                arquivo.write(linha + "\n")


# ================================
#   FERRAMENTAS DO SISTEMA
# ================================


def obter_cidade_validada(
    objeto: Grafo, mensagem_input: str, tipo_validacao: str
):

    while True:
        cidade_digitada = enter_para_sair(mensagem_input, Cor.MAGENTA)

        if not cidade_digitada:
            return False

        if tipo_validacao == "se_nao_existe":
            for item in objeto.cidades:
                if (
                    normalizar_texto(item.nome_cidade)
                    == normalizar_texto(cidade_digitada)
                ):
                    return cidade_digitada

            mostrar_erro("E03", Cor.AMARELO)

        elif tipo_validacao == "se_existe":
            cidade_cadastrada = objeto.cadastra_cidade(cidade_digitada)

            if not cidade_cadastrada:
                mostrar_erro("E02", Cor.AMARELO)
                continue

            return cidade_digitada


# ================================
#   FUNCIONALIDADES DO SISTEMA
# ================================


def cadastrar_cidades(objeto: Grafo):
    imprimir_cabecalho("CADASTRAR CIDADE", cor=Cor.LARANJA)

    while True:
        cidade = obter_cidade_validada(
            objeto, "Digite o nome da cidade", tipo_validacao="se_existe"
        )

        if not cidade:
            return

        print(
            f"\n{Cor.CIANO}Cidade {Cor.AMARELO}{cidade}{Cor.CIANO}"
            f" cadastrada com sucesso!\n{Cor.RESET}"
        )


def cadastrar_conexoes(objeto: Grafo):
    imprimir_cabecalho("CADASTRAR CONEXÕES", cor=Cor.LARANJA)

    if len(objeto.cidades) < 2:
        mostrar_erro("E04", Cor.AMARELO)
        return

    cidade_01 = obter_cidade_validada(
        objeto,
        "Digite o nome da primeira cidade",
        tipo_validacao="se_nao_existe"
    )

    if not cidade_01:
        return

    cidade_02 = obter_cidade_validada(
        objeto,
        "Digite o nome da segunda cidade",
        tipo_validacao="se_nao_existe"
    )

    if not cidade_02:
        return

    distancia = verificar_numero(
        "Digite a distância entre as cidades (Km): ", float, Cor.MAGENTA
    )

    objeto.cadastra_conexao(cidade_01, cidade_02, distancia)

    imprimir_cabecalho(
        "Dados cadastrados com sucesso.", cor=Cor.VERDE
    )

    pausar()


def listar_cidades(objeto: Grafo):
    imprimir_cabecalho("LISTAR CIDADES", cor=Cor.LARANJA)

    if len(objeto.cidades) == 0:
        mostrar_erro("E04", cor=Cor.AMARELO)
        return

    objeto.lista_cidades()

    pausar()


def listar_conexoes(objeto: Grafo):
    imprimir_cabecalho("LISTAR CONEXÕES", cor=Cor.LARANJA)

    if len(objeto.cidades) == 0:
        mostrar_erro("E04", cor=Cor.AMARELO)
        return

    objeto.lista_conexoes()

    pausar()


def listar_cidades_vizinhas(objeto: Grafo):
    imprimir_cabecalho("LISTAR CIDADES VIZINHAS", cor=Cor.LARANJA)

    if len(objeto.cidades) == 0:
        mostrar_erro("E04", cor=Cor.AMARELO)
        return

    cidade_escolhida = obter_cidade_validada(
        objeto, "Qual cidade quer pesquisar", "se_nao_existe")

    if not cidade_escolhida:
        return

    objeto.lista_vizinhas(cidade_escolhida)

    pausar()


def salvar_arquivo(objeto: Grafo):

    objeto.salva_arquivo()

    imprimir_cabecalho("Dados salvos com sucesso.", cor=Cor.VERDE)

    pausar()


def main():
    meu_grafo = Grafo.carregar_arquivo("grafos.csv")
    opcoes_menu = [
        "CADASTRAR CIDADE",
        "CADASTRAR CONEXÃO",
        "LISTAR CIDADES",
        "LISTAR CONEXÕES",
        "LISTAR CIDADES VIZINHAS",
        "SALVAR ARQUIVO CSV"
    ]
    escolha_menu = {
        1: cadastrar_cidades,
        2: cadastrar_conexoes,
        3: listar_cidades,
        4: listar_conexoes,
        5: listar_cidades_vizinhas,
        6: salvar_arquivo
    }

    while True:
        imprimir_cabecalho("SISTEMA DE GRAFOS v1", cor=Cor.LARANJA)

        criar_menu(opcoes_menu)

        opcao_digitada = verificar_numero(
            "Digite a opção desejada: ", int, permitir_zero=True)

        opcao_escolhida = escolha_menu.get(opcao_digitada)

        if opcao_escolhida:
            opcao_escolhida(meu_grafo)
        elif opcao_digitada == 0:
            meu_grafo.salva_arquivo()

            imprimir_cabecalho("SISTEMA SENDO ENCERRADO...", cor=Cor.VERDE)

            break
        else:
            mostrar_erro("E01", Cor.VERMELHO)


if __name__ == "__main__":
    main()
