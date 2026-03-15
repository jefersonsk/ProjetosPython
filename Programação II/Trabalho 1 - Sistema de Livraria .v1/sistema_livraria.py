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
    criar_linha("-")

def criar_cabecalho(texto: str, quantidade: int = 60) -> None:
    criar_linha("-")
    print(texto.center(quantidade))
    criar_linha("-")

def criar_linha(caracter: str, quantidade: int = 60) -> None:
    print(quantidade * caracter)

def verifica_numero(texto: str, tipo_conversao: type) -> int | float:
    while True:
        try:
            return tipo_conversao(input(texto))
        except (ValueError):
            mostrar_erro("E01", VERMELHO)
        
def mostrar_erro(codigo: str, cor: str) -> None:
    print(f"\n{cor}===== ERRO - {MENSAGEM_ERRO.get(codigo, "Erro Desconhecido")} ====={RESET}")

criar_cabecalho("SISTEMA DE LIVRARIA .v1")

criar_menu(["CADASTRAR NOVO LIVRO", 
              "LISTAR LIVROS", 
              "BUSCAR LIVROS POR NOME", 
              "BUSCAR LIVROS POR CATEGORIA", 
              "BUSCAR LIVROS POR PREÇO",
              "BUSCA POR QUANTIDADE EM ESTOQUE",
              "VALOR TOTAL EM ESTOQUE"])