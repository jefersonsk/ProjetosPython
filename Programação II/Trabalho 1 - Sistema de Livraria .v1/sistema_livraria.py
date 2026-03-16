VERDE = "\033[32m"
LARANJA = "\033[33m"
AZUL = "\033[34m"
CIANO = "\033[36m"
AMARELO = "\033[93m"
VERMELHO = "\033[31m"
RESET = "\033[0m"

MENSAGEM_ERRO = {"E01": "Valor inválido."}

class Livro:
    def __init__(self, titulo, codigo, editora, area, ano, valor, quantidade_estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.quantidade_estoque = quantidade_estoque

    def mostrar_informacoes(self):
        print(f"{"<" * 6} Cod#{self.codigo}")
        print(f"Título/Editora: {self.titulo}/{self.editora}")
        print(f"Categoria: {self.area}")
        print(f"Ano: {self.ano}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Estoque: {self.quantidade_estoque}")
        print(f"Valor total em estoque: R$ {self.valor * self.quantidade_estoque:.2f}")

def criar_menu(lista_opcoes: list) -> None:
    for i, item in enumerate(lista_opcoes, start=1):
        print(f"{i} - {item}")

    print("0 - ENCERRAR ATIVIDADES")
    imprimir_linha("-")

def imprimir_cabecalho(texto: str, quantidade: int = 60) -> None:
    imprimir_linha("-")
    print(texto.center(quantidade))
    imprimir_linha("-")

def imprimir_linha(caracter: str, quantidade: int = 60) -> None:
    print(quantidade * caracter)

def verifica_numero(texto: str, tipo_conversao: type) -> int | float:
    while True:
        try:
            return tipo_conversao(input(texto))
        except (ValueError):
            mostrar_erro("E01", VERMELHO)
        
def mostrar_erro(codigo: str, cor: str) -> None:
    print(f"\n{cor}===== ERRO - {MENSAGEM_ERRO.get(codigo, "Erro Desconhecido")} ====={RESET}")

def cadastrar_livros(lista_livros: list):

    livro = input("LIVRO: ")

def listar_livros(listar_livros: list):
    print("2")

def buscar_livros_nome(listar_livros: list):
    print("3")

def buscar_livros_categoria(listar_livros: list):
    print("4")

def buscar_livros_preco(listar_livros: list):
    print("5")

def buscar_quantidade_estoque(listar_livros: list):
    print("6")

def valor_total_estoque(listar_livros: list):
    print("7")

def encerrar_atividades():
    print("\nSistema encerrado\n")
    exit()

def main():
    lista_livros = []
    escolhas_menu = {1: cadastrar_livros,
                     2: listar_livros,
                     3: buscar_livros_nome,
                     4: buscar_livros_categoria,
                     5: buscar_livros_preco,
                     6: buscar_quantidade_estoque,
                     7: valor_total_estoque,
                     0: encerrar_atividades}

    imprimir_cabecalho("SISTEMA DE LIVRARIA .v1")

    criar_menu(["CADASTRAR NOVO LIVRO", 
                "LISTAR LIVROS", 
                "BUSCAR LIVROS POR NOME", 
                "BUSCAR LIVROS POR CATEGORIA", 
                "BUSCAR LIVROS POR PREÇO",
                "BUSCA POR QUANTIDADE EM ESTOQUE",
                "VALOR TOTAL EM ESTOQUE"])

if __name__ == "__main__":
    main()