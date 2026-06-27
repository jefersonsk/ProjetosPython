class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(">>> Produto <<<")
        print(40 * "=")
        print(f"Nome: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(40 * "=")


if __name__ == "__main__":
    produto_01 = Produto("Mouse", 120.00)
    produto_02 = Produto("Teclado", 250.00)

    produto_01.etiqueta()
    produto_02.etiqueta()
