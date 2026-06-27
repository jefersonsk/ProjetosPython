class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = "Curso em Vídeo"

    def se_apresentar(self):
        print(
            f"Olá, sou {self.nome} e sou {self.cargo} "
            f"do setor de {self.setor} da empresa {self.empresa}"
        )


if __name__ == "__main__":
    c1 = Funcionario("Jeferson", "TI", "Programador")

    c1.se_apresentar()
