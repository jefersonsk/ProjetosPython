from datetime import datetime


class Passagem_Aerea:
    def __init__(self,
                 numero_bilhete,
                 origem,
                 destino,
                 data_hora,
                 passageiro):
        self.numero_bilhete = numero_bilhete
        self.origem = origem
        self.destino = destino
        self.data_hora = data_hora
        self.passageiro = passageiro
        self.passageiro.lista_bilhete.append(self)

    def info(self):
        print("---- INFORMAÇÕES BILHETE ----")
        print(f"NÚMERO BILHETE: {self.numero_bilhete}")
        print(f"ORIGEM: {self.origem}")
        print(f"DESTINO: {self.destino}")
        print(f"DATA: {self.data_hora.strftime("%d/%m/%Y")}")
        print(f"HORA: {self.data_hora.strftime("%H:%M")}")
        self.passageiro.info()

    # @classmethod
    # def construtor_via_teclado(cls):
    #     numero_bilhete = int(input("Número do bilhete: "))
    #     origem = input("Origem: ")
    #     destino = input("Destino: ")
    #     data = input("Data: ")
    #     hora = input("Hora: ")
    #     cpf_passageiro = input("CPF do Passageiro: ")

    #     return cls(
    #         numero_bilhete,
    #         origem,
    #         destino,
    #         data,
    #         hora,
    #         cpf_passageiro)


class Pessoa:
    def __init__(self,
                 cpf,
                 nome,
                 sobrenome):
        self.cpf = cpf
        self.nome = nome
        self.sobrenome = sobrenome
        self.lista_bilhetes = []

    def info(self):
        print("---- INFORMAÇÃO PASSAGEIRO ----")
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")


if __name__ == "__main__":

    passageiro = Pessoa("89868927072", "Jeferson", "Silveira")
    passagem = Passagem_Aerea(123,
                              "POA",
                              "GRU",
                              datetime(2026, 10, 3, 14, 30),
                              passageiro)

    passagem.info()
    # print(passageiro.info())
