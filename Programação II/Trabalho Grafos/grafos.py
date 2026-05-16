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
        for item in self.cidades:
            if item.nome_cidade == nome:
                return

        # Instância um objeto do tipo Vertice
        nova_cidade = Vertice(nome)

        # Adiciona esse objeto na lista de cidades do Grafo
        self.cidades.append(nova_cidade)

    def cadastra_conexao(self, nome_cidade1, nome_cidade2, distancia):
        vertice1 = None
        vertice2 = None

        for item in self.cidades:
            if item.nome_cidade == nome_cidade1:
                vertice1 = item
            elif item.nome_cidade == nome_cidade2:
                vertice2 = item

        nova_aresta = Aresta(vertice1, vertice2, distancia)

        self.conexoes.append(nova_aresta)

        vertice1.vizinhanca.append(vertice2)
        vertice2.vizinhanca.append(vertice1)
        vertice1.conexoes.append(nova_aresta)
        vertice2.conexoes.append(nova_aresta)

    def listar_cidades(self):
        nomes_cidades = []

        for item in self.cidades:
            nomes_cidades.append(item.nome_cidade)

        nomes_cidades.sort()

        for item in nomes_cidades:
            print(item)

    def listar_conexoes(self):
        for aresta in self.conexoes:
            print(
                f"{aresta.cidade1.nome_cidade}, "
                f"{aresta.cidade2.nome_cidade}: "
                f"{aresta.distancia} Km"
            )

    def listar_vizinhas(self, nome_cidades):
        cidade_alvo = None
        lista_vizinhos = []

        for item in self.cidades:
            if item.nome_cidade == nome_cidades:
                cidade_alvo = item

        if cidade_alvo is not None:
            for item in cidade_alvo.conexoes:
                if item.cidade1 == cidade_alvo:
                    lista_vizinhos.append(
                        [item.distancia, item.cidade2.nome_cidade])
                else:
                    lista_vizinhos.append(
                        [item.distancia, item.cidade1.nome_cidade])

            lista_vizinhos.sort()

            for item in lista_vizinhos:
                print(f"{item[1]}: {item[0]:.2f} Km")
        else:
            print("Cidade não encontrado no sistema.")

    def carregar_arquivo(self, nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for dados in arquivo:
                cache = dados.strip.split(",")

                self.cadastra_cidade(cache[0])
                self.cadastra_cidade(cache[1])
                self.cadastra_conexao(cache[0], cache[1], int(cache[2]))


def criar_menu(lista: list) -> str:
    for i, item in enumerate(lista, start=1):
        print(f"{i} - {item}")
    print("0 - SAIR")


def cadastrar_cidades(objeto: object):
    cidade = input("Digite a cidade: ")
    print(f"Cidade {cidade} cadastrada com sucesso!")


def main():
    meu_grafo = Grafo()
    opcoes_menu = [
        "CADASTRAR CIDADE",
        "CADASTRAR CONEXÃO",
        "LISTAR CIDADES",
        "LISTAR CONEXÕES",
        "LISTAR CIDADES VIZINHAS",
        "CARREGAR ARQUIVO CSV"
    ]
    escolha_menu = {
        1: cadastrar_cidades,
        # 2: cadastrar_conexoes,
        # 3: listar_cidades,
        # 4: listar_conexoes,
        # 5: listar_cidades_vizinhas,
        # 6: carregar_arquivo_csv
    }

    while True:
        criar_menu(opcoes_menu)

        opcao_digitada = int(input("Digite a opção desejada: "))

        opcao_escolhida = escolha_menu.get(opcao_digitada)

        if opcao_escolhida:
            opcao_escolhida(meu_grafo)
        elif opcao_digitada == 0:
            print("Sistema sendo encerrado...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
