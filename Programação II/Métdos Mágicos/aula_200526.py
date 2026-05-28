class Moeda:
    def __init__(self, reais, centavos=0):
        self.total = reais*100 + centavos
        self.reais = self.total//100  # // divisão dos inteiros
        self.centavos = self.total % 100

    def __str__(self):
        return f"R$ {self.reais},{self.centavos:02d}"

    def total_centavos(self):
        return self.reais*100 + self.centavos

    def __add__(self, outro_valor):
        total = self.total + outro_valor.total
        return Moeda(0, total)

    def __eq__(self, outro_valor):
        return self.total == outro_valor.total

    def __lt__(self, outro_valor):
        return self.total < outro_valor.total

    def __repr__(self):
        return f"Classe Moeda({self.reais},{self.centavos:02d})"


if __name__ == "__main__":
    x = Moeda(10, 5)
    y = Moeda(89, 32)
    j = Moeda(0, 9937)
    print(x)
    print(y)
    w = x + y
    print(w < j)
    print(w == j)
    print(x < y)
    print(repr(x))
