class Pessoa:
    def __init__(self, nome_completo, telefone):
        self.__nome_completo = nome_completo
        self.__telefone = telefone

    @property
    def nome_completo(self):
        return self.__nome_completo

    @property
    def telefone(self):
        return self.__telefone

    def altera_contato(self, tel_novo=None):
        if tel_novo is None:
            tel_novo = input("Digite o novo telefone: ")
            self.__telefone = tel_novo

        self.__telefone = tel_novo

    def info(self):
        print(">>> Cliente <<<")
        imprimir_linha()
        print(f"NOME: {self.__nome_completo}")
        print(f"TELEFONE: {self.__telefone}")
        imprimir_linha()


class Mecanico(Pessoa):
    def __init__(self, nome_completo, telefone, especialidade, salario):
        super().__init__(nome_completo, telefone)
        self.__especialidade = especialidade
        self.__salario = salario
        self.__lista_servicos = []

    def info(self):
        print(f"NOME: {self.nome_completo}")
        print(f"TELEFONE: {self.telefone}")
        print(f"ESPECIALIDADE: {self.__especialidade}")
        print(f"SALÁRIO: R$ {self.__salario:.2f}")
        self.listar_servicos()

    def atribuir_servico(self, servico):
        self.__lista_servicos.append(servico)
        servico.mecanico_responsavel = self

    def listar_servicos(self):
        print(50 * "=")
        print(f">>> Serviços do Mecânico: {self.nome_completo}")
        for servico in self.__lista_servicos:
            print(f"CÓDIGO: {servico.codigo}")
            print(f"VALOR: {servico.valor}")
            print(f"CARRO: {servico.carro.modelo}")
            print(f"DESCRIÇÃO DO SERVIÇO: {servico.descricao_servico}")
        print(50 * "=")


class Carro:
    def __init__(self, modelo, ano, proprietario, observacoes):
        self.__modelo = modelo
        self.__ano = ano
        self.__proprietario = proprietario
        self.__observacoes = observacoes

    @property
    def modelo(self):
        return self.__modelo

    def info(self):
        print(">>> Carro <<<")
        imprimir_linha()
        print(f"MODELO: {self.__modelo}")
        print(f"ANO: {self.__ano}")
        print(f"PROPRIETÁRIO: {self.__proprietario.nome_completo}")
        print(f"OBSERVAÇÕES: {self.__observacoes}")
        imprimir_linha()


class Servico:
    def __init__(
        self, codigo, valor, carro, descricao_servico, mecanico_responsavel=None
    ):
        self.codigo = codigo
        self.valor = valor
        self.carro = carro
        self.descricao_servico = descricao_servico
        self.mecanico_responsavel = mecanico_responsavel

    def info(self):
        print(">>> Serviço <<<")
        print(f"CÓDIGO: {self.codigo}")
        print(f"VALOR: R$ {self.valor}")
        print(f"CARRO: {self.carro.modelo}")
        print(f"DESCRIÇÃO DO SERVIÇO: {self.descricao_servico}")
        print(
            f"MECÂNICO RESPONSÁVEL: {self.mecanico_responsavel.nome_completo}"
        )


def imprimir_linha():
    print(50 * "-")


if __name__ == "__main__":
    # Criação de Objetos
    pessoa_01 = Pessoa("Jeferson Silveira", "51 988887765")
    mecanico_01 = Mecanico("Pipe Gamer", "51 87776655", "Suspensão", 9000.00)
    carro_01 = Carro("HB20", 2014, pessoa_01, "Branco - 4 Portas - 1.0")

    # Criação de Serviço
    servico_01 = Servico(1, 250.00, carro_01, "Troca de Óleo")

    # Atribuição de Serviço ao Mecânico
    mecanico_01.atribuir_servico(servico_01)

    # Exibições na tela
    pessoa_01.info()
    imprimir_linha()
    mecanico_01.info()
    imprimir_linha()
    carro_01.info()
    imprimir_linha()
    servico_01.info()
