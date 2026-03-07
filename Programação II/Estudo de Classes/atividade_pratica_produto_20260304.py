class Produto:
    def __init__(self, marca, modelo, valor, estoque):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.estoque = estoque

    def Informacao(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Valor: R$ {self.valor:.2f}")
        print(f"Estoque: {self.estoque}")
        print(30 * "=")

    def AlteraValor(self):
        print("--- ALTERAÇÃO NO PRODUTO ---\n")
        self.Informacao()
        self.valor = float(input("Digite o novo valor: R$ "))

    def AlteraEstoque(self):
        print("--- ALTERAÇÃO NO PRODUTO ---")
        self.Informacao()
        self.estoque = int(input("Digite a nova quantidade de estoque: "))

def MostraProdutos(lista: list[Produto]) -> None:
    """Recebe uma lista com dados e exibe na tela.

    Args:
        lista (list{Produto}): Lista com os dados que deve ser exibidos.
    """

    for produto in lista:
        produto.Informacao()

if __name__ == '__main__':

    lista_produtos = []

    lista_produtos.append(Produto("Teclado", "Dell", 130, 15))
    lista_produtos.append(Produto("Monitor", "Acer", 450, 19))

    lista_produtos[0].AlteraValor()
    print()
    lista_produtos[1].AlteraEstoque()
    print(30 * "=")

    MostraProdutos(lista_produtos)