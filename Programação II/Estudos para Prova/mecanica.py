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

    @telefone.setter
    def telefone(self, novo_valor):
        if novo_valor == "":
            print("Valor inválido")
        else:
            self.__telefone = novo_valor

    def altera_contatos(self, telefone_novo=None):
        if telefone_novo is None:
            self.telefone = input("Digite novo telefone: ")
        else:
            self.telefone = telefone_novo

    def info(self):
        print(">>>> Pessoa")
        imprimir_linha()
        print(f"Nome Cliente: {self.__nome_completo}")
        print(f"Telefone: {self.__telefone}")
        imprimir_linha()


class Mecanico(Pessoa):
    def __init__(self, nome_completo, telefone, especialidade, salario):
        super().__init__(nome_completo, telefone)
        self.__especialidade = especialidade
        self.__salario = salario
        self.__lista_servicos = []

    def info(self):
        print(">>>> Mecanico")
        imprimir_linha()
        print(f"Nome Mecânico: {self.nome_completo}")
        print(f"Telefone: {self.telefone}")
        print(f"Especialidade: {self.__especialidade}")
        print(f"Salário: {self.__salario:.2f}")
        imprimir_linha()

    def listar_servico(self):
        print(f">>>> Serviços do Mecânico: {self.nome_completo}")
        imprimir_linha()
        for servico in self.__lista_servicos:
            print(f"Código: #{servico.codigo}")
            print(f"Carro: {servico.carro.modelo}")
            print(f"Descrição do Serviço: {servico.descricao_servico}")
            imprimir_linha()

    def atribuir_servico(self, servico):
        self.__lista_servicos.append(servico)

    def altera_especialidade(self, nova_necessidade=None):
        if nova_necessidade is None:
            self.__especialidade = input("Digite nova especialidade: ")
        else:
            self.__especialidade = nova_necessidade


class Carro:
    def __init__(self, modelo, ano, proprietario, observacoes):
        self.__modelo = modelo
        self.__ano = ano
        self.__proprietario = proprietario
        self.__observacoes = observacoes

    @property
    def modelo(self):
        return self.__modelo

    def altera_observacoes(self):
        pass

    def info(self):
        print(">>>> Carro")
        imprimir_linha()
        print(f"Modelo: {self.__modelo}")
        print(f"Ano: {self.__ano}")
        print(f"Proprietario: {self.__proprietario.nome_completo}")
        print(f"Observações: {self.__observacoes}")
        imprimir_linha()


class Servico:
    def __init__(self, codigo, valor, mecanico, carro, descricao_servico):
        self.codigo = codigo
        self.valor = valor
        self.mecanico = mecanico
        self.carro = carro
        self.descricao_servico = descricao_servico

    def info(self):
        print(">>>> Servico")
        imprimir_linha()
        print(f"Código: #{self.codigo}")
        print(f"Valor: R$ {self.valor}")
        print(f"Mecânico Responsável: {self.mecanico.nome_completo}")
        print(f"Carro: {self.carro.modelo}")
        print(f"Descrição Serviço: {self.descricao_servico}")
        imprimir_linha()

    # def atualiza_servico(self, novo_valor=None, nova_descriacao=None):
    #     pass


def imprimir_linha():
    print(50 * "-")


if __name__ == "__main__":
    pessoa_01 = Pessoa("Jeferson", "51-98453394")
    mecanico_01 = Mecanico("Pipe", "51-55555555", "Eletricista", 500.00)
    carro_01 = Carro("Celta", 2002, pessoa_01, "Cor vermelha")
    carro_02 = Carro("HB20", 2022, pessoa_01, "Cor Azul")
    servico_01 = Servico(1, 200.00, mecanico_01, carro_01, "Problema no Freio")
    servico_02 = Servico(2, 400.00, mecanico_01, carro_02, "Trocar Óleo")

    pessoa_01.info()
    mecanico_01.info()
    carro_01.info()
    servico_01.info()

    mecanico_01.atribuir_servico(servico_01)
    mecanico_01.atribuir_servico(servico_02)

    mecanico_01.listar_servico()

    pessoa_01.altera_contatos()

    pessoa_01.info()
