class Livro:
    def __init__(self, nome, numero_paginas):
        self.nome = nome
        self.numero_paginas = numero_paginas
        self.pagina_atual = None

    def avancar_paginas(self, quantidade_paginas):
        pagina = 0

        if self.pagina_atual is None:
            self.pagina_atual = 1

            print(
                f"Você abriu o livro {self.nome} "
                f"que tem {self.numero_paginas} páginas."
            )
            print(f"Você agora está na página {self.pagina_atual}")

        for pagina in range(1, quantidade_paginas + 1, 1):
            if self.pagina_atual <= self.numero_paginas:
                print(self.pagina_atual)
                self.pagina_atual += 1
                print(f"> Pág{self.pagina_atual}", end=" ")

        print(f"Você avançou {quantidade_paginas} páginas")
        print(f"Agora você está na página {self.pagina_atual}.")


if __name__ == "__main__":
    livro_01 = Livro("Senhor dos Aneis", 15)

    livro_01.avancar_paginas(5)
    livro_01.avancar_paginas(10)
    livro_01.avancar_paginas(3)
