class Veiculo:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.proprietario = None

    def info(self):
        print("-----> INFORMAÇÕES DO VEÍCULO")
        print("=" * 30)
        print(f"PLACA: {self.placa}")
        print(f"MODELO: {self.modelo}")
        print(f"ANO: {self.ano}")
        # if self.proprietario is not None:
        #     self.proprietario.info()

    def compra(self, novo_dono):
        self.proprietario = novo_dono


class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, nr_ocupantes):
        super().__init__(placa, modelo, ano)  # Chama a classe pai, nesse caso Veiculo
        self.nr_ocupantes = nr_ocupantes

    def info(self):
        super().info()
        print(f"NÚMERO DE OCUPANTES: {self.nr_ocupantes}")
        if self.proprietario is not None:
            self.proprietario.info()


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, ano, carga_atual):
        super().__init__(placa, modelo, ano)
        self.carga_atual = carga_atual

    def carga(self, carregamento):
        self.carga_atual += carregamento

    def descarga(self, descarga):
        self.carga_atual -= descarga

    def info(self):
        super().info()
        print(f"CARGA ATUAL: {self.carga_atual}")
        if self.proprietario is not None:
            self.proprietario.info()


class Pessoa:
    def __init__(self, cpf, nome, sobrenome):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome

    def info(self):
        print("-----> INFORMAÇÕES PESSOA")
        print(f"CPF: {self.cpf}")
        print(f"NOME: {self.nome}")
        print(f"SOBRENOME: {self.sobrenome}")


if __name__ == "__main__":
    caminhao = Caminhao("XYZ-1234",
                        "Mercedes Super",
                        1980,
                        50, )

    carro = Carro("XYZ-9999",
                  "Classic",
                  1980,
                  5)

    # carro = Carro("")

    pessoa = Pessoa("898689270-72", "Jeferson", "Silveira")

    # caminhao.carga(50)
    # caminhao.descarga(60)
    # caminhao.info()

    carro.compra(pessoa)

    carro.info()
