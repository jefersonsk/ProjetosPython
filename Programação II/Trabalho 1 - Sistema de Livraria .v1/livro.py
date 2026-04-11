from utilidades import Cor, imprimir_linha

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
        print(f"{Cor.VERDE_CLARO}{'>' * 6} Cod#{self.codigo:04}{Cor.RESET}")
        print(f"{Cor.AZUL}Título / Editora: {Cor.AMARELO}{self.titulo} / {self.editora}{Cor.RESET}")
        print(f"{Cor.AZUL}Categoria: {Cor.AMARELO}{self.area}{Cor.RESET}")
        print(f"{Cor.AZUL}Ano: {Cor.AMARELO}{self.ano}{Cor.RESET}")
        print(f"{Cor.AZUL}Valor: {Cor.AMARELO}R$ {self.valor:.2f}{Cor.RESET}")
        print(f"{Cor.AZUL}Estoque: {Cor.AMARELO}{self.quantidade_estoque}{Cor.RESET}")
        print(
            f"{Cor.AZUL}Valor total em estoque: "
            f"{Cor.AMARELO}R$ {self.calcular_valor_total():.2f}{Cor.RESET}"
        )
        imprimir_linha("-")


    def calcular_valor_total(self):
        return self.valor * self.quantidade_estoque
    

    def formatar_para_csv(self):
        return f"{self.codigo},{self.titulo},{self.editora},{self.area},{self.ano},{self.valor},{self.quantidade_estoque}"
