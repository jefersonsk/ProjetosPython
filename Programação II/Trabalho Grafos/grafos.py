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
