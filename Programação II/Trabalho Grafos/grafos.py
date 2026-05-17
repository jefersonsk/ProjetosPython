from utilidades import (
    Cor,
    verificar_numero,
    imprimir_cabecalho,
    criar_menu,
    continuar,
    enter_para_sair,
    imprimir_linha,
    mostrar_erro
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
        for item in self.cidades:
            if item.nome_cidade.strip().lower() == nome.strip().lower():
                return False

        nova_cidade = Vertice(nome)
        self.cidades.append(nova_cidade)
        return True

    def cadastra_conexao(self, nome_cidade1, nome_cidade2, distancia):
        vertice1 = None
        vertice2 = None

        for item in self.cidades:
            if item.nome_cidade == nome_cidade1:
                vertice1 = item
            elif item.nome_cidade == nome_cidade2:
                vertice2 = item
            else:
                return False

        nova_aresta = Aresta(vertice1, vertice2, distancia)

        self.conexoes.append(nova_aresta)

        vertice1.vizinhanca.append(vertice2)
        vertice2.vizinhanca.append(vertice1)
        vertice1.conexoes.append(nova_aresta)
        vertice2.conexoes.append(nova_aresta)
        return True

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


def cadastrar_cidades(objeto: Grafo):
    while True:
        imprimir_cabecalho("CADASTRAR CIDADE", cor=Cor.LARANJA)

        cidade = enter_para_sair("Digite o nome da cidade", Cor.MAGENTA)

        if not cidade:
            return
        
        validacao_dos_dados = objeto.cadastra_cidade(cidade)
        if not validacao_dos_dados:
            mostrar_erro("E02", Cor.AMARELO)
            continue
        
        print(
            f"\n{Cor.CIANO}Cidade {Cor.AMARELO}{cidade}{Cor.CIANO}" 
            f"cadastrada com sucesso!{Cor.RESET}"
        )


def cadastrar_conexoes(objeto: Grafo):
    cidade_01 = input("Digite o nome da primeira cidade: ")
    cidade_02 = input("Digite o nome da segunda cidade: ")
    distancia = verificar_numero("Digite a distância entre as cidades: ", float)

    validacao_dos_dados = objeto.cadastra_conexao(cidade_01, cidade_02, distancia)

    if validacao_dos_dados:
        imprimir_cabecalho("Dados cadastrados com sucesso.", cor=Cor.AMARELO)
    else:
        print("Erro")

def lista_cidades(objeto: Grafo):
    objeto.listar_cidades()

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
        2: cadastrar_conexoes,
        3: lista_cidades,
        # 4: listar_conexoes,
        # 5: listar_cidades_vizinhas,
        # 6: carregar_arquivo_csv
    }

    while True:
        imprimir_cabecalho("SISTEMA DE GRAFOS v1", cor=Cor.LARANJA)

        criar_menu(opcoes_menu)

        opcao_digitada = verificar_numero("Digite a opção desejada: ", int, permitir_zero=True)

        opcao_escolhida = escolha_menu.get(opcao_digitada)

        if opcao_escolhida:
            opcao_escolhida(meu_grafo)
        elif opcao_digitada == 0:
            imprimir_cabecalho("SISTEMA SENDO ENCERRADO...", cor=Cor.VERDE)
            break
        else:
            mostrar_erro("E01", Cor.VERMELHO)


if __name__ == "__main__":
    main()
